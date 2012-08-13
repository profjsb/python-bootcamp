subroutine arithmetic(a,b,c,d)
  
  implicit none

  ! Declarations
  real, intent(in) :: a,b
  real, intent(out) :: c,d

  c = a + b
  d = a * b

end subroutine arithmetic
