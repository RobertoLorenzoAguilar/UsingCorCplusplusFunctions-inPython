# Using C or C++ Functions in Python
How you can call functions in c or c++ since python language?

although exists some different ways, I will show you how you can call your functions through dlls

The first step is generate the dll file.

In my case, I will reproduce a little one example into the windows operating system.

I take advantage of the Visual Studio C/C++ IDE and Compiler for Windows.

![image](https://user-images.githubusercontent.com/48602725/124915834-d9687980-dfa6-11eb-92e4-8c9eecee2b7d.png)


if you want only you can install only the MSBuild on the command line - C++. without the necessity to install the Visual Studio IDE complete https://docs.microsoft.com/en-us/cpp/build/building-on-the-command-line?view=msvc-160.

But in my case, because I have some problems I decided to isolate the problem first started to compile one "Hello World" in the IDE.

note: before I had a lot of problems with   https://www.msys2.org/  who provide a collection of tools and libraries of Linux to run in windows, but really  I don't  tried with  Window Subsystem Linux sounds good well, possible I will make a test in the future.



prerequisites

 you need have install the:

~~~
          -python3 ("my version is python 3, I didnt try with version 2")
          -python install pip -----> this is the python package manager
          -python3 -m pip install invoke -----> we need this tool to invoke  enviroment vcvars32.bat
~~~

please dont forget set the system enviroments variables.

![image](https://user-images.githubusercontent.com/48602725/125308991-3b4a1b80-e2e6-11eb-9bca-abb7d6d0da6e.png)




As of now you can interact with the board.


The next step will be to try to create a DLL to embedded in other kind of project in a Graphical user interface.
this is my main.cpp

![image](https://user-images.githubusercontent.com/48602725/125455366-a98149af-ac4c-4846-a022-84b1606dd7a1.png)


this is my main.h  remember expouse the param -D __Expouse_Functions__

![image](https://user-images.githubusercontent.com/48602725/125455387-babf19e7-d1ff-42f3-b24a-3171558fa8cf.png)


here you can see in my method the way to create the .dll 

![image](https://user-images.githubusercontent.com/48602725/125455468-485ffb53-823a-4361-a89e-7cabb34d4f7a.png)


you should open the project folder and run in  cmd.
~~~
invoke clean
invoke build-main
~~~
remember always clean

Here I started to test the DLL in python, is simple string comparing.
![image](https://user-images.githubusercontent.com/48602725/125456431-d873076a-8d2f-48ae-9856-560e4cd0359b.png)




If you have this problem, it's because you built the project in other architecture different from what you using in your python interpreter, please change in the tasks.py the line:
~~~
 -path = f'"{path}vcvars32.bat" x86'  # Enter the VS venv 32 bits
 -path = f'"{path}vcvars32.bat" x64'  # Enter the VS venv 64 bits
~~~

![image](https://user-images.githubusercontent.com/48602725/125453551-2120a171-3933-4c98-8851-7a2f4978fa46.png)



Well, the one of important thing that I recommended you is to install the next program, which will help you can see if your function is accessible, it is necessary when you want to call the function of your dll.

![image](https://user-images.githubusercontent.com/48602725/125457717-5bb53afa-717f-4a67-ade2-ac8ee761d7be.png)




TODO: Pending by load.
~~~
1.- the references.
2.- STM32 code.cpp UART communication. By the moment, I couldn't compile the project, I need to learn about of Cortex-M4  :S, I wanted to incorporate the activities with process STM Board , to recreating A scenery a little more real,  I leave in stand by
g++ -O3 -Wall -Werror -shared -std=c++11 -fPIC  main.cpp -I../Inc -I../../Drivers/STM32F4xx_HAL_Driver/Inc -I../../Drivers/CMSIS/Device/ST/STM32F4xx/Include -D STM32F446xx  -I../../Drivers/CMSIS/Include  -D __GNUC__   I believe that I need to create a dll to work with the drivers, however, I hope that I hope someone benefits with the information about of how to establish communication serial with this kind of board, probably in the future I change this thread to other repository
3.- I need Upload this code how to create a DLL
4.- try to recrate the functionality using a python library in place of dll.
5.- Create GUI
~~~
