#!/usr/bin/env python
import yaml
import argparse

str1 = "This script reads a list of directories in yaml format and analyzes the minhopp for them"
parser = argparse.ArgumentParser(description=str1)
parser.add_argument('dirs', action='store' ,type=str, help="The directories to be analyzed in yaml format")
parser.add_argument('mh_s', action='store' ,type=int, help="cutoff minima hopping step for analyzing")
parser.add_argument('fn_out', action='store' ,type=str, help="list of directories which have MH_steps less than cutoff mh_s")
args=parser.parse_args()

stream_in = open(args.dirs,'r')
dir_list= yaml.load(stream_in)
stream_out = open(args.fn_out,'w')
for l in dir_list:
    filename = l+'/monminhopp/monitoring.000'    
    monmh = open(filename,'r')
    good_pot = True
    first_line = monmh.readline()
    for line in monmh:
        A = line.split()
        if int(float(A[-1])) > args.mh_s:
            good_pot = False
    if good_pot:
        stream_out.write('\t'+'-'+'\t'+l+'\n')
