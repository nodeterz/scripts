#!/usr/bin/env python
import subprocess
import os
import math
import time
#*****************************************************************************************
trg=os.getcwd()
src="/data/home/ehsan/work/SrTiO3/train/cent1/980901_mix_5_5/"
src_run="/data/home/ehsan/work/SrTiO3/cent_relax/template"
src_struct="/data/home/ehsan/work/SrTiO3/cent_relax/STRUCTURES"
nrun=31
nstr=10
iepoch=13
for irun in range(0,nrun):
    subprocess.call(["mkdir","run%4.4d" % (irun)])
    os.chdir("./run%4.4d" % (irun))
    for istr in range(1,nstr+1):
        subprocess.call(["cp","-r",src_run,"./GEOPT_S%3.3d" % (istr)])
        os.chdir("GEOPT_S%3.3d" % (istr))
        src_o=  src+"run%4.4d/O.ann.param.yaml.%5.5d"% (irun,iepoch)
        trg_o=  "./O.ann.param.yaml" 
        src_sr=  src+"run%4.4d/Sr.ann.param.yaml.%5.5d"% (irun,iepoch)
        trg_sr=  "./Sr.ann.param.yaml" 
        src_ti=  src+"run%4.4d/Ti.ann.param.yaml.%5.5d"% (irun,iepoch)
        trg_ti=  "./Ti.ann.param.yaml" 
        subprocess.call(["cp",src_o,trg_o])
        subprocess.call(["cp",src_sr,trg_sr])
        subprocess.call(["cp",src_ti,trg_ti])
        subprocess.call(["cp",src_struct+"/%2.2d.ascii"%(istr),"./poscur.ascii"])
        #subprocess.call(["ls"])

        poscur=open('poscur.ascii','r')
        nat=int(poscur.readline())
        sed_str='s/natoms/'+str(nat)+'/g'
        subprocess.call(["sed","-i",sed_str,"./flame_in.yaml"])
        Sr_at=nat/5
        sed_str='s/Srr/'+str(Sr_at)+'/g'
        subprocess.call(["sed","-i",sed_str,"./flame_in.yaml"])
        Ti_at=nat/5
        sed_str='s/Tii/'+str(Ti_at)+'/g'
        subprocess.call(["sed","-i",sed_str,"./flame_in.yaml"])
        O_at=3*(nat/5)
        sed_str='s/OO/'+str(O_at)+'/g'
        subprocess.call(["sed","-i",sed_str,"./flame_in.yaml"])

        os.chdir("..")
    subprocess.call(["pwd"])
    subprocess.call(["cp","../run_main","run"])
    outfile=open('SUBMIT',"w")
    subprocess.call(["sbatch","run"],stdout=outfile)
    outfile.close()
    os.chdir("..")
#*****************************************************************************************
