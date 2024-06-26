import ase.io
from nequip.ase import NequIPCalculator
from ase.mep import NEB
from ase.optimize import BFGS
import sys

# Read structures
num=int(sys.argv[1])
structure_AL = ase.io.read('out_%d_AL.extxyz'%num)
structure_BB = ase.io.read('out_%d_BB.extxyz'%num)
structure_CR = ase.io.read('out_%d_CR.extxyz'%num)


# Function to perform NEB calculation
def perform_neb(start, end, images_count, prefix):
    calculator=NequIPCalculator.from_deployed_model(
        model_path="mymodel.pth",
        device="cuda",
        species_to_type_name={
            "Au": "Au",
        }
    )
    # Create images for NEB
    images = [start] + [start.copy() for _ in range(images_count)] + [end]
    neb = NEB(images,allow_shared_calculator=True)
    neb.interpolate()
    
    # Attach the calculator to each image
    for image in images:
        image.calc=calculator
    
    # Optimize the path using BFGS
    optimizer = BFGS(neb, trajectory=f'{prefix}_neb.traj')
    optimizer.run(fmax=0.005)
    
    # Save the NEB images
    for i, image in enumerate(images):
        ase.io.write(f'{prefix}_{i:02d}.extxyz', image)

# Perform NEB from BB to AL
perform_neb(structure_BB, structure_AL, images_count=20, prefix='toLeft')

# Perform NEB from BB to CR
perform_neb(structure_BB, structure_CR, images_count=20, prefix='toRight')

