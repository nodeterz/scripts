#!/bin/sh
#SBATCH --job-name="vasp"
#SBATCH --exclusive=user
#SBATCH --ntasks=16
#SBATCH --nodes=1-1
#SBATCH --cpus-per-task=1
#SBATCH --qos=kernph-1week
#SBATCH --partition=psi
#SBATCH --mem-per-cpu=1700M

cp -r ../../template_Au/ 01501 && cd 01501  && cp ../data/tt01501 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01502 && cd 01502  && cp ../data/tt01502 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01503 && cd 01503  && cp ../data/tt01503 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01504 && cd 01504  && cp ../data/tt01504 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01505 && cd 01505  && cp ../data/tt01505 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01506 && cd 01506  && cp ../data/tt01506 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01507 && cd 01507  && cp ../data/tt01507 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01508 && cd 01508  && cp ../data/tt01508 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01509 && cd 01509  && cp ../data/tt01509 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01510 && cd 01510  && cp ../data/tt01510 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01511 && cd 01511  && cp ../data/tt01511 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01512 && cd 01512  && cp ../data/tt01512 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01513 && cd 01513  && cp ../data/tt01513 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01514 && cd 01514  && cp ../data/tt01514 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01515 && cd 01515  && cp ../data/tt01515 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01516 && cd 01516  && cp ../data/tt01516 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01517 && cd 01517  && cp ../data/tt01517 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01518 && cd 01518  && cp ../data/tt01518 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01519 && cd 01519  && cp ../data/tt01519 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01520 && cd 01520  && cp ../data/tt01520 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01521 && cd 01521  && cp ../data/tt01521 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01522 && cd 01522  && cp ../data/tt01522 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01523 && cd 01523  && cp ../data/tt01523 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01524 && cd 01524  && cp ../data/tt01524 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01525 && cd 01525  && cp ../data/tt01525 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01526 && cd 01526  && cp ../data/tt01526 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01527 && cd 01527  && cp ../data/tt01527 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01528 && cd 01528  && cp ../data/tt01528 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01529 && cd 01529  && cp ../data/tt01529 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01530 && cd 01530  && cp ../data/tt01530 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01531 && cd 01531  && cp ../data/tt01531 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01532 && cd 01532  && cp ../data/tt01532 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01533 && cd 01533  && cp ../data/tt01533 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01534 && cd 01534  && cp ../data/tt01534 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01535 && cd 01535  && cp ../data/tt01535 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01536 && cd 01536  && cp ../data/tt01536 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01537 && cd 01537  && cp ../data/tt01537 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01538 && cd 01538  && cp ../data/tt01538 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01539 && cd 01539  && cp ../data/tt01539 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01540 && cd 01540  && cp ../data/tt01540 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01541 && cd 01541  && cp ../data/tt01541 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01542 && cd 01542  && cp ../data/tt01542 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01543 && cd 01543  && cp ../data/tt01543 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01544 && cd 01544  && cp ../data/tt01544 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01545 && cd 01545  && cp ../data/tt01545 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01546 && cd 01546  && cp ../data/tt01546 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01547 && cd 01547  && cp ../data/tt01547 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01548 && cd 01548  && cp ../data/tt01548 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01549 && cd 01549  && cp ../data/tt01549 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01550 && cd 01550  && cp ../data/tt01550 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01551 && cd 01551  && cp ../data/tt01551 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01552 && cd 01552  && cp ../data/tt01552 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01553 && cd 01553  && cp ../data/tt01553 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01554 && cd 01554  && cp ../data/tt01554 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01555 && cd 01555  && cp ../data/tt01555 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01556 && cd 01556  && cp ../data/tt01556 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01557 && cd 01557  && cp ../data/tt01557 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01558 && cd 01558  && cp ../data/tt01558 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01559 && cd 01559  && cp ../data/tt01559 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01560 && cd 01560  && cp ../data/tt01560 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01561 && cd 01561  && cp ../data/tt01561 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01562 && cd 01562  && cp ../data/tt01562 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01563 && cd 01563  && cp ../data/tt01563 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01564 && cd 01564  && cp ../data/tt01564 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01565 && cd 01565  && cp ../data/tt01565 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01566 && cd 01566  && cp ../data/tt01566 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01567 && cd 01567  && cp ../data/tt01567 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01568 && cd 01568  && cp ../data/tt01568 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01569 && cd 01569  && cp ../data/tt01569 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01570 && cd 01570  && cp ../data/tt01570 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01571 && cd 01571  && cp ../data/tt01571 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01572 && cd 01572  && cp ../data/tt01572 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01573 && cd 01573  && cp ../data/tt01573 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01574 && cd 01574  && cp ../data/tt01574 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01575 && cd 01575  && cp ../data/tt01575 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01576 && cd 01576  && cp ../data/tt01576 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01577 && cd 01577  && cp ../data/tt01577 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01578 && cd 01578  && cp ../data/tt01578 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01579 && cd 01579  && cp ../data/tt01579 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01580 && cd 01580  && cp ../data/tt01580 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01581 && cd 01581  && cp ../data/tt01581 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01582 && cd 01582  && cp ../data/tt01582 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01583 && cd 01583  && cp ../data/tt01583 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01584 && cd 01584  && cp ../data/tt01584 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01585 && cd 01585  && cp ../data/tt01585 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01586 && cd 01586  && cp ../data/tt01586 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01587 && cd 01587  && cp ../data/tt01587 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01588 && cd 01588  && cp ../data/tt01588 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01589 && cd 01589  && cp ../data/tt01589 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01590 && cd 01590  && cp ../data/tt01590 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01591 && cd 01591  && cp ../data/tt01591 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01592 && cd 01592  && cp ../data/tt01592 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01593 && cd 01593  && cp ../data/tt01593 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01594 && cd 01594  && cp ../data/tt01594 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01595 && cd 01595  && cp ../data/tt01595 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01596 && cd 01596  && cp ../data/tt01596 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01597 && cd 01597  && cp ../data/tt01597 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01598 && cd 01598  && cp ../data/tt01598 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01599 && cd 01599  && cp ../data/tt01599 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01600 && cd 01600  && cp ../data/tt01600 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01601 && cd 01601  && cp ../data/tt01601 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01602 && cd 01602  && cp ../data/tt01602 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01603 && cd 01603  && cp ../data/tt01603 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01604 && cd 01604  && cp ../data/tt01604 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01605 && cd 01605  && cp ../data/tt01605 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01606 && cd 01606  && cp ../data/tt01606 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01607 && cd 01607  && cp ../data/tt01607 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01608 && cd 01608  && cp ../data/tt01608 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01609 && cd 01609  && cp ../data/tt01609 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01610 && cd 01610  && cp ../data/tt01610 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01611 && cd 01611  && cp ../data/tt01611 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01612 && cd 01612  && cp ../data/tt01612 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01613 && cd 01613  && cp ../data/tt01613 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01614 && cd 01614  && cp ../data/tt01614 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01615 && cd 01615  && cp ../data/tt01615 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01616 && cd 01616  && cp ../data/tt01616 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01617 && cd 01617  && cp ../data/tt01617 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01618 && cd 01618  && cp ../data/tt01618 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01619 && cd 01619  && cp ../data/tt01619 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01620 && cd 01620  && cp ../data/tt01620 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01621 && cd 01621  && cp ../data/tt01621 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01622 && cd 01622  && cp ../data/tt01622 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01623 && cd 01623  && cp ../data/tt01623 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01624 && cd 01624  && cp ../data/tt01624 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01625 && cd 01625  && cp ../data/tt01625 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01626 && cd 01626  && cp ../data/tt01626 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01627 && cd 01627  && cp ../data/tt01627 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01628 && cd 01628  && cp ../data/tt01628 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01629 && cd 01629  && cp ../data/tt01629 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01630 && cd 01630  && cp ../data/tt01630 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01631 && cd 01631  && cp ../data/tt01631 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01632 && cd 01632  && cp ../data/tt01632 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01633 && cd 01633  && cp ../data/tt01633 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01634 && cd 01634  && cp ../data/tt01634 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01635 && cd 01635  && cp ../data/tt01635 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01636 && cd 01636  && cp ../data/tt01636 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01637 && cd 01637  && cp ../data/tt01637 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01638 && cd 01638  && cp ../data/tt01638 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01639 && cd 01639  && cp ../data/tt01639 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01640 && cd 01640  && cp ../data/tt01640 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01641 && cd 01641  && cp ../data/tt01641 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01642 && cd 01642  && cp ../data/tt01642 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01643 && cd 01643  && cp ../data/tt01643 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01644 && cd 01644  && cp ../data/tt01644 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01645 && cd 01645  && cp ../data/tt01645 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01646 && cd 01646  && cp ../data/tt01646 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01647 && cd 01647  && cp ../data/tt01647 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01648 && cd 01648  && cp ../data/tt01648 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01649 && cd 01649  && cp ../data/tt01649 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 01650 && cd 01650  && cp ../data/tt01650 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
