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
xat_He=0.E+0
yat_He=0.E+0
zat_He=0.E+0
He=False
xat_Ne=0.E+0
yat_Ne=0.E+0
zat_Ne=0.E+0
Ne=False
xat_Ar=0.E+0
yat_Ar=0.E+0
zat_Ar=0.E+0
Ar=False
xat_Kr=0.E+0
yat_Kr=0.E+0
zat_Kr=0.E+0
Kr=False
xat_Xe=0.E+0
yat_Xe=0.E+0
zat_Xe=0.E+0
Xe=False
xat_Rn=0.E+0
yat_Rn=0.E+0
zat_Rn=0.E+0
Rn=False
xat_Lu=0.E+0
yat_Lu=0.E+0
zat_Lu=0.E+0
Lu=False
xat_Lr=0.E+0
yat_Lr=0.E+0
zat_Lr=0.E+0
Lr=False
for i in range(int(dict_list[0]['conf']['nat'])):
    #print dict_list[0]['conf']['coord'][i][3].strip()
    if dict_list[0]['conf']['coord'][i][3].strip()=='He':
        He=True
        if dict_list[0]['conf']['coord'][i][0] > (dict_list[0]['conf']['cell'][0][0]):
            dict_list[0]['conf']['coord'][i][0]=dict_list[0]['conf']['coord'][i][0]-dict_list[0]['conf']['cell'][0][0]
        if dict_list[0]['conf']['coord'][i][1] > (dict_list[0]['conf']['cell'][1][1]):
            dict_list[0]['conf']['coord'][i][1]=dict_list[0]['conf']['coord'][i][1]-dict_list[0]['conf']['cell'][1][1]
        if dict_list[0]['conf']['coord'][i][2] > (dict_list[0]['conf']['cell'][2][2]):
            dict_list[0]['conf']['coord'][i][2]=dict_list[0]['conf']['coord'][i][2]-dict_list[0]['conf']['cell'][2][2]
        xat_He=xat_He+dict_list[0]['conf']['coord'][i][0]
        yat_He=yat_He+dict_list[0]['conf']['coord'][i][1]
        zat_He=zat_He+dict_list[0]['conf']['coord'][i][2]
    elif dict_list[0]['conf']['coord'][i][3].strip()=='Ne':
        if dict_list[0]['conf']['coord'][i][0] > (dict_list[0]['conf']['cell'][0][0]):
            dict_list[0]['conf']['coord'][i][0]=dict_list[0]['conf']['coord'][i][0]-dict_list[0]['conf']['cell'][0][0]
        if dict_list[0]['conf']['coord'][i][1] > (dict_list[0]['conf']['cell'][1][1]):
            dict_list[0]['conf']['coord'][i][1]=dict_list[0]['conf']['coord'][i][1]-dict_list[0]['conf']['cell'][1][1]
        if dict_list[0]['conf']['coord'][i][2] > (dict_list[0]['conf']['cell'][2][2]):
            dict_list[0]['conf']['coord'][i][2]=dict_list[0]['conf']['coord'][i][2]-dict_list[0]['conf']['cell'][2][2]
        Ne=True
        xat_Ne=xat_Ne+dict_list[0]['conf']['coord'][i][0]
        yat_Ne=yat_Ne+dict_list[0]['conf']['coord'][i][1]
        zat_Ne=zat_Ne+dict_list[0]['conf']['coord'][i][2]
    elif dict_list[0]['conf']['coord'][i][3].strip()=='Ar':
        if dict_list[0]['conf']['coord'][i][0] > (dict_list[0]['conf']['cell'][0][0]):
            dict_list[0]['conf']['coord'][i][0]=dict_list[0]['conf']['coord'][i][0]-dict_list[0]['conf']['cell'][0][0]
        if dict_list[0]['conf']['coord'][i][1] > (dict_list[0]['conf']['cell'][1][1]):
            dict_list[0]['conf']['coord'][i][1]=dict_list[0]['conf']['coord'][i][1]-dict_list[0]['conf']['cell'][1][1]
        if dict_list[0]['conf']['coord'][i][2] > (dict_list[0]['conf']['cell'][2][2]):
            dict_list[0]['conf']['coord'][i][2]=dict_list[0]['conf']['coord'][i][2]-dict_list[0]['conf']['cell'][2][2]
        Ar=True
        xat_Ar=xat_Ar+dict_list[0]['conf']['coord'][i][0]
        yat_Ar=yat_Ar+dict_list[0]['conf']['coord'][i][1]
        zat_Ar=zat_Ar+dict_list[0]['conf']['coord'][i][2]
    elif dict_list[0]['conf']['coord'][i][3].strip()=='Kr':
        if dict_list[0]['conf']['coord'][i][0] > (dict_list[0]['conf']['cell'][0][0]):
            dict_list[0]['conf']['coord'][i][0]=dict_list[0]['conf']['coord'][i][0]-dict_list[0]['conf']['cell'][0][0]
        if dict_list[0]['conf']['coord'][i][1] > (dict_list[0]['conf']['cell'][1][1]):
            dict_list[0]['conf']['coord'][i][1]=dict_list[0]['conf']['coord'][i][1]-dict_list[0]['conf']['cell'][1][1]
        if dict_list[0]['conf']['coord'][i][2] > (dict_list[0]['conf']['cell'][2][2]):
            dict_list[0]['conf']['coord'][i][2]=dict_list[0]['conf']['coord'][i][2]-dict_list[0]['conf']['cell'][2][2]
        Kr=True
        xat_Kr=xat_Kr+dict_list[0]['conf']['coord'][i][0]
        yat_Kr=yat_Kr+dict_list[0]['conf']['coord'][i][1]
        zat_Kr=zat_Kr+dict_list[0]['conf']['coord'][i][2]
    elif dict_list[0]['conf']['coord'][i][3].strip()=='Xe':
        if dict_list[0]['conf']['coord'][i][0] > (dict_list[0]['conf']['cell'][0][0]):
            dict_list[0]['conf']['coord'][i][0]=dict_list[0]['conf']['coord'][i][0]-dict_list[0]['conf']['cell'][0][0]
        if dict_list[0]['conf']['coord'][i][1] > (dict_list[0]['conf']['cell'][1][1]):
            dict_list[0]['conf']['coord'][i][1]=dict_list[0]['conf']['coord'][i][1]-dict_list[0]['conf']['cell'][1][1]
        if dict_list[0]['conf']['coord'][i][2] > (dict_list[0]['conf']['cell'][2][2]):
            dict_list[0]['conf']['coord'][i][2]=dict_list[0]['conf']['coord'][i][2]-dict_list[0]['conf']['cell'][2][2]
        Xe=True
        xat_Xe=xat_Xe+dict_list[0]['conf']['coord'][i][0]
        yat_Xe=yat_Xe+dict_list[0]['conf']['coord'][i][1]
        zat_Xe=zat_Xe+dict_list[0]['conf']['coord'][i][2]
    elif dict_list[0]['conf']['coord'][i][3].strip()=='Rn':
        if dict_list[0]['conf']['coord'][i][0] > (dict_list[0]['conf']['cell'][0][0]):
            dict_list[0]['conf']['coord'][i][0]=dict_list[0]['conf']['coord'][i][0]-dict_list[0]['conf']['cell'][0][0]
        if dict_list[0]['conf']['coord'][i][1] > (dict_list[0]['conf']['cell'][1][1]):
            dict_list[0]['conf']['coord'][i][1]=dict_list[0]['conf']['coord'][i][1]-dict_list[0]['conf']['cell'][1][1]
        if dict_list[0]['conf']['coord'][i][2] > (dict_list[0]['conf']['cell'][2][2]):
            dict_list[0]['conf']['coord'][i][2]=dict_list[0]['conf']['coord'][i][2]-dict_list[0]['conf']['cell'][2][2]
        Rn=True
        xat_Rn=xat_Rn+dict_list[0]['conf']['coord'][i][0]
        yat_Rn=yat_Rn+dict_list[0]['conf']['coord'][i][1]
        zat_Rn=zat_Rn+dict_list[0]['conf']['coord'][i][2]
    elif dict_list[0]['conf']['coord'][i][3].strip()=='Lu':
        if dict_list[0]['conf']['coord'][i][0] > (dict_list[0]['conf']['cell'][0][0]):
            dict_list[0]['conf']['coord'][i][0]=dict_list[0]['conf']['coord'][i][0]-dict_list[0]['conf']['cell'][0][0]
        if dict_list[0]['conf']['coord'][i][1] > (dict_list[0]['conf']['cell'][1][1]):
            dict_list[0]['conf']['coord'][i][1]=dict_list[0]['conf']['coord'][i][1]-dict_list[0]['conf']['cell'][1][1]
        if dict_list[0]['conf']['coord'][i][2] > (dict_list[0]['conf']['cell'][2][2]):
            dict_list[0]['conf']['coord'][i][2]=dict_list[0]['conf']['coord'][i][2]-dict_list[0]['conf']['cell'][2][2]
        Lu=True
        xat_Lu=xat_Lu+dict_list[0]['conf']['coord'][i][0]
        yat_Lu=yat_Lu+dict_list[0]['conf']['coord'][i][1]
        zat_Lu=zat_Lu+dict_list[0]['conf']['coord'][i][2]
    elif dict_list[0]['conf']['coord'][i][3].strip()=='Lr':
        if dict_list[0]['conf']['coord'][i][0] > (dict_list[0]['conf']['cell'][0][0]):
            dict_list[0]['conf']['coord'][i][0]=dict_list[0]['conf']['coord'][i][0]-dict_list[0]['conf']['cell'][0][0]
        if dict_list[0]['conf']['coord'][i][1] > (dict_list[0]['conf']['cell'][1][1]):
            dict_list[0]['conf']['coord'][i][1]=dict_list[0]['conf']['coord'][i][1]-dict_list[0]['conf']['cell'][1][1]
        if dict_list[0]['conf']['coord'][i][2] > (dict_list[0]['conf']['cell'][2][2]):
            dict_list[0]['conf']['coord'][i][2]=dict_list[0]['conf']['coord'][i][2]-dict_list[0]['conf']['cell'][2][2]
        Lr=True
        xat_Lr=xat_Lr+dict_list[0]['conf']['coord'][i][0]
        yat_Lr=yat_Lr+dict_list[0]['conf']['coord'][i][1]
        zat_Lr=zat_Lr+dict_list[0]['conf']['coord'][i][2]
