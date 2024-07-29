# Evologics-modems
Start by installing SDMShell (install git if neccessary or download manually) according to the [github page.](https://github.com/EvoLogics/sdmsh/wiki/SDM-%3A-SDMShell---Compile-and-Run)
```
$ git clone https://github.com/evologics/sdmsh.git
$ cd sdmsh
$ sudo apt-get install libreadline-dev -y
$ make
```
This should make the sdmsh file and add the libreadline dependancy.
Now to add our scripts for running the modems:
```
$ cd ..
$ git clone https://github.com/marinetech/Evologics-modems.git
$ mv sdmsh/sdmsh Evologics-modems/
```
finally remove the folder with the unnecessary sdm shell components
```
$ rm -rf sdmsh
```
