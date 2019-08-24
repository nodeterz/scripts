#!/bin/sh
#SBATCH --job-name="vasp"
#SBATCH --exclusive=user
#SBATCH --ntasks=16
#SBATCH --nodes=1-1
#SBATCH --cpus-per-task=1
#SBATCH --qos=kernph-1week
#SBATCH --partition=psi
#SBATCH --mem-per-cpu=1700M

cp -r ../../template_Au/ 01651 && cd 01651  && cp ../data/tt01651 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01652 && cd 01652  && cp ../data/tt01652 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01653 && cd 01653  && cp ../data/tt01653 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01654 && cd 01654  && cp ../data/tt01654 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01655 && cd 01655  && cp ../data/tt01655 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01656 && cd 01656  && cp ../data/tt01656 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01657 && cd 01657  && cp ../data/tt01657 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01658 && cd 01658  && cp ../data/tt01658 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01659 && cd 01659  && cp ../data/tt01659 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01660 && cd 01660  && cp ../data/tt01660 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01661 && cd 01661  && cp ../data/tt01661 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01662 && cd 01662  && cp ../data/tt01662 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01663 && cd 01663  && cp ../data/tt01663 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01664 && cd 01664  && cp ../data/tt01664 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01665 && cd 01665  && cp ../data/tt01665 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01666 && cd 01666  && cp ../data/tt01666 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01667 && cd 01667  && cp ../data/tt01667 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01668 && cd 01668  && cp ../data/tt01668 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01669 && cd 01669  && cp ../data/tt01669 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01670 && cd 01670  && cp ../data/tt01670 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01671 && cd 01671  && cp ../data/tt01671 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01672 && cd 01672  && cp ../data/tt01672 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01673 && cd 01673  && cp ../data/tt01673 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01674 && cd 01674  && cp ../data/tt01674 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01675 && cd 01675  && cp ../data/tt01675 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01676 && cd 01676  && cp ../data/tt01676 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01677 && cd 01677  && cp ../data/tt01677 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01678 && cd 01678  && cp ../data/tt01678 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
