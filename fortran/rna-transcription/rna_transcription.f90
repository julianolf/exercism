module rna_transcription
        implicit none
contains

        function to_rna(dna)
                character(*) :: dna
                character(len(dna)) :: to_rna
                character :: n
                integer :: i

                do i = 1, len(dna)
                        n = dna(i:i)

                        if (n == 'G') then
                                to_rna(i:i) = 'C'
                        else if (n == 'C') then
                                to_rna(i:i) = 'G'
                        else if (n == 'T') then
                                to_rna(i:i) = 'A'
                        else if (n == 'A') then
                                to_rna(i:i) = 'U'
                        end if
                end do

        end function to_rna

end module rna_transcription
