import numpy as np
import scipy
from ase.io import read
from time import time


def get_dist(xyz=None):
    dist_vec = scipy.spatial.distance.pdist(X=xyz, metric='euclidean')
    return scipy.spatial.distance.squareform(X=dist_vec)


def get_laplace_fingerprint(input_str=None, verbose=False, calcDer=None):
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
    if calcDer == False:
        return fp_arr
    elif calcDer == True:
        inv_d2 = inv_d2[:, idx]
        t_call_eig = time()-t_call_eig
        fp_der_arr = np.zeros(shape=(3, nat, nat))

        #  Trace and its derivative
        t_call_trace = time()
        inv_d4 = np.divide(2.E0, d4, out=np.zeros_like(d4), where=d4 != 0)
        work_arr = np.zeros(shape=(3, nat, nat), dtype=np.float64)
        for iat in range(nat):
            for jat in range(0, iat):
                dx = x_val[iat]-x_val[jat]
                dy = y_val[iat]-y_val[jat]
                dz = z_val[iat]-z_val[jat]
                tt = inv_d4[iat, jat]
                work_arr[0, iat, jat] = dx*tt
                work_arr[1, iat, jat] = dy*tt
                work_arr[2, iat, jat] = dz*tt
                work_arr[0, jat, iat] = -dx*tt
                work_arr[1, jat, iat] = -dy*tt
                work_arr[2, jat, iat] = -dz*tt
        t_call_trace = time()-t_call_trace
        # contribution of off-diagonal matrix elements to derivative of eval(nat) using the Hellmann-Feynmann
        t_call_hf = time()
        for lat in range(nat):
            for iat in range(nat):
                for jat in range(nat):
                    if iat == jat:
                        continue
                    fp_der_arr[0, iat, lat] -= work_arr[0, iat, jat]*(2.E0*inv_d2[iat, lat]*inv_d2[jat, lat])
                    fp_der_arr[1, iat, lat] -= work_arr[1, iat, jat]*(2.E0*inv_d2[iat, lat]*inv_d2[jat, lat])
                    fp_der_arr[2, iat, lat] -= work_arr[2, iat, jat]*(2.E0*inv_d2[iat, lat]*inv_d2[jat, lat])
        t_call_hf = time()-t_call_hf
        # derivatives of diagonal elements from derivatives of  off-diagonal elements
        t_call_od = time()
        for jat in range(nat):
            tx = 0.E0
            ty = 0.E0
            tz = 0.E0
            for iat in range(nat):
                if iat == jat:
                    continue
                tx -= work_arr[0, iat, jat]
                ty -= work_arr[1, iat, jat]
                tz -= work_arr[2, iat, jat]
            work_arr[0, jat, jat] = tx
            work_arr[1, jat, jat] = ty
            work_arr[2, jat, jat] = tz
        t_call_od = time()-t_call_od
        # contribution of diagonal matrix elements to derivative of eval(nat) using Hellmann-Feynmann
        t_call_odhf = time()
        for lat in range(nat):
            for kat in range(nat):
                for jat in range(nat):
                    fp_der_arr[0, kat, lat] += work_arr[0, kat, jat]*inv_d2[jat, lat]**2
                    fp_der_arr[1, kat, lat] += work_arr[1, kat, jat]*inv_d2[jat, lat]**2
                    fp_der_arr[2, kat, lat] += work_arr[2, kat, jat]*inv_d2[jat, lat]**2
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
            print('DistMat: %.6f (ms)' % (t_call_dist_mat*1000.E0))
            print('EigenVal: %.6f (ms)' % (t_call_eig*1000.E0))
            print('Trace: %.6f (ms)' % (t_call_trace*1000.E0))
            print('HF: %.6f (ms)' % (t_call_hf*1000.E0))
            print('Off-diagonal: %.6f (ms)' % (t_call_od*1000.E0))
            print('Off-diagonal HF: %.6f (ms)' % (t_call_odhf*1000.E0))
        return fp_arr, fp_der_arr


def get_laplace_fingerprint_distance(src_fingerprint=None, src_struct=None, trg_struct=None, calcDer=None):


    if calcDer == True:
        fp_src_arr, fp_src_der_arr = get_laplace_fingerprint(src_struct, calcDer=calcDer)
        fp_trg_arr, fp_trg_der_arr = get_laplace_fingerprint(trg_struct, calcDer=calcDer)
        fp_dist = np.linalg.norm(fp_src_arr-fp_trg_arr)**2
        fp_dist_der=np.zeros((3,len(fp_src_arr)))
        for i in range(3):
            for j in range(len(fp_src_arr)):
                # fp_dist_der[i,j]=2.E0*np.sum((fp_src_arr-fp_trg_arr)*(fp_src_der_arr[i][j][:]-fp_trg_der_arr[i][j][:]))
                fp_dist_der[i, j] = 2.E0 * np.sum((fp_src_arr - fp_trg_arr) * (fp_src_der_arr[i][j][:] - fp_trg_der_arr[i][j][:]))
        print(np.sum(fp_dist_der[0,:]))
        print(np.sum(fp_dist_der[1,:]))
        print(np.sum(fp_dist_der[2,:]))

        delta_fp_dist = np.subtract(fp_src_arr, fp_trg_arr)
        delta_fp_der_dist = np.subtract(fp_src_der_arr, fp_trg_der_arr)
        element_wise_product = np.multiply(delta_fp_dist, delta_fp_der_dist)
        fp_dist_der2 = 2.E0*np.sum(element_wise_product, axis=2)
        for i in range(3):
            for j in range(len(fp_src_arr)):
                print(i,j,fp_dist_der2[i,j],fp_dist_der[i,j])
        return fp_dist, fp_dist_der
    elif calcDer == False:
        fp_trg_arr = get_laplace_fingerprint(trg_struct, calcDer=calcDer)
        fp_dist = np.linalg.norm(src_fingerprint-fp_trg_arr)**2
        return fp_dist


if __name__ == '__main__':
    structure = read('posinp.xyz')
    structure_Target = read('posinp.xyz')
    FP, FP_der = get_laplace_fingerprint(structure, verbose=False)
    FP_dist, FP_dist_der = get_laplace_fingerprint_distance(src_struct=structure, trg_struct=structure_Target, calcDer=True)
