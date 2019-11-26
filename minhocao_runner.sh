#! /bin/sh

run_arr=("run0001" "run0002")
iter_arr=("14" "15")
size_arr=("005" "010" "015" "020" "025" "030")
for run in ${run_arr[@]};
do
    for iter in ${iter_arr[@]};
    do
        for int_size in $(seq 5 5 30);
        do
            #echo $((int_size))
            Sr=$((int_size/5))
            Ti=$Sr
            O=$((Sr*3))
            size=$(printf "%03d" $int_size)
            #echo $size $int_size $Sr $Ti $O
            echo $PWD
            cp -r ./template ./STO_${run}_${iter}_${size}
            cp posout/STO_${size}.ascii STO_${run}_${iter}_${size}/poscur.ascii
            cp /data/home/ehsan/work/SrTiO3/train/cent1/980811_cluster_5_5/${run}/Sr.ann.param.yaml.000${iter} STO_${run}_${iter}_${size}/Sr.ann.param.yaml
            cp /data/home/ehsan/work/SrTiO3/train/cent1/980811_cluster_5_5/${run}/Ti.ann.param.yaml.000${iter} STO_${run}_${iter}_${size}/Ti.ann.param.yaml
            cp /data/home/ehsan/work/SrTiO3/train/cent1/980811_cluster_5_5/${run}/O.ann.param.yaml.000${iter} STO_${run}_${iter}_${size}/O.ann.param.yaml
            cd STO_${run}_${iter}_${size}
            sed -i "s/natoms/$int_size/g" flame_in.yaml
            sed -i "s/Srr/$Sr/g" flame_in.yaml
            sed -i "s/Tii/$Ti/g" flame_in.yaml
            sed -i "s/OO/$O/g" flame_in.yaml

            #sbatch run > submit
            cd ..
            #echo "cp $run STO_${iter}_${size}"
        done
    done
done
