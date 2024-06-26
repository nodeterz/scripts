import numpy as np
import scipy
from ase.io import read
from time import time
import sys
from numba import jit
#sys.stdout=open('fpLaplace.out', 'w')
#sys.stderr=open('fpLaplace.err', 'w')


def get_dist(xyz=None):
    dist_vec = scipy.spatial.distance.pdist(X=xyz, metric='euclidean')
    return scipy.spatial.distance.squareform(X=dist_vec)

@jit(nopython=True)
def DiagHF(fpd, wa, ind2, nat):
    for lat in range(nat):
        for kat in range(nat):
            for jat in range(nat):
                fpd[kat, lat] += wa[kat, jat]*ind2[jat, lat]**2
    return fpd

@jit(nopython=True)
def OffDiagHF(fpd, wa, ind2, nat):
    for lat in range(nat):
        for iat in range(nat):
            for jat in range(0,iat):
                fpd[iat, lat] -= wa[iat, jat]*(2.E0*ind2[iat, lat]*ind2[jat, lat])
            for jat in range(iat+1,nat):
                fpd[iat, lat] -= wa[iat, jat]*(2.E0*ind2[iat, lat]*ind2[jat, lat])
    return fpd

@jit(nopython=True)
def TraceNDer(x, nat, ind4, wa):
    for iat in range(nat):
        for jat in range(0, iat):
            dx = x[iat]-x[jat]
            tt = ind4[iat, jat]
            wa[iat, jat] = dx*tt
            wa[jat, iat] = -dx*tt
    return wa

@jit(nopython=True)
def DiagDer(nat, wa):
    for jat in range(nat):
        tx = 0.E0
        for iat in range(nat):
            if iat == jat:
                continue
            tx -= wa[iat, jat]
        wa[jat, jat] = tx
    return wa


