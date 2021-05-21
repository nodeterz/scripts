#!/usr/bin/python

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

stream_in=open(args.fn_inp,'r')
stream_out = open(args.fn_out,'w')

dict_list = list(yaml.load_all(stream_in, Loader=Loader))

#print dict_list[0][0]
stream_out.write("t_id\trmse\tfrmse\tO_Qvar\tO_Qmin\tO_Qmax\tMg_Qvar\t Mg_Qmin\tMg_Qmax\tO_Cvar\tO_Cmin\tO_Cmax\tMg_Cvar\tMg_Cmin\tMg_Cmax\n")
for item in dict_list:
    print item[0]['id']
    t_id= item[0]['id']
    rmse= item[0]['train']['rmse']
    frmse= item[0]['train']['frmse']
    O_Qvar = item[0]['charge_O']['qvar']
    O_Qmin = item[0]['charge_O']['qmin']
    O_Qmax = item[0]['charge_O']['qmax']
    Mg_Qvar = item[0]['charge_Mg']['qvar']
    Mg_Qmin = item[0]['charge_Mg']['qmin']
    Mg_Qmax = item[0]['charge_Mg']['qmax']
    O_Cvar = item[0]['chi_O']['chivar']
    O_Cmin = item[0]['chi_O']['chimin']
    O_Cmax = item[0]['chi_O']['chimax']
    Mg_Cvar = item[0]['chi_Mg']['chivar']
    Mg_Cmin = item[0]['chi_Mg']['chimin']
    Mg_Cmax = item[0]['chi_Mg']['chimax']
    stream_out.write("%s|\t%11.3f|\t%11.3f|\t%11.3f|\t%11.3f\t%11.3f|\t%11.3f|\t%11.3f|\t%11.3f|\t%11.3f|\t%11.3f|\t%11.3f|\t%11.3f|\t%11.3f|\t%11.3f \n" %(t_id,rmse,frmse,O_Qvar,O_Qmin,O_Qmax,Mg_Qvar, Mg_Qmin, Mg_Qmax, O_Cvar , O_Cmin , O_Cmax , Mg_Cvar, Mg_Cmin, Mg_Cmax))
     
