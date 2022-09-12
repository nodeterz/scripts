#! /bin/sh
run_arr=("run00303 " "run00464 " "run00526 " "run01218 " "run01130 " "run01136 " "run00488 ")
iter_arr=("13" "14" "15")
size_arr=("016" "038" "056")
for run in ${run_arr[@]};
do
    for iter in ${iter_arr[@]};
    do
        for int_size in ${size_arr[@]};
        do
            size=$int_size
            echo $PWD
            cp -r ./template ./MgO_${run}_${iter}_${size}
            cp posout/MgO_${size}.yaml MgO_${run}_${iter}_${size}/posinp.yaml
            cp /data/home/ehsan/work/cent_2_double_Chi/MgO/980913/PY/${run}/Mg.ann.param.yaml.000${iter} MgO_${run}_${iter}_${size}/Mg.ann.param.yaml
            cp /data/home/ehsan/work/cent_2_double_Chi/MgO/980913/PY/${run}/O.ann.param.yaml.000${iter} MgO_${run}_${iter}_${size}/O.ann.param.yaml
            cd MgO_${run}_${iter}_${size}
            sbatch run > submit
            cd ..
        done
    done
done
