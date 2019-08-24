#!/bin/bash
dtol=eeee
FN=5000
for j in $(seq -f "%04g" 1 $FN) ; do
    FILE=./traj_proc000_step000${j}_mde.bin
    if [ -f "$FILE" ]; then
        cd ./select_$j
        sed -i "s/dddd/$dtol/g" run_2
        #sed -i "s/all/bigmem2/g" run_2
        sbatch run_2 > submit_2 
        cd ..
    fi
done
