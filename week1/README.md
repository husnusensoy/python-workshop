
* [Download iTerm2](https://iterm2.com/)
* **Optional:** To create a better looking iTerm2 with zsh shell go to [Oh My ZSH](https://ohmyz.sh/)

# Some basic shell

* Change directory into `$HOME`: `cd ~`
* Create a new directory `mkdir coding`
* Change into that directory `cd coding`
* Move to parent directory `cd ..`
* Show current directory `pwd`


If `conda info` returns an error download 

* [Download Miniconda](https://docs.conda.io/en/latest/miniconda.html#installing)
  * Ensure that you pick the right architecture **intel** or **arm** (for M1)

Assuming that you have download it into **Downloads**

```bash
cd ~/Downloads

chmod +x Miniconda3-latest-MacOSX-x86_64.sh

./Miniconda3-latest-MacOSX-x86_64.sh

```
To check everything is OK open up a new window using Cmd + Shift + D and run `python --version` to see the version.

# Creating a new Python env in Conda

```bash
conda create -n python-training38 python=3.8
```

```bash
#
# To activate this environment, use
#
#     $ conda activate python-training38
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```

* To list existing environments: `conda env list`
* Remove existing environment: `conda env remove -n python-training37`

# Our Popular Editors/IDE

* [VSCode](https://code.visualstudio.com/)


## VSCode


* Ensure that u installed **Python** Plugin by Microsoft
* Ensure that u picked right env using `Cmd + Shift + P` -> **Select Interpreter**

* [PyCharm CE](https://www.jetbrains.com/pycharm/download/#section=mac)
* [Fleet](https://www.jetbrains.com/fleet/download/#section=mac)


# iTerm2 Short Cuts

* New Horizontal Split -> `Cmd + Shift + d`
* New Vertical Split -> `Cmd + d`
* Close split -> `Ctrl + a + d`
* Moving between windows -> `Cmd + Opt + <Arrow Keys>`

# Basics of Python 3

* [Learn X in Y Minutes](https://learnxinyminutes.com/docs/python/)
