#!/bin/sh
#SBATCH --job-name="vasp"
#SBATCH --exclusive=user
#SBATCH --ntasks=16
#SBATCH --nodes=1-1
#SBATCH --cpus-per-task=1
#SBATCH --qos=kernph-1week
#SBATCH --partition=psi
#SBATCH --mem-per-cpu=1700M

cp -r ../../template_Au/ 00301 && cd 00301  && cp ../data/tt00301 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00302 && cd 00302  && cp ../data/tt00302 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00303 && cd 00303  && cp ../data/tt00303 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00304 && cd 00304  && cp ../data/tt00304 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00305 && cd 00305  && cp ../data/tt00305 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00306 && cd 00306  && cp ../data/tt00306 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00307 && cd 00307  && cp ../data/tt00307 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00308 && cd 00308  && cp ../data/tt00308 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00309 && cd 00309  && cp ../data/tt00309 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00310 && cd 00310  && cp ../data/tt00310 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00311 && cd 00311  && cp ../data/tt00311 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00312 && cd 00312  && cp ../data/tt00312 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00313 && cd 00313  && cp ../data/tt00313 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00314 && cd 00314  && cp ../data/tt00314 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00315 && cd 00315  && cp ../data/tt00315 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00316 && cd 00316  && cp ../data/tt00316 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00317 && cd 00317  && cp ../data/tt00317 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00318 && cd 00318  && cp ../data/tt00318 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00319 && cd 00319  && cp ../data/tt00319 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00320 && cd 00320  && cp ../data/tt00320 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00321 && cd 00321  && cp ../data/tt00321 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00322 && cd 00322  && cp ../data/tt00322 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00323 && cd 00323  && cp ../data/tt00323 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00324 && cd 00324  && cp ../data/tt00324 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00325 && cd 00325  && cp ../data/tt00325 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00326 && cd 00326  && cp ../data/tt00326 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00327 && cd 00327  && cp ../data/tt00327 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00328 && cd 00328  && cp ../data/tt00328 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00329 && cd 00329  && cp ../data/tt00329 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00330 && cd 00330  && cp ../data/tt00330 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00331 && cd 00331  && cp ../data/tt00331 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00332 && cd 00332  && cp ../data/tt00332 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00333 && cd 00333  && cp ../data/tt00333 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00334 && cd 00334  && cp ../data/tt00334 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00335 && cd 00335  && cp ../data/tt00335 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00336 && cd 00336  && cp ../data/tt00336 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00337 && cd 00337  && cp ../data/tt00337 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00338 && cd 00338  && cp ../data/tt00338 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00339 && cd 00339  && cp ../data/tt00339 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00340 && cd 00340  && cp ../data/tt00340 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00341 && cd 00341  && cp ../data/tt00341 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00342 && cd 00342  && cp ../data/tt00342 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00343 && cd 00343  && cp ../data/tt00343 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00344 && cd 00344  && cp ../data/tt00344 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00345 && cd 00345  && cp ../data/tt00345 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00346 && cd 00346  && cp ../data/tt00346 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00347 && cd 00347  && cp ../data/tt00347 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00348 && cd 00348  && cp ../data/tt00348 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00349 && cd 00349  && cp ../data/tt00349 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00350 && cd 00350  && cp ../data/tt00350 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00351 && cd 00351  && cp ../data/tt00351 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00352 && cd 00352  && cp ../data/tt00352 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00353 && cd 00353  && cp ../data/tt00353 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00354 && cd 00354  && cp ../data/tt00354 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00355 && cd 00355  && cp ../data/tt00355 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00356 && cd 00356  && cp ../data/tt00356 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00357 && cd 00357  && cp ../data/tt00357 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00358 && cd 00358  && cp ../data/tt00358 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00359 && cd 00359  && cp ../data/tt00359 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00360 && cd 00360  && cp ../data/tt00360 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00361 && cd 00361  && cp ../data/tt00361 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00362 && cd 00362  && cp ../data/tt00362 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00363 && cd 00363  && cp ../data/tt00363 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00364 && cd 00364  && cp ../data/tt00364 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00365 && cd 00365  && cp ../data/tt00365 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00366 && cd 00366  && cp ../data/tt00366 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00367 && cd 00367  && cp ../data/tt00367 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00368 && cd 00368  && cp ../data/tt00368 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00369 && cd 00369  && cp ../data/tt00369 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00370 && cd 00370  && cp ../data/tt00370 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00371 && cd 00371  && cp ../data/tt00371 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00372 && cd 00372  && cp ../data/tt00372 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00373 && cd 00373  && cp ../data/tt00373 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00374 && cd 00374  && cp ../data/tt00374 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00375 && cd 00375  && cp ../data/tt00375 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00376 && cd 00376  && cp ../data/tt00376 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00377 && cd 00377  && cp ../data/tt00377 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00378 && cd 00378  && cp ../data/tt00378 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00379 && cd 00379  && cp ../data/tt00379 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00380 && cd 00380  && cp ../data/tt00380 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00381 && cd 00381  && cp ../data/tt00381 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00382 && cd 00382  && cp ../data/tt00382 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00383 && cd 00383  && cp ../data/tt00383 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00384 && cd 00384  && cp ../data/tt00384 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00385 && cd 00385  && cp ../data/tt00385 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00386 && cd 00386  && cp ../data/tt00386 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00387 && cd 00387  && cp ../data/tt00387 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00388 && cd 00388  && cp ../data/tt00388 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00389 && cd 00389  && cp ../data/tt00389 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00390 && cd 00390  && cp ../data/tt00390 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00391 && cd 00391  && cp ../data/tt00391 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00392 && cd 00392  && cp ../data/tt00392 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00393 && cd 00393  && cp ../data/tt00393 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00394 && cd 00394  && cp ../data/tt00394 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00395 && cd 00395  && cp ../data/tt00395 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00396 && cd 00396  && cp ../data/tt00396 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00397 && cd 00397  && cp ../data/tt00397 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00398 && cd 00398  && cp ../data/tt00398 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00399 && cd 00399  && cp ../data/tt00399 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00400 && cd 00400  && cp ../data/tt00400 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00401 && cd 00401  && cp ../data/tt00401 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00402 && cd 00402  && cp ../data/tt00402 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00403 && cd 00403  && cp ../data/tt00403 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00404 && cd 00404  && cp ../data/tt00404 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00405 && cd 00405  && cp ../data/tt00405 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00406 && cd 00406  && cp ../data/tt00406 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00407 && cd 00407  && cp ../data/tt00407 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00408 && cd 00408  && cp ../data/tt00408 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00409 && cd 00409  && cp ../data/tt00409 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00410 && cd 00410  && cp ../data/tt00410 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00411 && cd 00411  && cp ../data/tt00411 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00412 && cd 00412  && cp ../data/tt00412 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00413 && cd 00413  && cp ../data/tt00413 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00414 && cd 00414  && cp ../data/tt00414 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00415 && cd 00415  && cp ../data/tt00415 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00416 && cd 00416  && cp ../data/tt00416 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00417 && cd 00417  && cp ../data/tt00417 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00418 && cd 00418  && cp ../data/tt00418 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00419 && cd 00419  && cp ../data/tt00419 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00420 && cd 00420  && cp ../data/tt00420 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00421 && cd 00421  && cp ../data/tt00421 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00422 && cd 00422  && cp ../data/tt00422 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00423 && cd 00423  && cp ../data/tt00423 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00424 && cd 00424  && cp ../data/tt00424 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00425 && cd 00425  && cp ../data/tt00425 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00426 && cd 00426  && cp ../data/tt00426 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00427 && cd 00427  && cp ../data/tt00427 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00428 && cd 00428  && cp ../data/tt00428 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00429 && cd 00429  && cp ../data/tt00429 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00430 && cd 00430  && cp ../data/tt00430 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00431 && cd 00431  && cp ../data/tt00431 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00432 && cd 00432  && cp ../data/tt00432 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00433 && cd 00433  && cp ../data/tt00433 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00434 && cd 00434  && cp ../data/tt00434 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00435 && cd 00435  && cp ../data/tt00435 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00436 && cd 00436  && cp ../data/tt00436 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00437 && cd 00437  && cp ../data/tt00437 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00438 && cd 00438  && cp ../data/tt00438 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00439 && cd 00439  && cp ../data/tt00439 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00440 && cd 00440  && cp ../data/tt00440 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00441 && cd 00441  && cp ../data/tt00441 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00442 && cd 00442  && cp ../data/tt00442 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00443 && cd 00443  && cp ../data/tt00443 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00444 && cd 00444  && cp ../data/tt00444 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00445 && cd 00445  && cp ../data/tt00445 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00446 && cd 00446  && cp ../data/tt00446 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00447 && cd 00447  && cp ../data/tt00447 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00448 && cd 00448  && cp ../data/tt00448 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00449 && cd 00449  && cp ../data/tt00449 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00450 && cd 00450  && cp ../data/tt00450 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
