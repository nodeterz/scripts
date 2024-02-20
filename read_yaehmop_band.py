import numpy as np
import matplotlib.pyplot as plt
inpstream=open('mp1018088.bind.band','r')
kpts=[]
bands=[]
for iline,line in enumerate(inpstream):
    if iline == 0 or iline == 1:
        continue
    elif iline == 2:
        points_num= int(line.split()[0])
    elif iline == 3:
        continue
    elif iline == 4:
        orbs_num = int(line.split()[0])
    elif iline < 5+points_num:
        continue
    elif iline > 5+points_num:
        if line.startswith('; K point:'):
            kpts.append([float(line.split()[3]),float(line.split()[4]),float(line.split()[5])])
            bands.append([])
        else:
            try:
                bands[-1].append(float(line.split()[0]))
            except:
                print(line)
                
    
#print(np.shape(kpts))
#print(np.shape(bands))
#plt.plot(bands)
#plt.show()


        
