module leap
  implicit none

contains

  logical function is_leap_year(year)
    integer :: year

    is_leap_year = .true.

    if (mod(year, 4) == 0) then
      if (mod(year ,100) == 0 .and. mod(year, 400) /= 0) then
        is_leap_year = .false.
      end if
    else
      is_leap_year = .false.
    end if
  end function

end module

