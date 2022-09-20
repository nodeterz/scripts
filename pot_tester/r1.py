#!/usr/bin/python3
import os
import shutil
import argparse
import yaml
from yaml import Loader
from pathlib import Path

str1 = "This script reads address from address.yaml and gets the epoch number to run CENT1 SP"
parser = argparse.ArgumentParser(description=str1)
parser.add_argument('fn_inp', action='store' ,type=str, help="address file name in YAML format")
parser.add_argument('epoch', action='store' ,type=int, help="epoch number")
args=parser.parse_args()

stream_in=open(args.fn_inp, "r")
dict_list = list(yaml.load_all(stream_in, Loader=Loader))

strs_list=[]
i=0
#strs_list=list(os.walk(dict_list[0]['structures'][0]))

for path in Path(dict_list[0]['structures'][0]).rglob('*.yaml'):
        strs_list.append(path.name)

runs_list=[]
runs_name=[]
for run in (dict_list[0]['runs']):
    runs_list.append(os.path.join(dict_list[0]['runs_add'][0],run))
    runs_name.append(run)

for irun,run in enumerate(runs_list):
    os.system('mkdir %s'%runs_name[irun])
    inp=open('inprun','r')
    out=open('f'+runs_name[irun],'w')
    for lines in inp:
        out.write(lines)
    for istr,structs in enumerate(strs_list):
        cur_add=runs_name[irun]+'_'+structs.split('.')[0]
        cur_add=os.path.join(runs_name[irun],cur_add)
        print(cur_add)
        shutil.copytree('./template',cur_add)
        shutil.copy(os.path.join(dict_list[0]['structures'][0],structs),os.path.join(cur_add,'posinp.yaml'))
        shutil.copy(os.path.join(run,'Mg.ann.param.yaml.%05d'%args.epoch),os.path.join(cur_add,'Mg.ann.param.yaml'))
        shutil.copy(os.path.join(run,'O.ann.param.yaml.%05d'%args.epoch),os.path.join(cur_add,'O.ann.param.yaml'))
        out.write('cd '+cur_add+' && ~/Programs/FLAME.AGH-Orig-lammps-libmode/src/flame && cd ../..\n')
    out.close()
    inp.close()
