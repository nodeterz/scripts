#!/bin/bash -l
#SBATCH --nodes=1
#SBATCH --job-name="Compass"
#SBATCH --time=23:50:00
#SBATCH --cpus-per-task=12
#SBATCH --ntasks-per-node=1
#SBATCH --hint=nomultithread
#SBATCH --constraint=gpu
#SBATCH --partition=normal
##SBATCH --partition=debug
#SBATCH --account=s1167
#SBATCH --output=slurm.out

# setting up environment
module purge
module load daint-gpu
module load PyTorch

export MPICH_MAX_THREAD_SAFETY=multiple
export CRAY_CUDA_MPS=0
export MKL_NUM_THREADS=$SLURM_CPUS_PER_TASK
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
###export SIRIUS_SAVE_CONFIG=all

srun python Compass.py > LOG_Compass
