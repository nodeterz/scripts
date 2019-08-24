#!/bin/bash
FN=5000
rm -rf all_selected.yaml
touch all_selected.yaml
for j in $(seq -f "%04g" 1 $FN) ; do
    FILE=./traj_proc000_step000${j}_mde.bin
    if [ -f "$FILE" ]; then
        cd ./select_$j
        python $PYTHONPATH/bin2yaml.py ./all.bin ./all.yaml
        cd ..
        echo $j
    #    sleep 5s
    fi
done
for j in $(seq -f "%04g" 1 $FN) ; do
    FILE=./traj_proc000_step000${j}_mde.bin
    if [ -f "$FILE" ]; then
        cd ./select_$j
        cat all.yaml >> ../all_selected.yaml
        cd ..
        echo $j
    fi
done
