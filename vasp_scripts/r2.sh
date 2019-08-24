#!/bin/bash
FN=5000
rm -rf final.yaml
for j in $(seq -f "%05g" 1 $FN) ; do
    dir=${j}
    if [ -d "$dir" ]; then
        echo "$dir exist"
        cd $dir
        vasp_xml2yaml.py vasprun.xml posout.yaml
        cat posout.yaml >> ../final.yaml
        cd ..
    else
        echo "ERROR : $dir does not exist."
    fi
done

