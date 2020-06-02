#!/usr/bin/env python
import yaml
import argparse
str1 = "This script reads input and seprates fake potentials from normal ones."
parser = argparse.ArgumentParser(description=str1)
parser.add_argument('fn_inp', action='store' ,type=str, help="Name of the input file in yaml format")
args=parser.parse_args()
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader
stream=open(args.fn_inp)
dict_list = list(yaml.load_all(stream, Loader=Loader))
normal='out_normal.yaml'
fake='out_fake.yaml'
output_normal=open(normal,"w")
output_fake=open(fake,"w")
fake=0
normal=0
for conf in dict_list:
    if ('fpotgw' in conf['conf'] != 0):
        output_fake.write('---\n')
        yaml.dump(conf,output_fake,default_flow_style=None)
        fake=fake+1
    else:
        output_normal.write('---\n')
        yaml.dump(conf,output_normal,default_flow_style=None)
        normal=normal+1
print 'normal strs :',normal 
print 'fake strs :',fake
