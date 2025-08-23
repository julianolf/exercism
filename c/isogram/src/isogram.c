#include <ctype.h>
#include <stdlib.h>
#include <string.h>

#include "isogram.h"

bool is_isogram(const char phrase[])
{
        if (phrase == NULL)
                return false;

        int length = strlen(phrase);
        char ctable[26] = { 0 };
    
        for (int i = 0; i < length; i++) {
                char current = tolower(phrase[i]);

                if (isalpha(current)) {
                        int pos = current - 97;

                        if (ctable[pos] != current)
                                ctable[pos] = current;
                        else
                                return false;
                }
        }

        return true;
}