if(He):
    dict_list[0]['conf']['coord'].append([])
    dict_list[0]['conf']['coord'][-1]=([xat_He/2.E0,yat_He/2.E0,zat_He/2.E0,'Sr','TTT'])
#    print dict_list[0]['conf']['coord'][-1]
if(Ne):
    dict_list[0]['conf']['coord'].append([])
    dict_list[0]['conf']['coord'][-1]=([xat_Ne/2.E0,yat_Ne/2.E0,zat_Ne/2.E0,'Sr','TTT'])
#    print dict_list[0]['conf']['coord'][-1]
if(Ar):
    dict_list[0]['conf']['coord'].append([])
    dict_list[0]['conf']['coord'][-1]=([xat_Ar/2.E0,yat_Ar/2.E0,zat_Ar/2.E0,'Sr','TTT'])
#    print dict_list[0]['conf']['coord'][-1]
if(Kr):
    dict_list[0]['conf']['coord'].append([])
    dict_list[0]['conf']['coord'][-1]=([xat_Kr/2.E0,yat_Kr/2.E0,zat_Kr/2.E0,'Sr','TTT'])
#    print dict_list[0]['conf']['coord'][-1]
if(Xe):
    dict_list[0]['conf']['coord'].append([])
    dict_list[0]['conf']['coord'][-1]=([xat_Xe/2.E0,yat_Xe/2.E0,zat_Xe/2.E0,'Sr','TTT'])
