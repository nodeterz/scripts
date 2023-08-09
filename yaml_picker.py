#!/usr/bin/env python
import yaml
import argparse
############################################
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader
############################################

str1 = "This script reads input.yaml and pickes the specific structures from input file"
parser = argparse.ArgumentParser(description=str1)
parser.add_argument('fn_inp', action='store' ,type=str, help="Name of the input file in yaml format")
parser.add_argument('fn_out', action='store' ,type=str, help="Name of the output file in acf format")
args=parser.parse_args()

strnum_stream = open('input.yaml','r')
input_stream=open(args.fn_inp)
output_stream=open(args.fn_out,"w")

pick_list = yaml.load(strnum_stream,Loader=Loader)
str_list = list(yaml.load_all(input_stream,Loader=Loader))


for iconf, conf in enumerate(str_list):
    if(iconf+1 in pick_list):
        output_stream.write('---\n')
        yaml.dump(conf,output_stream,default_flow_style=None)
