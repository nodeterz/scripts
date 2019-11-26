#!/usr/bin/env python
import yaml
import argparse
str1 = "This script reads input.yaml and deletes the specific structures from input file"
parser = argparse.ArgumentParser(description=str1)
parser.add_argument('fn_inp', action='store' ,type=str, help="Name of the input file in yaml format")
parser.add_argument('str_num', action='store' ,type=int, help="Name of desired conf in each file.")
args=parser.parse_args()
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader
stream=open(args.fn_inp)
dict_list = list(yaml.load_all(stream, Loader=Loader))

for count,conf in enumerate(dict_list):
    file_num = count/args.str_num
    #print(file_num)
    fn_out = "tt%5.5d.yaml"%file_num
    output_stream=open(fn_out,"a+")
    output_stream.write('---\n')
    yaml.dump(dict_list[count],output_stream)




#del_list = yaml.load(stream)
#for i,d in enumerate(del_list):
#    del_list[i]=int(d)-1
#
#conf_list=list(range(len(dict_list)))
#
#conf_keep_list=list(set(conf_list) - set(del_list))
#
#for conf in conf_keep_list:
#    output_stream.write('---\n')
#    yaml.dump(dict_list[conf],output_stream)
