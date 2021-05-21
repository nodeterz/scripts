#!/usr/bin/env python
import yaml
import argparse

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


str1 = "This script replaces epot with its equivalent after scf calculations"
parser = argparse.ArgumentParser(description=str1)
parser.add_argument('scf_in', action='store' ,type=float, help="screening factor")
parser.add_argument('list_in', action='store' ,type=str, help="screening factor")
args=parser.parse_args()
scf=args.scf_in

ener_stream=open(args.list_in,'r')
ener_stream_SRS=open('ehartree_scn_excl.yaml','r')
ener_list_dict=list(yaml.load(ener_stream,Loader=Loader))
ener_list_dict_srs=list(yaml.load(ener_stream_SRS,Loader=Loader))
home_add='/home/ehsan/works/cent2_SCF/data/trial_data/out_gaussian/'
def diverse_atom_select(conf,sat):
    xat=[]
    yat=[]
    zat=[]
    for i in range(conf[0]['conf']['nat']):
        xat.append(conf[0]['conf']['coord'][i][0])
        yat.append(conf[0]['conf']['coord'][i][1])
        zat.append(conf[0]['conf']['coord'][i][2])
    x_cm=sum(xat)/len(xat)
    y_cm=sum(yat)/len(yat)
    z_cm=sum(zat)/len(zat)
    r=-10000.E0
    r_cm=10000.E0
    for i in range(len(xat)):
        if(conf[0]['conf']['coord'][i][3]==sat):
            dr=((xat[i]-x_cm)**2+(yat[i]-y_cm)**2+(zat[i]-z_cm)**2)**0.5E0
            if(dr>r):
                r=dr
                at_furth=i
            if(dr<r_cm):
                r_cm=dr
                at_center=i
    r=-10000.E0
    for i in range(len(xat)):
        if(conf[0]['conf']['coord'][i][3]==sat):
            dr=((xat[i]-xat[at_furth])**2+(yat[i]-yat[at_furth])**2+(zat[i]-zat[at_furth])**2)**0.5E0
            if(dr>r):
                r=dr
                at_furth_2=i
    return at_furth+1,at_furth_2+1,at_center+1

for strs in ener_list_dict:
    if (strs[6]==scf):
        inp_add=home_add+strs[0]+'/'+strs[0]+'.yaml'
        out_add=home_add+strs[0]+'/out_'+str(scf)+'_'+strs[0]+'_'+'%03d'%strs[1]+'.yaml'
        inp_stream=open(inp_add,'r')
        conf=list(yaml.load_all(inp_stream,Loader=Loader))
        s1,s2,s3=diverse_atom_select(conf,'Mg')
        s4,s5,s6=diverse_atom_select(conf,'O')
        if(strs[1]==s1 or strs[1]==s2 or strs[1]==s3 or strs[1]==s4 or strs[1]==s5 or strs[1]==s6):
            print(inp_add)
            out_stream=open(out_add,'w')
            conf[0]['conf']['epot']=strs[5]
            conf[0]['conf']['ntrial']=1
            conf[0]['conf']['trial_ref_energy']=[[]]
            conf[0]['conf']['trial_ref_energy'][0]=[0,0,0,0,0]
            conf[0]['conf']['trial_ref_energy'][0][0]=strs[1]
            conf[0]['conf']['trial_ref_energy'][0][1]=strs[2]
            conf[0]['conf']['trial_ref_energy'][0][2]=strs[3]
            conf[0]['conf']['trial_ref_energy'][0][3]=strs[4]
            conf[0]['conf']['trial_ref_energy'][0][4]=next((sub[1] for sub in ener_list_dict_srs if (sub[0]==strs[0] and sub[2]==strs[6])),None)
            out_stream.write('---\n')
            yaml.dump(conf[0],out_stream,default_flow_style=None)
