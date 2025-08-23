#include <ctype.h>
#include <stdlib.h>
#include <string.h>

#include "isogram.h"

bool is_isogram(const char phrase[])
{
        if (phrase == NULL)
                return false;

        int length = strlen(phrase);

        if (length < 2)
                return true;

        char ctable[25] = { 0 };
        char current = 0;
        int pos = 0;
    
        for (int i = 0; i < length; i++) {
                current = tolower(phrase[i]);

                if (current > 96 && current < 123) {
                        pos = current - 97;

                        if (ctable[pos] != current)
                                ctable[pos] = current;
                        else
                                return false;
                }
        }

        return true;
}
