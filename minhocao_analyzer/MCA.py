#!/usr/bin/env python
import yaml
import argparse
import os

str1 = "This script reads a list of directories in yaml format and analyzes the minhopp for them"
parser = argparse.ArgumentParser(description=str1)
parser.add_argument('dirs', action='store' ,type=str, help="The directories to be analyzed in yaml format")
parser.add_argument('mc_s', action='store' ,type=int, help="cutoff minima hopping step for analyzing")
parser.add_argument('fn_out', action='store' ,type=str, help="list of directories which have MC_steps less than cutoff mc_s")
args=parser.parse_args()
stream_in = open(args.dirs,'r')
dir_list= yaml.load(stream_in)
stream_out = open(args.fn_out,'w')
for l in dir_list:
    os.system("echo "+ l)
    flamelog=l+'/flame_log.yaml'
    if os.path.isfile(flamelog):
        mca_in=l+'/MCA_IN'
        gp_cmd = "grep 'FIRE converged:' " + flamelog + ' > ' + mca_in
        sed_cmd = "sed -i 's/,/ /g' " + mca_in
        os.system(gp_cmd)
        os.system(sed_cmd)
        mca = open(mca_in,'r')
        good_pot = True
        B = 0.0E+00
        N = 0.0E+00
        max_val = -1.E+00
        for line in mca :
            A = line.split()
            mc_step =  int(float(A[3]))
            B = B + mc_step
            N = N + 1.0E+00
            if mc_step > max_val:
                max_val = mc_step
                max_loc = N
            if mc_step > args.mc_s:
                good_pot = False
        if good_pot:
            average = B/N
            #stream_out.write('\t'+'-'+'\t'+l+'\t'+str(average)+'\t\t'+str(max_val)+'\t\t'+str(max_loc)+'\n')
            stream_out.write(" \t - %s \t %5.3f \t %5d \t %5d \n" % (l,average,max_val,max_loc))
    else:
        print flamelog+' not found.'
