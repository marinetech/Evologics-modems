# Evologics-modems
This repository contains instructions for compiling the required SDMShell by Evologics for controling their modems, as well as python wrapper scripts for use to transmit with the modem (need to add recording)

Start by installing the libreadline dependancy:
```
$ sudo apt-get install libreadline-dev -y
```
The install the SDMShell (install git if neccessary or download manually) according to the [github page.](https://github.com/EvoLogics/sdmsh/wiki/SDM-%3A-SDMShell---Compile-and-Run)
```
$ git clone https://github.com/evologics/sdmsh.git
$ cd sdmsh
$ make
```
This should make the sdmsh file suitable for the used system.
Now to add our scripts for running the modems:
```
$ cd ..
$ git clone https://github.com/marinetech/Evologics-modems.git
$ mv sdmsh/sdmsh Evologics-modems/
```
finally remove the folder with the unnecessary sdm shell components.
```
$ rm -rf sdmsh
```
In order to transmit a signal (the repository contains a couple of example signals), enter the working directory and run the python script:
```
$ cd Evologics-modems
$ python3 tx.py
```
the examples are setup to run on a modem with the ip 192.168.0.136. in order to use a different one, change the modem number in the python script. 
