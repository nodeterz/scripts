import numpy as np
from ase.io import read
import matplotlib.pyplot as plt
import matplotlib.colors as cls
import matplotlib.gridspec as gs
import sys
from sys import getsizeof
import argparse

Values=["HFPEtot", "HFPEH", "HFPXC", "HFPEVXC", "HFPEION", "HFPEBS", "HFPQ", "VNPEtot", "VNPEH", "VNPXC", "VNPEVXC", "VNPEION", "VNPEBS", "VNPQ"]
FPS=["ACSF", "OMFP", "SOMFP", "TOMFP", "TBQ", "TBEBS"]

str1 = "This script epot per atom of all the structures in the input file."
parser = argparse.ArgumentParser(description=str1)
parser.add_argument('ival', action='store' ,type=int, help="Value Element Number. Range= 0:%d"%(len(Values)-1))
parser.add_argument('ifp', action='store' ,type=int, help="FP Element Number. Range= 0:%d"%(len(FPS)-1))
args=parser.parse_args()
#sys.stdout=open('log_Plot.stdout','a')
#sys.stderr=open('log_Plot.stderr','a')

structures = read('posoutAllFpNoNan.extxyz', ':')

#desCoeffs={'ACSF': 71.65429302, 'OMFP': 3.10608381, 'SOMFP': 19.93236403, 'TOMFP': 33.84008823, 'TBQ': 0.96173867, 'TBEBS': 32.72190277} #MAX Element
desCoeffs={'ACSF': 146.20540101469416, 'OMFP': 4.394228114945839, 'SOMFP': 132.8807825288577, 'TOMFP': 255.98889873160925, 'TBQ': 1.2756892564780629, 'TBEBS': 47.499115278840975} #Max Norm



cMap='jet'

desRange=1.E0 
desBin=10000
desX=desRange/desBin
desArr=np.linspace(0,desRange,num=desBin)

valRange=10.0
valBin=10000
valX=valRange/valBin
valArr=np.linspace(0,valRange,num=valBin)

Value=Values[args.ival]
FP1=FPS[args.ifp]

print('Processing: ', Value,FP1)
fpd=np.zeros((valBin,desBin),dtype=int)
maxVal=0.E0
maxDes=0.E0
for istr,i_structure in enumerate(structures):
    i_descriptors=np.divide(i_structure.get_array(FP1),desCoeffs[FP1])
    i_vals=i_structure.get_array(Value)
    #try:  #For when having TBQ and TBEBS in Value Arrays
    #    i_vals=np.sum(i_structure.get_array(Value),axis=1)
    #except:
    #    i_vals=i_structure.get_array(Value)
    for jstr,j_structure in enumerate(structures):
        if(jstr<istr):
            continue
        j_descriptors=np.divide(j_structure.get_array(FP1),desCoeffs[FP1])
        try:
            j_vals=np.sum(j_structure.get_array(Value),axis=1)
        except:
            j_vals=j_structure.get_array(Value)
        if (istr==jstr):
            for iat in range(i_structure.get_global_number_of_atoms()):
                for jat in range(iat+1,j_structure.get_global_number_of_atoms()):
                    try:
                        ival=abs(np.subtract(i_vals[iat],j_vals[jat]))
                        ides=np.linalg.norm(i_descriptors[iat]-j_descriptors[jat])
                        fpd[int(ival/valX),int(ides/desX)] += 1
                        maxVal=max(maxVal,ival) # Has to be here to account for Accepted Values
                        maxDes=max(maxDes,ides) # Has to be here to account for Accepted Values
                    except:
                        pass
                       # if (int(abs(np.subtract(i_vals[iat],j_vals[jat]))/valX) > valBin-1) and (int(np.linalg.norm(i_descriptors[iat]-j_descriptors[jat])/desX) > desBin-1):
                       #     fpd[valBin-1,desBin-1] += 1
                       # elif (int(abs(np.subtract(i_vals[iat],j_vals[jat]))/valX) > valBin-1):
                       #     fpd[valBin-1,int(np.linalg.norm(i_descriptors[iat]-j_descriptors[jat])/desX)] += 1
                       # elif (int(np.linalg.norm(i_descriptors[iat]-j_descriptors[jat])/desX) > desBin-1):
                       #     fpd[int(abs(np.subtract(i_vals[iat],j_vals[jat]))/valX),desBin-1] += 1
        else:
            for iat in range(i_structure.get_global_number_of_atoms()):
                for jat in range(j_structure.get_global_number_of_atoms()):
                    try:
                        ival=abs(np.subtract(i_vals[iat],j_vals[jat]))
                        ides=np.linalg.norm(i_descriptors[iat]-j_descriptors[jat])
                        fpd[int(ival/valX),int(ides/desX)] += 1
                        maxVal=max(maxVal,ival) # Has to be here to account for Accepted Values
                        maxDes=max(maxDes,ides) # Has to be here to account for Accepted Values
                    except:
                        pass
                        #if (int(abs(np.subtract(i_vals[iat],j_vals[jat]))/valX) > valBin-1) and (int(np.linalg.norm(i_descriptors[iat]-j_descriptors[jat])/desX) > desBin-1):
                        #    fpd[valBin-1,desBin-1] += 1
                        #elif (int(abs(np.subtract(i_vals[iat],j_vals[jat]))/valX) > valBin-1):
                        #    fpd[valBin-1,int(np.linalg.norm(i_descriptors[iat]-j_descriptors[jat])/desX)] += 1
                        #elif (int(np.linalg.norm(i_descriptors[iat]-j_descriptors[jat])/desX) > desBin-1):
                        #    fpd[int(abs(np.subtract(i_vals[iat],j_vals[jat]))/valX),desBin-1] += 1
fig, ax = plt.subplots(nrows=1,ncols=1,figsize=(10,10))
#im=ax.imshow(fpd,extent=[0,int(maxDes/desX),0,int(maxVal/valX)],cmap='jet',origin='lower',vmin=1,aspect='auto')
print(int(maxVal/valX),int(maxDes/desX))
im=ax.imshow(fpd[0:int(maxVal/valX),0:int(maxDes/desX)],cmap='jet',origin='lower',vmin=1,aspect='auto')
ax.set(xlabel='%s'%(FP1),ylabel='%s'%(Value))
fig.colorbar(im,ax=ax)
fig.savefig('%s_%s.png'%(Value,FP1),dpi=400,bbox_inches='tight')
plt.close(fig)
