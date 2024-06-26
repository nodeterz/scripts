import sys
import numpy as np
from ase.io import read,write
from tqdm import tqdm

def calculate_angle(vec1, vec2):
    """Calculate the angle in degrees between two vectors."""
    unit_vec1 = vec1 / np.linalg.norm(vec1)
    unit_vec2 = vec2 / np.linalg.norm(vec2)
    dot_product = np.dot(unit_vec1, unit_vec2)
    angle = np.arccos(np.clip(dot_product, -1.0, 1.0))
    return np.degrees(angle)

inpFileName=sys.argv[1]
outFileName=sys.argv[2]


inpStrs=read(inpFileName,index=':')

for struct in tqdm(inpStrs):
    cell_vectors = struct.cell
    # Calculate angles between the cell vectors
    alpha = calculate_angle(cell_vectors[1], cell_vectors[2])
    beta = calculate_angle(cell_vectors[0], cell_vectors[2])
    gamma = calculate_angle(cell_vectors[0], cell_vectors[1]) 
    if(alpha<75 or alpha>105 or beta<75 or beta>105 or  gamma<75 or gamma>105):
        continue
    else:
        struct.write(outFileName,format='extxyz',append=True)
