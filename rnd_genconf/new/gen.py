#!/usr/bin/env python
import random
import math

global STR_NUM, sat, typat, units, dmin, cvx, cvy, cvz

STR_NUM=100 # Number of structures to be produced
sat = ['Li','Ti','O'] # Atoms type
typat=[4,5,12] # Number of each atom in order
units=10  # Number of molecules 
dmin = 2.1 # Minimum Distance between atoms
cvx=5 # Box X dimension ratio
cvy=3 # Box Y dimension ratio
cvz=1 # Box Z dimension ratio

#################################################################################
def gen_conf(i,list_sat):
    global STR_NUM, sat, typat, units, dmin, cvx, cvy, cvz
    nat=sum(typat)*units
    output = open('pos_out_%06d.ascii'%(i+1),'w')
    cube_len=0.5*dmin/math.sqrt(3)
    v_per_atom = cube_len**3
    coeff = float(nat)/float(cvx*cvy*cvz)
    cv1=coeff*cube_len*cvx#+1.0*dmin
    cv2=coeff*cube_len*cvy#+1.0*dmin
    cv3=coeff*cube_len*cvz#+1.0*dmin
    #cell_vol = (cv1-2.0*dmin)*(cv2-2.0*dmin)*(cv3-2.0*dmin)
    #print(cv1,cv2,cv3,nat,cell_vol,nat*v_per_atom) 
    #if (cell_vol/(nat*v_per_atom))<1.1:
    #    exit('Cell is not large enough')
    xat=[]
    yat=[]
    zat=[]
    iat=0
    while(iat < nat):
        accepted = True
        x1 = random.random()*(cv1-2.0*dmin)
        y1 = random.random()*(cv2-2.0*dmin)
        z1 = random.random()*(cv3-2.0*dmin)
        if (iat==0) :
            xat.append(x1)
            yat.append(y1)
            zat.append(z1)
            iat += 1
        else :
            for jat in range(len(xat)):
                dr = (xat[jat]-x1)**2+(yat[jat]-y1)**2+(zat[jat]-z1)**2
                dr = math.sqrt(dr)
                if dr < dmin:
                    accepted = False
                    break
            if accepted :
                #print(iat,cv1,cv2,cv3)
                xat.append(x1)
                yat.append(y1)
                zat.append(z1)
                iat += 1
    output.write(str(nat)+'\n')
    output.write("%14.6f \t %14.6f \t %14.6f \n" %(cv1,0.,cv2))
    output.write("%14.6f \t %14.6f \t %14.6f \n" %(0.,0.,cv3))
    for iat in range(len(xat)):
        output.write("%14.6f \t %14.6f \t %14.6f \t %s \n" %(xat[iat],yat[iat],zat[iat],list_sat[iat]))
#################################################################################
list_sat=[]
for iat,i in enumerate(sat):
#    print(iat,i)
    tmp=[i]
    list_sat+=tmp*typat[iat]*units
random.shuffle(list_sat)
for i in range(STR_NUM):
    gen_conf(i,list_sat)
    print ('STR %d out of %d generated'%(i+1,STR_NUM))
