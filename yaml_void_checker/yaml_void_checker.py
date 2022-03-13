#!/usr/bin/env python
import yaml
import argparse
import math
str1 = "This script reads a yaml file and checks for voids or atom seprations in free BC"
parser = argparse.ArgumentParser(description=str1)
parser.add_argument('fn_inp', action='store' ,type=str, help="Name of the input file in yaml format")
parser.add_argument('bond_length', action='store' ,type=float, help="bondlength")
parser.add_argument('fn_out', action='store' ,type=str, help="Name of the output file in yaml format")
#parser.add_argument('nx', action='store' ,type=int, help="division in x axis")
#parser.add_argument('ny', action='store' ,type=int, help="division in y axis")
#parser.add_argument('nz', action='store' ,type=int, help="division in z axis")
args=parser.parse_args()
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader
stream=open(args.fn_inp)
output_stream=open(args.fn_out,"w")
dict_list = list(yaml.load_all(stream, Loader=Loader))


for iconf,conf in enumerate(dict_list):
    minX,minY,minZ=1.E+6,1.E+6,1.E+6
    maxX,maxY,maxZ=-1.E+6,-1.E+6,-1.E+6
    for i in range(int(conf['conf']['nat'])):
        minX=min(conf['conf']['coord'][i][0],minX)
        minY=min(conf['conf']['coord'][i][1],minY)
        minZ=min(conf['conf']['coord'][i][2],minZ)
        maxX=max(conf['conf']['coord'][i][0],maxX)
        maxY=max(conf['conf']['coord'][i][1],maxY)
        maxZ=max(conf['conf']['coord'][i][2],maxZ)
    #print(minX,minY,minZ,maxX,maxY,maxZ)
    minX-=0.5E0*args.bond_length
    minY-=0.5E0*args.bond_length
    minZ-=0.5E0*args.bond_length
    maxX+=0.5E0*args.bond_length
    maxY+=0.5E0*args.bond_length
    maxZ+=0.5E0*args.bond_length
    lenX=maxX-minX
    lenY=maxY-minY
    lenZ=maxZ-minZ
    vX=2.E0*args.bond_length
    vY=lenY#3.E0*args.bond_length
    vZ=lenZ#3.E0*args.bond_length
    nx=int(lenX/vX)
    ny=1#int(lenY/vY)
    nz=1#int(lenZ/vZ)
    #vX=lenX/args.nx
    #vY=lenY/args.ny
    #vZ=lenZ/args.nz
    #minX-=vX/2
    #minY-=vY/2
    #minZ-=vZ/2
    #maxX+=vX/2
    #maxY+=vY/2
    #maxZ+=vZ/2
    #lenX=maxX-minX
    #lenY=maxY-minY
    #lenZ=maxZ-minZ
    #vX=lenX/args.nx
    #vY=lenY/args.ny
    #vZ=lenZ/args.nz
    #print('p %d found inside cube %d %d %d %f %f %f %f %f %f'%(i,sx,sy,sz,minX+sx*vx,minY+sy*vy,minZ+sz*vz,conf['conf']['coord'][i][0], conf['conf']['coord'][i][1], conf['conf']['coord'][i][2]))
    for sx in range(1,nx+1):
        for sy in range(1,ny+1):
            for sz in range(1,nz+1):
                void_found=True
                for i in range(int(conf['conf']['nat'])):
                    if(conf['conf']['coord'][i][0]<=minX+sx*vX and conf['conf']['coord'][i][0]>=minX+(sx-1)*vX and 
                       conf['conf']['coord'][i][1]<=minY+sy*vY and conf['conf']['coord'][i][1]>=minY+(sy-1)*vY and 
                       conf['conf']['coord'][i][2]<=minZ+sz*vZ and conf['conf']['coord'][i][2]>=minZ+(sz-1)*vZ):
                        void_found=False
                        break
                if(void_found):
                    print('conf= %d has void,box dims = %.2f %.2f %.2f'%(iconf+1,vX,vY,vZ))
                    break
            if(void_found):
                break
        if(void_found):
            break
    if(not void_found):
        output_stream.write('---\n')
        yaml.dump(dict_list[iconf],output_stream)
        print('conf= %d has no void'%(iconf+1))