#    print dict_list[0]['conf']['coord'][-1]
if(Rn):
    dict_list[0]['conf']['coord'].append([])
    dict_list[0]['conf']['coord'][-1]=([xat_Rn/2.E0,yat_Rn/2.E0,zat_Rn/2.E0,'Sr','TTT'])
#    print dict_list[0]['conf']['coord'][-1]
if(Lu):
    dict_list[0]['conf']['coord'].append([])
    dict_list[0]['conf']['coord'][-1]=([xat_Lu/2.E0,yat_Lu/2.E0,zat_Lu/2.E0,'Sr','TTT'])
#    print dict_list[0]['conf']['coord'][-1]
if(Lr):
    dict_list[0]['conf']['coord'].append([])
    dict_list[0]['conf']['coord'][-1]=([xat_Lr/2.E0,yat_Lr/2.E0,zat_Lr/2.E0,'Sr','TTT'])
#    print dict_list[0]['conf']['coord'][-1]
final_dict= {'conf':{'coord':[]}}
final_dict['conf']=dict_list[0]['conf'].copy()
final_dict['conf']['coord']=[]
nat=0
for atoms in dict_list[0]['conf']['coord']:
    if atoms[3].strip()=='I':
        nat=nat+1
        final_dict['conf']['coord'].append([])
        final_dict['conf']['coord'][-1]=([atoms[0],atoms[1],atoms[2],'O',atoms[4]])
    elif atoms[3].strip()=='Pb':
        nat=nat+1
        final_dict['conf']['coord'].append([])
        final_dict['conf']['coord'][-1]=([atoms[0],atoms[1],atoms[2],'Ti',atoms[4]])
    elif atoms[3].strip()=='Sr':
        nat=nat+1
        final_dict['conf']['coord'].append([])
        final_dict['conf']['coord'][-1]=([atoms[0],atoms[1],atoms[2],'Sr',atoms[4]])
final_dict['conf']['nat']=nat
stream_out.write('---\n')
yaml.dump(final_dict,stream_out,default_flow_style=None)
