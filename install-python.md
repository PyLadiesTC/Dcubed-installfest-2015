Install Python
==============

### Installing Anaconda on a Windows system:

1. Download the Anaconda installer from http://continuum.io/downloads.
2. Double click on the installer application icon and run it. Follow the instructions in the installer.

The installer is also capable of running in silent mode, without bringing up the graphical interface. To install Anaconda, type the following command into a command prompt:

    > Anaconda-2.x.x-Windows-x86[_64].exe /S /D=C:\Anaconda

The /D option specifies the install location.

**Note**
If you encounter any issues, please try disabling your anti-virus software.

Anaconda installs cleanly into a single directory, does not require Administrator or
root privileges, does not affect other Python installs on your system, or interfere
with OSX Frameworks.

### Installing Anaconda on a Mac system (64-bit Mac OSX, 10.5 and higher):

1. Download the Mac OS X Anaconda installer from http://continuum.io/downloads. 
2. Double click the installer to install.

Due to a bug in the Mac OS X installer software, you may see a screen that says: 
“You cannot install Anaconda in this location. The Anaconda installer does not allow its software to be installed here.”

To fix this, just click the **“Install for me only”** button with the house icon, and the installation will work again.

The installer package will automatically modify your bash profile to add anaconda to your PATH. 
If you do not want it to do this, you can choose “Customize” at the “Installation Type” phase.

Then deselect the “Modify PATH” option.

**Source:** [http://docs.continuum.io/anaconda/install.html]


Getting started
===============

Navigate to the terminal (OSX, Linux) or Command prompt (Windows) and type the following commands:

* to start Spyder (Scientific PYthon Development EnviRonment), the interactive development environment (IDE) included with Anaconda

    > spyder

Spyder comes with an Editor (on the left side) to write code, a Console (right side down) to evaluate it and see its results at any time, a Variable Explorer (right side up) to see what variables have been defined during evaluation, and several other facilities to help you to effectively develop the programs you need as a scientist.

Follow the 'First steps with Spyder' described in the tutorial provided in the 'Help' section of the program. 

* to start Iphyton

    > ipython

Type:<br />
    > print("Hello World")<br />
Then press enter. You'll see the message printed.<br />

Type:<br />
    > list = [1, 2, 3, 4]<br />
    > print list<br />

* to start IPython Notebook

    > ipython notebook

The IPython Notebook dashboard will launch inside your default web browser. 
Create a notebook by clicking the New Notebook button on the right. You can change the title of the notebook by left clicking on the current title at the top of the page. 

IPython has a set of magic commands that help the interactive programming process. Magic commands are prefixed with a single or double percent symbol. The pylab magic command automatically configures Python for plotting. Use the pylab magic command by entering the following into a code cell:

    > %pylab inline

Execute the cell and the pylab magic will run. In another code cell, add and execute the following Python code to plot a segment of the sine function:
	
    > x = linspace(0, 10)
    > y = sin(x)
    > plot(x, y)

Anaconda also includes a graphical Launcher application that enables you to start IPython Notebook, IPython QTConsole, and Spyder with a single click. 

On Mac, double click Launcher.app in your ~/anaconda directory.
On Windows, you’ll find Anaconda Launcher in your Start Menu.


* Check out what packages are installed with Anaconda

    > conda list

quickly display a list of all the packages in your default Anaconda environment. 
Conda is the package and environment manager tool included in Anaconda, it will allow you to install additional packages, to create environments with different versions of python or other packages, etc.
You can type the command 'conda -h' to pull up the help menu.

* Check for updates

    > conda update conda<br />
    > conda update anaconda<br />


Uninstalling
============

To remove Anaconda from your Windows sytem use the uninstaller in Add/Remove programs.

On Mac or Linux, remove all the prepended path variables in your .bashrc or your System Environment, and then remove the installation directory.


## More resources & tutorials...
* [Anaconda Quickstart Guide] (https://store.continuum.io/static/img/Anaconda-Quickstart.pdf)
* [Anaconda FAQs] (http://docs.continuum.io/anaconda/faq.html)
* [Getting started with IPython Notebook] (http://nbviewer.ipython.org/github/jvns/pandas-cookbook/blob/master/cookbook/A%20quick%20tour%20of%20IPython%20Notebook.ipynb)
* [More examples to practice with IPython Notebook] (http://nbviewer.ipython.org/github/jckantor/CBE20255/blob/master/notebooks/Getting%20Started%20with%20IPython.ipynb)

