""" Task definitions for invoke command line utility for python bindings
    overview article.
"""
# https://realpython.com/python-bindings-overview/

import invoke
import sys
import os
import shutil
import glob

on_win = sys.platform.startswith("win")


@invoke.task
def clean(c):
    """ Remove any built objects """
    for file_pattern in (
        "*.o",
        "*.so",
        "*.obj",
        "*.dll",
        "*.exp",
        "*.lib",
        "*.pyd",
        "cffi_example*",  # Is this a dir?
        "cython_wrapper.cpp",
    ):
        for file in glob.glob(file_pattern):
            os.remove(file)
    for dir_pattern in "Release":
        for dir in glob.glob(dir_pattern):
            shutil.rmtree(dir)


def print_banner(msg):
    print("==================================================")
    print("= {} ".format(msg))


@invoke.task()
def build_main(c, path=None):
    """ Build the shared library for the sample C or C++ code """
    c: invoke.Context
    if on_win:
        path = 'C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\VC\\Auxiliary\\Build\\'
        if not path:
            print("Path is missing")
        else:
            # Using c.cd didn't work with paths that have spaces :/
            #path = f'"{path}vcvars32.bat" x86'  # Enter the VS venv 32 bits
            path = f'"{path}vcvars32.bat" x64'  # Enter the VS venv 64 bits
            path += f'&& cd "{os.getcwd()}"'  # Change to current dir            
            """EXAMPLES"""
            # path += "&& cl main.cpp -I../Inc -I../../Drivers/STM32F4xx_HAL_Driver/Inc -I../../Drivers/CMSIS/Device/ST/STM32F4xx/Include -D STM32F446xx  -I../../Drivers/CMSIS/Include -D __CC_ARM"  # Compile           
            path += "&& cl -c main.cpp -D __Expouse_Functions__"  # Compile expouse functions
            # path += "&& cl -c main.cpp"  # Compile not expouse functions
            path += "&& cl /LD main.obj"
            c.run(path)
    else:
        print_banner("Building C Library")
        cmd = "g++ -c -Wall -Werror -fpic  main.cpp -I../Inc -I../../Drivers/STM32F4xx_HAL_Driver/Inc -I../../Drivers/CMSIS/Device/ST/STM32F4xx/Include -D STM32F446xx  -I../../Drivers/CMSIS/Include -D __GNUC__ "
        invoke.run(cmd)
        print("* Complete")

@invoke.task(
    clean,
    build_main
)
def all(c):
    """ Build and run all tests """
    pass


