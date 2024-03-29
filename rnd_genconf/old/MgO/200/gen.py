#!/usr/bin/env python
import random
import math
def gen_conf(i):
    output = open('pos_out_%.3d.ascii'%i,'w')
    nat = 200
    dmin = 2.1
    cv1=28
    cv2=28
    cv3=8
    v_per_atom = dmin**3
    cell_vol = (cv1-2*dmin)*(cv2-2*dmin)*(cv3-2*dmin)
    
    if (cell_vol/(nat*v_per_atom))<1.1:
        exit('Cell size = %d is not large enough, must be larger that %d'%(cell_vol,v_per_atom*nat*1.1E0))
    xat=[]
    yat=[]
    zat=[]
    iat=0
    while(iat < nat):
        accepted = True
        x1 = random.random()*(cv1-dmin)
        y1 = random.random()*(cv2-dmin)
        z1 = random.random()*(cv3-dmin)
        if (iat==0) :
            xat.append(x1)
            yat.append(y1)
            zat.append(z1)
            iat += 1
        else :
            for jat in range(len(xat)):
                dr = (xat[jat]-x1)**2+(yat[jat]-y1)**2+(zat[jat]-z1)**2
                dr = math.sqrt(dr)
                if dr < dmin :
                    accepted = False
                    break
            if accepted :
                xat.append(x1)
                yat.append(y1)
                zat.append(z1)
                iat += 1
    output.write(str(nat)+'\n')
    output.write("%14.6f \t %14.6f \t %14.6f \n" %(cv1,0.,cv2))
    output.write("%14.6f \t %14.6f \t %14.6f \n" %(0.,0.,cv3))
    atoms_sat=['Mg','O']
    for iat in range(len(xat)):
        output.write("%14.6f \t %14.6f \t %14.6f \t %s \n" %(xat[iat],yat[iat],zat[iat],atoms_sat[iat%2]))
for i in range(100):
    gen_conf(i)
