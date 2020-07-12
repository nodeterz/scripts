#!/usr/bin/env python
import yaml
import argparse
str1 = "This script reads a yaml file and prints cell margin distance from LR/TB/FB"
parser = argparse.ArgumentParser(description=str1)
parser.add_argument('fn_inp1', action='store' ,type=str, help="Name of the input file in yaml format")
parser.add_argument('fn_inp2', action='store' ,type=str, help="Name of the input file in yaml format")
args=parser.parse_args()
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader
stream_1=open(args.fn_inp1)
stream_2=open(args.fn_inp2)
dict_list_1 = list(yaml.load_all(stream_1, Loader=Loader))
dict_list_2 = list(yaml.load_all(stream_2, Loader=Loader))
frq_1=[]
frq_2=[]
for qp_1 in dict_list_1[0]['phonon']:
    for freq_1 in qp_1['band']:
        frq_1.append(float(freq_1['frequency']))
for qp_2 in dict_list_2[0]['phonon']:
    for freq_2 in qp_2['band']:
        frq_2.append(float(freq_2['frequency']))
rmse=0.E+00
for i in range(len(frq_1)):
    rmse=rmse+(frq_1[i]-frq_2[i])**2
rmse=rmse**0.5
print rmse
