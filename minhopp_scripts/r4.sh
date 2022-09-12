#!/bin/sh
#SBATCH --job-name="MH_r1"
#SBATCH --exclusive=user
#SBATCH --ntasks=1
#SBATCH --nodes=1-1
#SBATCH --cpus-per-task=1
#SBATCH --qos=kernph-1week
#SBATCH --partition=phi
#SBATCH --mem-per-cpu=2800M


cd pos_28_010_001 && cp ../Run_3.sh . && Run_3.sh && cd ..
cd pos_28_010_002 && cp ../Run_3.sh . && Run_3.sh && cd ..
cd pos_28_010_003 && cp ../Run_3.sh . && Run_3.sh && cd ..
cd pos_28_020_001 && cp ../Run_3.sh . && Run_3.sh && cd ..
cd pos_28_020_002 && cp ../Run_3.sh . && Run_3.sh && cd ..
cd pos_28_020_003 && cp ../Run_3.sh . && Run_3.sh && cd ..
cd pos_28_030_001 && cp ../Run_3.sh . && Run_3.sh && cd ..
cd pos_28_030_002 && cp ../Run_3.sh . && Run_3.sh && cd ..
cd pos_28_030_003 && cp ../Run_3.sh . && Run_3.sh && cd ..
cd pos_28_050_001 && cp ../Run_3.sh . && Run_3.sh && cd ..
cd pos_28_050_002 && cp ../Run_3.sh . && Run_3.sh && cd ..
cd pos_28_050_003 && cp ../Run_3.sh . && Run_3.sh && cd ..
cd pos_28_070_001 && cp ../Run_3.sh . && Run_3.sh && cd ..
cd pos_28_070_002 && cp ../Run_3.sh . && Run_3.sh && cd ..
cd pos_28_070_003 && cp ../Run_3.sh . && Run_3.sh && cd ..
cd pos_28_090_001 && cp ../Run_3.sh . && Run_3.sh && cd ..
cd pos_28_090_002 && cp ../Run_3.sh . && Run_3.sh && cd ..
cd pos_28_090_003 && cp ../Run_3.sh . && Run_3.sh && cd ..
cd pos_37_010_001 && cp ../Run_3.sh . && Run_3.sh && cd ..
cd pos_37_010_002 && cp ../Run_3.sh . && Run_3.sh && cd ..
cd pos_37_010_003 && cp ../Run_3.sh . && Run_3.sh && cd ..
cd pos_37_020_001 && cp ../Run_3.sh . && Run_3.sh && cd ..
cd pos_37_020_002 && cp ../Run_3.sh . && Run_3.sh && cd ..
cd pos_37_020_003 && cp ../Run_3.sh . && Run_3.sh && cd ..
cd pos_37_030_001 && cp ../Run_3.sh . && Run_3.sh && cd ..
cd pos_37_030_002 && cp ../Run_3.sh . && Run_3.sh && cd ..
cd pos_37_030_003 && cp ../Run_3.sh . && Run_3.sh && cd ..
cd pos_37_050_001 && cp ../Run_3.sh . && Run_3.sh && cd ..
cd pos_37_050_002 && cp ../Run_3.sh . && Run_3.sh && cd ..
cd pos_37_050_003 && cp ../Run_3.sh . && Run_3.sh && cd ..
cd pos_37_070_001 && cp ../Run_3.sh . && Run_3.sh && cd ..
cd pos_37_070_002 && cp ../Run_3.sh . && Run_3.sh && cd ..
cd pos_37_070_003 && cp ../Run_3.sh . && Run_3.sh && cd ..
cd pos_37_090_001 && cp ../Run_3.sh . && Run_3.sh && cd ..
cd pos_37_090_002 && cp ../Run_3.sh . && Run_3.sh && cd ..
cd pos_37_090_003 && cp ../Run_3.sh . && Run_3.sh && cd ..
