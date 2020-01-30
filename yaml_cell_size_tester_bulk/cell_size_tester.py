#!/usr/bin/env python
import yaml
import argparse
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

for iconf,conf in enumerate(dict_list):
    ttx_min = 1.E+24
    tty_min = 1.E+24
    ttz_min = 1.E+24
    ttx_max = -1.E+24
    tty_max = -1.E+24
    ttz_max = -1.E+24
    for i in range(int(conf['conf']['nat'])):
        if conf['conf']['coord'][i][0]<ttx_min:
            ttx_min = conf['conf']['coord'][i][0]
        if conf['conf']['coord'][i][1]<tty_min:
            tty_min = conf['conf']['coord'][i][1]
        if conf['conf']['coord'][i][2]<ttz_min:
            ttz_min = conf['conf']['coord'][i][2]
        
        if conf['conf']['coord'][i][0]>ttx_max:
            ttx_max = conf['conf']['coord'][i][0]
        if conf['conf']['coord'][i][1]>tty_max:
            tty_max = conf['conf']['coord'][i][1]
        if conf['conf']['coord'][i][2]>ttz_max:
            ttz_max = conf['conf']['coord'][i][2]
    #print conf[>'conf']['nat']
    fmt="%5d"+3*"\t %10.6f"
    #cell_x = (conf['conf']['cell'][0][0]**2+conf['conf']['cell'][0][1]**2+conf['conf']['cell'][0][2]**2)**0.5
    #cell_y = (conf['conf']['cell'][1][0]**2+conf['conf']['cell'][1][1]**2+conf['conf']['cell'][1][2]**2)**0.5
    #cell_z = (conf['conf']['cell'][2][0]**2+conf['conf']['cell'][2][1]**2+conf['conf']['cell'][2][2]**2)**0.5
    cell_x = abs(conf['conf']['cell'][0][0])
    cell_y = abs(conf['conf']['cell'][1][1])
    cell_z = abs(conf['conf']['cell'][2][2])
    conf_x = abs(ttx_min-ttx_max)
    conf_y = abs(tty_min-tty_max)
    conf_z = abs(ttz_min-ttz_max)
    print (fmt%(iconf+1,cell_x/conf_x,cell_y/conf_y,cell_z/conf_z))
    #print ttx_max, tty_max, ttz_max
