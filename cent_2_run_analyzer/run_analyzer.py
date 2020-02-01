#!/usr/bin/env python
import yaml
import argparse

str1 = "This scripts prints rmse frmse qvar chivar and etc. of trains directory listed in input.yaml"
parser = argparse.ArgumentParser(description=str1)
parser.add_argument('itr', action='store' ,type=int, help="iteration number")
parser.add_argument('fn_out', action='store' ,type=str, help="Name of the output file")
args=parser.parse_args()

stream = open('input.yaml','r')
outstream = open(args.fn_out,'w')
head_line=("iter : %5.5d\n")%args.itr
outstream.write(head_line)
head_line="#   DIR      |  rmse     |  frmse    |  qvar_Mg  |  qvar_O   | chivar_Mg | chivar_O  |  gw_Mg_1  |  gw_Mg_2  |  gw_O_1   |  gw_O_2   |  J_1_Mg   |  J_2_Mg   |  J_1_O    |  J_2_O    | chi_0_Mg  |  chi_0_O  | chi_1_Mg  | chi_1_O   |  errmax   | eref_Mg       |  eref_O  |\n"
outstream.write(head_line)
head_line="#    1       |    3      |    5      |      7    |    9      |     11    |    13     |     15    |     17    |    19     |    21     |    23     |    25     |    27     |    29     |     31    |     33    |    35     |    37     |    39     |      41       |    43    |\n"
outstream.write(head_line)
head_line="#------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|---------------|----------|\n"
outstream.write(head_line)
dir_list=yaml.load(stream)
for wd in dir_list:

    stream2=open(wd+'/train_output.yaml','r')
    train = yaml.load(stream2)
    rmse=train['training iterations'][args.itr]['train']['rmse']
    frmse=train['training iterations'][args.itr]['train']['frmse']
    qvar_Mg=train['training iterations'][args.itr]['charge_Mg']['qvar']
    qvar_O=train['training iterations'][args.itr]['charge_O']['qvar']
    chivar_Mg=train['training iterations'][args.itr]['chi_Mg']['chi_2_var']
    chivar_O=train['training iterations'][args.itr]['chi_O']['chi_2_var']
    errmax=train['training iterations'][args.itr]['train']['errmax']
    
    stream3=open(wd+'/Mg.ann.input.yaml','r')
    Mg_NN = yaml.load(stream3)
    gw_Mg_1=Mg_NN['main']['gausswidth_1']
    gw_Mg_2=Mg_NN['main']['gausswidth_2']
    chi_0_Mg=Mg_NN['main']['chi0']
    chi_1_Mg=Mg_NN['main']['chi1']
    J_1_Mg=Mg_NN['main']['hardness_1']
    J_2_Mg=Mg_NN['main']['hardness_2']
    eref_Mg=Mg_NN['main']['ener_ref']

    stream4=open(wd+'/O.ann.input.yaml','r')
    O_NN = yaml.load(stream4)
    gw_O_1=O_NN['main']['gausswidth_1']
    gw_O_2=O_NN['main']['gausswidth_2']
    chi_0_O=O_NN['main']['chi0']
    chi_1_O=O_NN['main']['chi1']
    J_1_O=O_NN['main']['hardness_1']
    J_2_O=O_NN['main']['hardness_2']
    eref_O=O_NN['main']['ener_ref']
    pformat="%s"+21* " \t | %6.3f"+"\t|\n"
    #print pformat
    outstream.write(pformat%(wd,rmse,frmse,qvar_Mg,qvar_O,chivar_Mg,chivar_O,gw_Mg_1,gw_Mg_2,gw_O_1,gw_O_2,J_1_Mg,J_2_Mg,J_1_O,J_2_O,chi_0_Mg,chi_0_O,chi_1_Mg,chi_1_O,errmax,eref_Mg,eref_O))
    stream2.close()

outstream.close()
