#!/usr/bin/env python
import yaml
import argparse
import numpy as np


def angle(v1, v2):
    return np.arccos(np.inner(v1,v2)/(np.linalg.norm(v1)*np.linalg.norm(v2)))*180.0/np.pi
def volume(v1, v2, v3):
    return np.inner(np.cross(v1,v2),v3)
def ratio(v1, v2):
    return np.linalg.norm(v1)/np.linalg.norm(v2)


str1 = "This script reads a yaml file and prints cell margin distance from LR/TB/FB"
parser = argparse.ArgumentParser(description=str1)
parser.add_argument('fn_inp', action='store' ,type=str, help="Name of the input file in yaml format")
args=parser.parse_args()
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader
stream=open(args.fn_inp)
dict_list = list(yaml.load_all(stream, Loader=Loader))
v1 = [0, 0 ,0]
v2 = [0, 0 ,0]
v3 = [0, 0 ,0]
print 'iconf','\t', 'angle(v1,v2)','\t', 'angle(v2,v3)','\t', 'angle(v1,v3)','\t', 'volume(v1, v2, v3)','\t','ratio(v1, v2)','\t','ratio(v1,v3)','\t','ratio(v2,v3)','\t','nat','\t','V/nat'
for iconf,conf in enumerate(dict_list):
    v1[0]=conf['conf']['cell'][0][0]
    v1[1]=conf['conf']['cell'][0][1]
    v1[2]=conf['conf']['cell'][0][2]
    v2[0]=conf['conf']['cell'][1][0]
    v2[1]=conf['conf']['cell'][1][1]
    v2[2]=conf['conf']['cell'][1][2]
    v3[0]=conf['conf']['cell'][2][0]
    v3[1]=conf['conf']['cell'][2][1]
    v3[2]=conf['conf']['cell'][2][2]
    nat=conf['conf']['nat']
    print("%5d \t %10.3f \t %10.3f \t %10.3f \t %10.3f \t %10.3f \t %10.3f \t %10.3f \t %i \t %10.3f" %(iconf+1, angle(v1,v2), angle(v2,v3), angle(v1,v3), volume(v1, v2, v3),ratio(v1, v2),ratio(v1,v3),ratio(v2,v3),nat,volume(v1, v2, v3)/nat))
