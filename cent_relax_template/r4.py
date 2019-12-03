#!/usr/bin/env python
import subprocess
import os
import math
import time
import re
#*****************************************************************************************
os.chdir("Results")
nrun = 31
nstr= 10
l_str = [0,0,0,0,0,0,0,0,0,0]
l_ref = [1,2,3,4,5,6,7,8,9,10]
#l_ref = [9, 10, 4, 5, 8, 1, 7, 6, 2, 3]
for irun in range(0,nrun):
    f = open ("run%4.4d"%irun,"r")
    a = f.read()
    m = re.findall('GEOPT_S\d+',a)
    for istr in range(0,nstr):
        tmp=re.findall('\d+',m[istr])
        #print(tmp[0])
        l_str[istr]=int(tmp[0])
    print(irun)
    print(l_str)
    print(l_ref)
    if l_str==l_ref:
        print('TRUE')
    else:
        print('FALSE')
#*****************************************************************************************
