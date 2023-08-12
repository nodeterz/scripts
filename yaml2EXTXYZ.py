#!/usr/bin/env python
import argparse
import yaml
import os
from tqdm import tqdm

str1 = "This script read a file in the yaml dictionary format and write it in the extended XYZ format."
parser = argparse.ArgumentParser(description=str1)
parser.add_argument('fn_inp', action='store' ,type=str, help="Name of the input file in yaml format")
parser.add_argument('fn_out', action='store' ,type=str, help="Name of the output file")
args=parser.parse_args()

def readYamlStruct(dir, inputFile, outputFile):
    try:
        from yaml import CLoader as Loader
    except ImportError:
        from yaml import Loader
    stream = open(os.path.join(dir, inputFile), "r")
    dict_list = list(yaml.load_all(stream, Loader=Loader))
    outStream = open(os.path.join(dir, outputFile), 'w')
    for strnum in tqdm(range(len(dict_list)),bar_format='{l_bar}{bar:100}{r_bar}{bar:-10b}'):
        outStream.write("%d\n" % dict_list[strnum]['conf']['nat'])
        s = 'Lattice="'
        for i in range(3):
            for j in range(3):
                s += "%14.8f " % (dict_list[strnum]['conf']['cell'][i][j])
        # s += '" Properties=species:S:1:pos:R:3:forces:R:3:charges:R:1 energy=%f pbc="F F F"\n' % dict_list[strnum]['conf']['epot']
        s += '" Properties=species:S:1:pos:R:3:forces:R:3 energy=%f pbc="F F F"\n' % dict_list[strnum]['conf']['epot']
        outStream.write(s)
        for iat in range(dict_list[strnum]['conf']['nat']):
            c = "%3s " % dict_list[strnum]['conf']['coord'][iat][3]
            for i in range(3):  # X Y Z
                c += "%14.8f " % (dict_list[strnum]['conf']['coord'][iat][i])
            for i in range(3):  # FX FY FZ
                c += "%14.8f " % (dict_list[strnum]['conf']['force'][iat][i])
            c += "\n"
            outStream.write(c)
    outStream.close()


readYamlStruct('.',args.fn_inp,args.fn_out)