def get_laplace_fingerprint(input_str=None, calcDerivative=True, verbose=False):
    x_val = input_str.get_positions()[:, 0]
    y_val = input_str.get_positions()[:, 1]
    z_val = input_str.get_positions()[:, 2]
    nat = input_str.get_global_number_of_atoms()
    t_call_dist_mat = time()
    dist_mat = get_dist(xyz=input_str.get_positions())
    d2 = np.multiply(dist_mat, dist_mat)
    d4 = np.multiply(d2, d2)
    inv_d2 = np.divide(-1.E0, d2, out=np.zeros_like(d2), where=d2 != 0)
    np.fill_diagonal(inv_d2, -1.E0*inv_d2.sum(axis=1))
    t_call_dist_mat = time()-t_call_dist_mat

    t_call_eig = time()
    fp_arr, inv_d2 = np.linalg.eigh(inv_d2, UPLO='U')
    idx = np.argsort(fp_arr)
    fp_arr = fp_arr[idx]
    if calcDerivative == False :
        return fp_arr
    if calcDerivative == True :
        inv_d2 = inv_d2[:, idx]
        t_call_eig = time()-t_call_eig

        fp_der_arr = np.zeros(shape=(3, nat, nat))

        #  Trace and its derivative
        t_call_trace = time()
        inv_d4 = np.divide(2.E0, d4, out=np.zeros_like(d4), where=d4 != 0)
        work_arr = np.zeros(shape=(3, nat, nat), dtype=np.float64)
        work_arr[0]=TraceNDer(x=x_val, nat=nat, ind4=inv_d4, wa=work_arr[0])
        work_arr[1]=TraceNDer(x=y_val, nat=nat, ind4=inv_d4, wa=work_arr[1])
        work_arr[2]=TraceNDer(x=z_val, nat=nat, ind4=inv_d4, wa=work_arr[2])
        t_call_trace = time()-t_call_trace
        # contribution of off-diagonal matrix elements to derivative of eval(nat) using the Hellmann-Feynmann
        t_call_hf = time()
        fp_der_arr[0] = OffDiagHF(fpd=fp_der_arr[0], wa=work_arr[0], ind2=inv_d2, nat=nat)
        fp_der_arr[1] = OffDiagHF(fpd=fp_der_arr[1], wa=work_arr[1], ind2=inv_d2, nat=nat)
        fp_der_arr[2] = OffDiagHF(fpd=fp_der_arr[2], wa=work_arr[2], ind2=inv_d2, nat=nat)
        t_call_hf = time()-t_call_hf
        # derivatives of diagonal elements from derivatives of  off-diagonal elements
        t_call_od = time()
        work_arr[0]=DiagDer(nat=nat, wa=work_arr[0])
        work_arr[1]=DiagDer(nat=nat, wa=work_arr[1])
        work_arr[2]=DiagDer(nat=nat, wa=work_arr[2])
        t_call_od = time()-t_call_od
        # contribution of diagonal matrix elements to derivative of eval(nat) using Hellmann-Feynmann
        t_call_odhf = time()
        fp_der_arr[0] = DiagHF(fpd=fp_der_arr[0], wa=work_arr[0], ind2=inv_d2, nat=nat)
        fp_der_arr[1] = DiagHF(fpd=fp_der_arr[1], wa=work_arr[1], ind2=inv_d2, nat=nat)
        fp_der_arr[2] = DiagHF(fpd=fp_der_arr[2], wa=work_arr[2], ind2=inv_d2, nat=nat)
        t_call_odhf = time()-t_call_odhf
        if verbose:
            fp_stream = open('FP.dat', 'w')
            fp_der_stream = open('FPdev.dat', 'w')
            for iat in range(nat):
                fp_stream.write('%4d %.18f\n' % (iat+1, fp_arr[iat]))
                for jat in range(nat):
                    fp_der_stream.write(
                        f'{iat + 1:4d} {jat + 1:4d} '
                        f'{fp_der_arr[0, iat, jat]:.18f} '
                        f'{fp_der_arr[1, iat, jat]:.18f} '
                        f'{fp_der_arr[2, iat, jat]:.18f}\n')
            fp_stream.close()
            fp_der_stream.close()
            print('DistMat: %.6f (sec)' % (t_call_dist_mat))
            print('EigenVal: %.6f (sec)' % (t_call_eig))
            print('Trace: %.6f (sec)' % (t_call_trace))
            print('HF: %.6f (sec)' % (t_call_hf))
            print('Off-diagonal: %.6f (sec)' % (t_call_od))
            print('Off-diagonal HF: %.6f (sec)' % (t_call_odhf))
            sys.stdout.flush()
        return fp_arr, fp_der_arr


def get_laplace_fingerprint_distance(src_struct, fp_trg_arr):
    fp_src_arr, fp_src_der_arr = get_laplace_fingerprint(src_struct,verbose=True)
    fp_dist = np.linalg.norm(fp_src_arr-fp_trg_arr)**2
    delta_fp_dist = np.subtract(fp_src_arr, fp_trg_arr)
    delta_fp_der_dist = fp_src_der_arr
    element_wise_product = np.multiply(delta_fp_dist, delta_fp_der_dist)
    fp_dist_der = 2.E0*np.sum(element_wise_product, axis=2)
    
    return fp_dist, fp_dist_der.T


if __name__ == '__main__':
    structure = read('posinp.xyz')
    structure_Target = read('posinp2.xyz')
    FP, FP_der = get_laplace_fingerprint(structure_Target, verbose=False)
    FP_dist, FP_dist_der = get_laplace_fingerprint_distance(src_struct=structure, fp_trg_arr=FP)
    stream1=open('S1.txt','w')
    stream2=open('S2.txt','w')
    stream2.write('%.12f\n'%FP_dist)
    for j in range(structure.get_global_number_of_atoms()):
        stream2.write('%03d %.12f %.12f %.12f %.12f\n'%(j,FP[j],FP_dist_der[j,0],FP_dist_der[j,1],FP_dist_der[j,2]))
        for k in range(structure.get_global_number_of_atoms()):
            stream1.write('%03d %03d %.12f  %.12f %.12f\n'%(j,k,FP_der[0,j,k],FP_der[1,j,k],FP_der[2,j,k]))
    stream1.close()
    stream2.close()

