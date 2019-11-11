#!/usr/bin/env python

import yaml
import argparse


try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

str1 = "This script epot per atom of all the structures in the input file."
parser = argparse.ArgumentParser(description=str1)
parser.add_argument('fn_inp', action='store' ,type=str, help="input file name in YAML format")
parser.add_argument('fn_out', action='store' ,type=str, help="list of epot/atom for structures")
args=parser.parse_args()

stream_in=open(args.fn_inp, "r")
dict_list = list(yaml.load_all(stream_in, Loader=Loader))

stream_out=open(args.fn_out, "w")

for i in range(len(dict_list)):
    epot = float(dict_list[i]['conf']['epot'])*27.211385e+00
    nat = float(dict_list[i]['conf']['nat'])
    stream_out.write("%5.5d \t %14.6f \t %5.5d \t %14.6f \n" %(i+1,epot,nat,epot/nat))
