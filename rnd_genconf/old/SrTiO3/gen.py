#!/usr/bin/env python
import random
import math
str_num = 5
kat = 6
nat = 5*kat
dmin = 3
#cv1=8
#cv2=8
#cv3=8

v_per_atom = dmin**3
#cell_vol = (cv1-2*dmin)*(cv2-2*dmin)*(cv3-2*dmin)
cvs = float(int((1.1*nat*v_per_atom)**(1./3.))+1)
cvs += 2*dmin
cv1 = cvs
cv2 = cvs
cv3 = cvs
#if (cell_vol/(nat*v_per_atom))<1.1:
#    print('Cell is not large enough\n')
#    print('suggested cv is : %4.4f\n'% (cvs))
#    exit()
for i in range(str_num):
    str_name = 'posout_'+"%3.3d" % (nat)+'_'+"%3.3d" % (i)+'.ascii'
    output = open(str_name,'w')
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
    for iat in range(len(xat)):
        if iat < kat :
            output.write("%14.6f \t %14.6f \t %14.6f \t %s \n" %(xat[iat],yat[iat],zat[iat],'Sr'))
        elif iat < 2*kat :
            output.write("%14.6f \t %14.6f \t %14.6f \t %s \n" %(xat[iat],yat[iat],zat[iat],'Ti'))
        else :
            output.write("%14.6f \t %14.6f \t %14.6f \t %s \n" %(xat[iat],yat[iat],zat[iat],'O'))


