# GHRSS Survey Plot
This code is a python program to plot the obsevered sky area, targetted sky area of the GHRSS High Resolution Southern Sky (GHRSS) Survey. This also allows plot the pulsars and RRATs discovered in the survey and other pulsars using coordinates or names of the pulsars. 

## Requirements
### Python Packages
The code uses the following python packages, which are required to be installed before running the code.

* astropy
* matplotlib
* pickel
* numpy

### Data Files
The code uses a few data files by default which can be seen on the repository. There are two kinds od datafiles: 
* .list file which contains the list of sources in the format HR_RADec (For eg: HR_0000-40).
* .csv file which contains list of pulsar names and their corresponding period seperated by ',' with a header "Pulsar_name, Period".

It is required that the new files given by user should follow same format for respective data. The path of the files is also required to be the same for all file, which can be changed accordingly in the <code>utility.py</code> file.


## Running the program
The user can run the program either on jupyter, colab or terminal using the commands.
### To run the program using jypyter notebook or google colaboratory
the file <code>GHRSS_survey_plot.ipynb</code> must be opened. It is required to run each cells in the sequential order. If the user is running the program on google colabotory, then all the data files can be saved on the google drive and the the correct path of these files must be given wherever required. 

### To run the program using command on terminal
it is required to run only <code>main.py</code> file using the command.
```
python3 main.py
```

ensure the python environment has required python packages and the path of the data files is correct.

## Input and Execution
The user it first given the choice to plot either on existing figure or to plot a complete new figure. On choosing the option to plot a new figure, any previously drawn plots will be erased permanently. After this, the user is given the option to plot various data as follows
* Targetted sky: to plot the sources which are targetted to be scanned in a survey. The user will be asked to give the number of files followed by the file-names (It should be .list file, the extension should not be mentioned).
* Observed sources : to plot the sources which are already scanned in a survey. User is given the option to plot all observed sources, which will directly take the exisiting data in file all_observed_sources.list. Any new data can also be appended to this file. Second option under this is to plot by giving the data files.
* Discovered objects: to plot the pulsars, millisecond pulsars (MSPs), RRATs discovered in the survey. 4 options are given under this category
  * Phase-1 : To plot objects discovered in phase-1 of the survey, new data can also be appended. (.csv file without any header is the accepted format)
  * Phase-2 : To plot objects discovered in phase-2 of the survey, new data can also be appended. (.csv file without any header is the accepted format)
  * New data files : To plot objects using the names of the pulsars (.csv file with appropriate header)
  * By giving the coordinates : To plot using a particular coordinates (only one object at a time). The coordinates can be either Right Accession-declination or Galactic latitude and longitude format.
* End : To terminate the input loop and see the final plot.
After the user gives input for any one of the 3 categories, the user will be again given same options in a loop until the the option "End" is chosen.

## Output
The output of the program is a single figure containing the plots for all data files as given by user. The figure contains a legend denoting the colour and symbol used for a particular data. The labels used in the legend are same as the file names. The normal pulsars, MSPs and RRATs are all given different symbols. It is required that in order to change the markers/colors necessary changes in the program (<code>functions.py</code>) can be made.
