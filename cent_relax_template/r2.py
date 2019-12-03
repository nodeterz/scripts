#!/usr/bin/env python
import subprocess
import os
import math
import time
#*****************************************************************************************
subprocess.call(["mkdir","Results"])
nrun=31
nstr=10
os.system("clear")
sorter=open("r3.sh",'w')
for irun in range(0,nrun):
    os.system("grep epot run%4.4d/GEOPT_S???/posout.yaml | sort -nr -k4 > ./Results/epot_run%4.4d"%(irun,irun))
    os.system("grep nat run%4.4d/GEOPT_S???/posout.yaml | sort -nr -k4 > ./Results/nat_run%4.4d"%(irun,irun))
    epot_file=open("./Results/epot_run%4.4d"%irun,'r')
    nat_file=open("./Results/nat_run%4.4d"%irun,'r')
    out=open("./Results/run%4.4d"%irun,'w')
    sorter.write("sort -k3gr Results/run%4.4d > Results/temp && cat Results/temp >  Results/run%4.4d\n"%(irun,irun))
    for istr in range(1,nstr+1):
        epot_line=epot_file.readline()
        epot=float(epot_line.rsplit()[-1])
        nat_line=nat_file.readline()
        nat=float(nat_line.rsplit()[-1])
        out.write("run%4.4d/GEOPT_S%3.3d/posout.yaml: \t epot: \t %7.4f \n"%(irun,istr,epot/nat))
        #print epot/nat
        os.system("clear")
        percentage = 100.E0*irun/nrun
        print "Getting info is %3.3d%% done." % (percentage)
    out.close()
sorter.close()
