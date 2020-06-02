#!/usr/bin/env python
import yaml
import argparse
import os
str1 = "This is a script for checking dpm_rmse for flame dpm outputs." 
parser = argparse.ArgumentParser(description=str1)
parser.add_argument('fn_inp', action='store' ,type=str, help="Name of the input file in yaml format")
parser.add_argument('sed', action='store', nargs='?' ,type=str, help="write SED if you want to run sedding.")
args=parser.parse_args()
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader
if (args.sed=='SED'):
    sed_spc='sed -i "s/       /    /g" '+args.fn_inp
    sed_dpm='sed -i "s/dpm/- dpm/g" '+ args.fn_inp
    sed_nat='sed -i "s/nat/- nat/g" '+ args.fn_inp
    os.system(sed_spc)
    os.system(sed_dpm)
    os.system(sed_nat)
stream=open(args.fn_inp)
dict_list = list(yaml.load_all(stream, Loader=Loader))
rmse=0.E+00
count=0
for i in range(len(dict_list)):
    dpx_dft =float(dict_list[i]['conf'][2]['dpm(dft )'].split()[0])
    dpx_cent=float(dict_list[i]['conf'][1]['dpm(cent)'].split()[0])
    dpy_dft =float(dict_list[i]['conf'][2]['dpm(dft )'].split()[1])
    dpy_cent=float(dict_list[i]['conf'][1]['dpm(cent)'].split()[1])
    dpz_dft =float(dict_list[i]['conf'][2]['dpm(dft )'].split()[2])
    dpz_cent=float(dict_list[i]['conf'][1]['dpm(cent)'].split()[2])
    if ((dpx_dft!=0) and (dpy_dft!=0) and (dpz_dft!=0)):
        count=count+1
        rmse = rmse+(dpx_dft-dpx_cent)**2+(dpy_dft-dpy_cent)**2+(dpz_dft-dpz_cent)**2
rmse = rmse/(3.0*count)
rmse = rmse**(0.5)
print ("Dipole moment RMSE is : %8.3f"%rmse)
