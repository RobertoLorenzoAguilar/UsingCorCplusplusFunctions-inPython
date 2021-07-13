#include "main.h"
#include <iostream>
int main(char * path_str)
{     
    // Using strcmp()
    int res = strcmp(path_str, "Santiago & Roberto");
      
    if (res==0)
        printf("Strings are equal");
    else 
        printf("Strings are unequal");
      
    printf("\nValue returned by strcmp() is:  %d" , res);
    return res;
}





