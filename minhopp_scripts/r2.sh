#!/bin/sh
#SBATCH --job-name="MH_r1"
#SBATCH --exclusive=user
#SBATCH --ntasks=2
#SBATCH --nodes=1-1
#SBATCH --cpus-per-task=1
#SBATCH --qos=kernph-1week
#SBATCH --partition=phi
#SBATCH --mem-per-cpu=2800M


cp Run_1.sh pos_28_010_001 && cd pos_28_010_001 && Run_1.sh && cd ..
cp Run_1.sh pos_28_010_002 && cd pos_28_010_002 && Run_1.sh && cd ..
cp Run_1.sh pos_28_010_003 && cd pos_28_010_003 && Run_1.sh && cd ..
cp Run_1.sh pos_28_020_001 && cd pos_28_020_001 && Run_1.sh && cd ..
cp Run_1.sh pos_28_020_002 && cd pos_28_020_002 && Run_1.sh && cd ..
cp Run_1.sh pos_28_020_003 && cd pos_28_020_003 && Run_1.sh && cd ..
cp Run_1.sh pos_28_030_001 && cd pos_28_030_001 && Run_1.sh && cd ..
cp Run_1.sh pos_28_030_002 && cd pos_28_030_002 && Run_1.sh && cd ..
cp Run_1.sh pos_28_030_003 && cd pos_28_030_003 && Run_1.sh && cd ..
cp Run_1.sh pos_28_050_001 && cd pos_28_050_001 && Run_1.sh && cd ..
cp Run_1.sh pos_28_050_002 && cd pos_28_050_002 && Run_1.sh && cd ..
cp Run_1.sh pos_28_050_003 && cd pos_28_050_003 && Run_1.sh && cd ..
cp Run_1.sh pos_28_070_001 && cd pos_28_070_001 && Run_1.sh && cd ..
cp Run_1.sh pos_28_070_002 && cd pos_28_070_002 && Run_1.sh && cd ..
cp Run_1.sh pos_28_070_003 && cd pos_28_070_003 && Run_1.sh && cd ..
cp Run_1.sh pos_28_090_001 && cd pos_28_090_001 && Run_1.sh && cd ..
cp Run_1.sh pos_28_090_002 && cd pos_28_090_002 && Run_1.sh && cd ..
cp Run_1.sh pos_28_090_003 && cd pos_28_090_003 && Run_1.sh && cd ..
cp Run_1.sh pos_37_010_001 && cd pos_37_010_001 && Run_1.sh && cd ..
cp Run_1.sh pos_37_010_002 && cd pos_37_010_002 && Run_1.sh && cd ..
cp Run_1.sh pos_37_010_003 && cd pos_37_010_003 && Run_1.sh && cd ..
cp Run_1.sh pos_37_020_001 && cd pos_37_020_001 && Run_1.sh && cd ..
cp Run_1.sh pos_37_020_002 && cd pos_37_020_002 && Run_1.sh && cd ..
cp Run_1.sh pos_37_020_003 && cd pos_37_020_003 && Run_1.sh && cd ..
cp Run_1.sh pos_37_030_001 && cd pos_37_030_001 && Run_1.sh && cd ..
cp Run_1.sh pos_37_030_002 && cd pos_37_030_002 && Run_1.sh && cd ..
cp Run_1.sh pos_37_030_003 && cd pos_37_030_003 && Run_1.sh && cd ..
cp Run_1.sh pos_37_050_001 && cd pos_37_050_001 && Run_1.sh && cd ..
cp Run_1.sh pos_37_050_002 && cd pos_37_050_002 && Run_1.sh && cd ..
cp Run_1.sh pos_37_050_003 && cd pos_37_050_003 && Run_1.sh && cd ..
cp Run_1.sh pos_37_070_001 && cd pos_37_070_001 && Run_1.sh && cd ..
cp Run_1.sh pos_37_070_002 && cd pos_37_070_002 && Run_1.sh && cd ..
cp Run_1.sh pos_37_070_003 && cd pos_37_070_003 && Run_1.sh && cd ..
cp Run_1.sh pos_37_090_001 && cd pos_37_090_001 && Run_1.sh && cd ..
cp Run_1.sh pos_37_090_002 && cd pos_37_090_002 && Run_1.sh && cd ..
cp Run_1.sh pos_37_090_003 && cd pos_37_090_003 && Run_1.sh && cd ..
sbatch r3.sh > sub_r3
sbatch r4.sh > sub_r4
