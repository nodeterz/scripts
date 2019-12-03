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
stream_out.write(" \t # %20s \t %8s \t %5s \t %5s \t %5s \n" % ("DIR","AVERAGE","MAX","ITER","MHS"))
for l in dir_list:
    filename = l+'/monminhopp/monitoring.000'    
    monmh = open(filename,'r')
    good_pot = True
    first_line = monmh.readline()
    B = 0.0E+00
    N = 0.0E+00
    max_val = -1.E+00
    min_num=-1
    for line in monmh:
        min_num = min_num+1
        A = line.split()
        mh_step =  int(float(A[-1]))
        B = B + mh_step
        N = N + 1.0E+00
        if mh_step > max_val:
            max_val = mh_step
            max_loc = N
        if mh_step > args.mh_s:
            good_pot = False
    if good_pot:
        average = B/N
#        stream_out.write('\t'+'-'+'\t'+l+'\t'+str(average)+'\t'+str(max_val)+'\t'+str(max_loc)+'\n')
        stream_out.write(" \t - %20s \t %5.3f \t %5d \t %5d \t %5d \n" % (l,average,max_val,max_loc,min_num))
