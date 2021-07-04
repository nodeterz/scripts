#!/usr/bin/env python
import yaml
import argparse
str1 = "This script reads input.yaml and deletes the specific structures from input file"
parser = argparse.ArgumentParser(description=str1)
parser.add_argument('fn_inp_ref', action='store' ,type=str, help="Name of the reference input file in yaml format")
parser.add_argument('fn_inp_cent', action='store' ,type=str, help="Name of the cent2 SP input file in yaml format")
parser.add_argument('fn_SP_short', action='store' ,type=str, help="Name of the short range output file in yaml format")
args=parser.parse_args()
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader
stream_ref=open(args.fn_inp_ref)
dict_list_ref = list(yaml.load_all(stream_ref, Loader=Loader))
stream_cent=open(args.fn_inp_cent)
dict_list_cent = list(yaml.load_all(stream_cent, Loader=Loader))
dict_list_short=dict_list_ref

dict_list_short[0]['conf']['epot']-=dict_list_cent[0]['conf']['epot']

for i in range(dict_list_ref[0]['conf']['nat']):
    dict_list_short[0]['conf']['force'][i][0]-=dict_list_cent[0]['conf']['force'][i][0]
    dict_list_short[0]['conf']['force'][i][1]-=dict_list_cent[0]['conf']['force'][i][1]
    dict_list_short[0]['conf']['force'][i][2]-=dict_list_cent[0]['conf']['force'][i][2]

output_stream=open(args.fn_SP_short,"w")
output_stream.write('---\n')
yaml.dump(dict_list_short,output_stream,default_flow_style=None)
