module bob
  implicit none
contains

  function hey(statement) result(msg)
    character(100) :: msg
    character(len=*), intent(in) :: statement

    character :: curr_char, last_char
    logical :: asking, yelling, has_chars
    integer :: char_length, ord, ascii_a_lower, ascii_z_lower, ascii_a_upper, ascii_z_upper, i

    ascii_a_lower = ichar('a')
    ascii_z_lower = ichar('z')
    ascii_a_upper = ichar('A')
    ascii_z_upper = ichar('Z')
    asking = .false.
    yelling = .true.
    has_chars = .false.
    char_length = len_trim(statement)
    last_char = statement(char_length:char_length)

    if (last_char == '?') then
            asking = .true.
    end if

    do i = 1, char_length
        curr_char = statement(i:i)
        ord = ichar(curr_char)

        if (ord >= ascii_a_lower .and. ord <= ascii_z_lower) then
                yelling = .false.
                has_chars = .true.
        else if (ord >= ascii_a_upper .and. ord <= ascii_z_upper) then
                has_chars = .true.
        end if
    end do

    if (char_length == 0) then
            msg = "Fine. Be that way!"
    else if (asking .and. yelling .and. has_chars) then
            msg = "Calm down, I know what I'm doing!"
    else if (yelling .and. has_chars) then
            msg = "Whoa, chill out!"
    else if (asking) then
            msg = "Sure."
    else
            msg = "Whatever."
    end if
  end function hey

end module bob
