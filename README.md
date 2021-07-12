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

Creating a C++ project in nucleo board to keep communication serial USART with a STM Nucleo-F446RE Board 




![image](https://user-images.githubusercontent.com/48602725/125197963-b511d480-e214-11eb-8766-f8fe53f0db30.png)

references----> http://www.coffeebrain.org/wiki/index.php?title=USART_B%C3%A1sico


test the serial communication. although exist  PUTTY and TERATERM to establish and test connection serial with our board I prefer minicom,I reccomend that you have install a window subsystem linux, here you can find the steps to will install the app https://docs.microsoft.com/es-es/windows/wsl/install-win10  and after install the minicom 

I installed the Ubuntu 20.04 LTS release on Windows, in this new version you don't need use the apt-get only the apt in the (Focal Fossa) version, obviously you can choose the Linux version os with you to feel comfortable "remember update and upgrade"
~~~
 sudo apt update && sudo apt upgrade -y
 sudo apt  install minicom 
~~~

to run a minicom interface you need to type the following command 
~~~
sudo minicom -s.

~~~
![image](https://user-images.githubusercontent.com/48602725/125220799-1b7e0d80-e27c-11eb-8f22-99a4a30057ca.png)


remember that you shall set the virtual COM port, and you can find in the device manager.
![image](https://user-images.githubusercontent.com/48602725/125220616-e2459d80-e27b-11eb-84f3-e95c544bb5ad.png)


![image](https://user-images.githubusercontent.com/48602725/125220979-5ed87c00-e27c-11eb-82c2-7651508c0682.png)


![image](https://user-images.githubusercontent.com/48602725/125221031-7283e280-e27c-11eb-9232-26085c22d39f.png)










Well, the one of important thing that I recommended you is to install the next program, which will help you can see if your function is accessible, it is necessary when you want to call the function of your dll.

https://www.nirsoft.net/utils/dll_export_viewer.html


![image](https://user-images.githubusercontent.com/48602725/124914144-dc626a80-dfa4-11eb-869c-7b3d4126dc9d.png)
