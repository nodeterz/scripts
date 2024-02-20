program calc_fpd
    implicit real*8 (a-h,o-z)
    parameter(nat=309,nat_sphere_max=309)
    parameter(ns=2,np=1)
    dimension rxyz(3,nat),alat(3)
    dimension fp(nat*(ns+3*np))  !fingerprint vectors
    dimension dfp(nat*(ns+3*np),3,nat) !fingerprint vectors derivative
    dimension rcov(nat)
    character*1 jobz,uplo 
    character*2 atomname
    !write(*,*) " The units are supposed to be Angstroem"
    open(unit=9,file='posinp.xyz',status='old')
    read(9,*) natp
    if (natp.ne.nat) stop 'wrong nat'
    read(9,*)
    do iat=1,nat
        read(9,*) atomname,rxyz(1,iat),rxyz(2,iat),rxyz(3,iat)
        call sym2rcov(atomname,rcv)
        rcov(iat)=rcv
    enddo
    close(9)
        !fingerprint_and_derivatives(nat, nat_sphere_max, ns, np, width_cutoff, alat, rxyz,rcov, fp, dfp)
    call fingerprint_and_derivatives(nat, nat_sphere_max, ns, np, 5.d0, 0.0, rxyz,rcov, fp, dfp)
    open(unit=9,file='fp.dat',status='new')
    do iat=1,nat*(ns+3*np)
        write(9,'(E24.10)') fp(iat)
    end do
end program calc_fpd
