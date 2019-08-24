#!/bin/bash
FN=5000
for j in $(seq -f "%04g" 1 $FN) ; do
    FILE=./traj_proc000_step000${j}_mde.bin
    if [ -f "$FILE" ]; then
       # echo "$FILE exist"
        mkdir select_$j
        cp ./traj_proc000_step000${j}_mde.bin ./select_$j/poslow.bin
        cp /kernph/ghasemi/ehsan/work/Au/minhopp/batch_2/pick_diff_template/* ./select_$j
        cd ./select_$j
        sbatch run > submit
        cd ..
    fi
done
