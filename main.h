#include<stdio.h>
#include<string.h>

#if defined ( __Expouse_Functions__ )
    #define EXPORT_SYMBOL __declspec(dllexport)
    EXPORT_SYMBOL int  main(char * path_str);
#endif




