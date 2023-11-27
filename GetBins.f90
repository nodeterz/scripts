program CalculateEnergyDifferenceAndDistance
  implicit none

  ! Define parameters
  integer, parameter :: num_structures = 4916
  integer, parameter :: num_atoms = 60
  integer, parameter :: max_columns = 500
  integer, parameter :: bins_Num = 10000
  character(80) :: input_file
  character(80) :: output_file
  character(180) :: input_filename, output_filename,num_columns_str
  character(1) :: null_term
  character(80) :: formatStr 
  integer :: maxValIndex = -bins_Num 
  integer :: minValIndex = bins_Num
  integer :: maxDesIndex = -bins_Num 
  integer :: num_columns ! The number of columns
  integer :: arg_count, i, j, k
  integer :: unit_in, unit_out
  integer :: valIndex, desIndex 
  integer, dimension(-bins_Num:bins_Num,bins_Num) :: Bins
  real(8) :: desRange=1.d0
  real(8) :: valRange=10.d0
  real(8) :: desX,valX
  real(8), dimension(num_structures*num_atoms, max_columns) :: data
  real(8) :: energy_difference
  real(8) :: distance
  
! Calculate the bininig grid size
  desX=desRange/bins_Num
  valX=valRange/bins_Num
! Get the command-line arguments for input file, output file, and number of columns
  call get_command_argument(1, input_filename, arg_count)
  call get_command_argument(2, output_filename, arg_count)
  call get_command_argument(3, num_columns_str, arg_count)
  input_file = trim(input_filename)
  output_file = trim(output_filename)
  ! Convert the number of columns from string to integer
  read(num_columns_str, *) num_columns
  num_columns = num_columns+1

  ! Check if the argument count is valid
  if (arg_count /= 2) then
    write(*,*) "Usage: ./program_name input_file.txt output_file.txt num_columns"
    write(*,*) arg_count,input_filename,output_filename,num_columns_str
    stop
  end if

  ! Open the input file
  open(unit_in, file=input_file, status='old')

  ! Read data from the file
  do i = 1, num_structures*num_atoms
     read(unit_in, *) data(i, 1:num_columns)
  end do

  ! Close the input file
  close(unit_in)

  ! Calculate energy difference and distance using OpenMP parallelization
  do i = 1, num_structures * num_atoms
    write(*,*) 'Proc:',(i-1)/num_atoms
    do j = i + 1, num_structures * num_atoms
      energy_difference = data(i, 1) - data(j, 1)
      distance = 0.d0
      do k = 2, num_columns
        distance = distance + (data(i, k) - data(j, k))**2
      end do
      distance = sqrt(distance)
      valIndex = ceiling(energy_difference / valX)
      desIndex = ceiling(distance / desX)
      if (desIndex > bins_Num) cycle
      if (valIndex > bins_Num) cycle
      if (valIndex < -bins_Num) cycle
      bins(valIndex, desIndex) = bins(valIndex, desIndex) + 1
      maxValIndex = max(maxValIndex, valIndex)
      minValIndex = min(minValIndex, valIndex)
      maxDesIndex = max(maxDesIndex, desIndex)
    end do
  end do

  write(*,*) maxValIndex,minValIndex,maxDesIndex
  ! Open the output file
  open(unit_out, file=output_file, status='replace')
  write(unit_out,'(a,a,2f8.3,3I6)') '# ',trim(input_file),desRange,valRange,maxValIndex,minValIndex,maxDesIndex

  ! Write the results to the output file
  write(formatStr,'(a,i5,a)') '(',maxDesIndex,'I10)'
  do i = minValIndex,maxValIndex
    write(unit_out,formatStr) bins(i,1:maxDesIndex)
  end do

  ! Close the output file
  close(unit_out)

  ! Now, the results have been written to the output file.

end program CalculateEnergyDifferenceAndDistance
