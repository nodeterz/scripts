import os
import math
import ase.io
import numpy as np
from compass import Compass
from nequip.ase import NequIPCalculator

Strs=ase.io.read('SelectedStrs.extxyz',index=':')
lenStrs=len(Strs)
compassLog=open('compassLog.log','w')
formater=1+int(np.log10(lenStrs))
calculator =  NequIPCalculator.from_deployed_model(
        model_path="mymodel.pth",
        device = "cuda",
        species_to_type_name = {
            "Au": "Au",
        }
    )

try:
    logFile = open('logFile','r')
    for line in logFile:
        startStr = int(line.split()[0])
    logFile.close()
except:
    startStr = 0

logFile = open('logFile','a')
for i in range(startStr,lenStrs-1):
    logFile.write('%d\n'%i)
    logFile.flush()
    formatB='out_%'+'0'+str(formater)+'d_BB.extxyz'
    formatL='out_%'+'0'+str(formater)+'d_AL.extxyz'
    formatR='out_%'+'0'+str(formater)+'d_CR.extxyz'
    formatP='Processing: %'+'0'+str(formater)+'d/'+str(lenStrs)+'\n'
    formatC='clog_%'+'0'+str(formater)+'d'
    #compass_input = {
    #    'forcetol': 99.2,
    #    'targetdistancesaddle': 0.05,
    #    'targetdistanceother': 0.05,
    #    'energydifferencethreshold': 0.1,
    #    'trustradius': 0.01,
    #    'restart_level': 1,
    #    'basename': formatC%i
    #}
    compass_input = {
        'minimize_input': True, # Minimize start/end.
        'nsteps': 2000,#1000, # The maximal number of steps in the optimization loop.
        'nloops': 40,#20, # How many times a rearrangement of the chain should be attempted.
        'forcetol': 40.0, #0.2, # The tolerance on the residual forces.
        'forcetolperdistance': 0.2, # The tolerance on the residual forces relative to the distance.
        'distancestepmax': 0.05, # The maximum step size by which the images should approach each other relative to the current distance.
        'distancestepmin': 0.005, # The minimum step size by which the images should approach each other relative to the current distance.
        'targetdistancesaddle': 0.2, # The target distance in phase two if the forces are anti-parallel.
        'targetdistanceother': 0.2, # The target distance in phase one or when the forces are not anti-parallel.
        'energydifferencethreshold': 0.015,#0.2, # The energy difference threshold. Used to detect extrema along the path, to check the same-energy condition and to eliminate nodes with energies too close to the barrier energy.
        'nsplitdouble': 2, # How many local minima along a non-monotonous path should be used to split the segment (1 or more).
        'nsplitsingle': 1, # How many split position along a monotonous path should be used (0 or 1).
        'alpha0': 0.001, # The minimal (and initial) step size in SQNM complementary subspace (inv. max. curvature).
        'trustradius': 0.005, # Trust radius applied during projection and for the SQNM step in the unconstrained subspace (per atom).
        'trustedforcedifference': 0.5, # Maximum trusted change of the model force attributed to the distance reduction step.
        'extracurv': False, # Make the optimization more robust for small distances by adding an additional curvature term to the sqnm model.
        'saddle_cosp': 0.7, # Confirm a saddle point if the cosine of the angle between the force in the optimization manifold and the distance constraint is above this threshold.
        'nhistx': 10, # The history size of the SQNM part in COMPASS.
        'restart_level': 1,#0, # Whether to write intermediate positions as restart files: 0: None, 1: Only minimization and chain, 2: Also intermediate positions and extrema.
        'restart_interval': 10,  # At which intervals to write the current position (only with restart_level=2).
        'basename': formatC%i,#'clog_', # The filename prefix used for log and restart files (may include a path).
        'minimize_fmax': 0.001, # The maximal force on a single atom after the minimization.
        'minimize_nsteps': 2000,#500, # The maximal number of force evaluation during minimization.
        'minimize_maxrise': 0.001, # The tolerated rise of energy during minimization without resetting SQNM history.
        'parallel': False, # Whether to do an MPI parallelisation with two tasks (for the left and right image).
        'incremental_projection': True, # Whether the position and force history should be projected incrementally to the same energy surface or in a single step.
        'interpolation_idpp': False, # Whether the distance step in the unknown subspace should be performed in the IDPP direction.
        'scalar_pressure': 0.0, # The pressure (in eV/Ang^3) in case of variable cell shape systems.
    }
    atomsL=Strs[i]
    atomsR=Strs[i+1]
    atomsL.set_calculator(calculator)
    atomsR.set_calculator(calculator)
    atomsL.write(formatL%i,format='extxyz',append=False)
    atomsR.write(formatR%i,format='extxyz',append=False)
    compass = Compass(atomsL, atomsR, **compass_input)
    initial_nodes = compass.calc_initial_nodes()
    barrier, allsaddles = compass.run(initial_nodes)
    barrier.write(formatB%i,format='extxyz',append=False)
    compassLog.write(formatP%i)
    compassLog.flush()
compassLog.close()
