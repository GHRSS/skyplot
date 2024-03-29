# GHRSS Survey Plot
This code is a python program to plot the observed sky area, targetted sky area of the GHRSS High Resolution Southern Sky (GHRSS) Survey. This also allows plotting the pulsars and RRATs discovered in the survey and other pulsars using coordinates or names of the pulsars.

## Requirements
### Python Packages
The code uses the following python packages, which must be installed before running the code.

* Astropy
* Matplotlib
* pickle
* NumPy

### Data Files
The code uses a few data files by default which can be seen on the repository. There are two kinds od datafiles: 
* .list file contains the sources in the format HR_RADec (E.g., HR_0000-40).
* .csv file contains the list of pulsar names and their corresponding period in milliseconds separated by ',' with a header "Pulsar_name, Period". 

It is required that the new files given by the user should follow the same format for respective data. The path of the files is also required to be the same for all files, which can be changed accordingly in the <code>config.py</code>.


## Running the program
The user can run the program either on jupyter, google colaboratory, or terminal using the commands.
### To run the program using jypyter notebook or google colaboratory
It is required to run the single cell in <code>GHRSS_survey_plot.ipynb</code>

If the user is running the program on google colaboratory, then all the data files can be saved on google drive, and the path of these files must be given <code>config.py</code>

### To run the program using command on terminal
It is required to run <code>main.py</code> file using the following command.
```
python3 main.py
```

Ensure that the Python environment has required python packages and the path of the data files is correct.
In order to plot more after the execution, the program can be rerun.

## Input and Execution
The user is first given a choice to plot either on the existing figure or a completely new figure. On choosing the option to plot a new figure, any previously drawn plots will be erased permanently. After this, the user is given the option to plot various data as follows
* Targetted sky: to plot the sources which are targetted to be scanned in a survey. The user will be asked to give the number of files followed by the file names (It should be a .list file, the extension should not be mentioned).
* Observed sources: to plot the sources which are already scanned in a survey. The user is given the option to plot all observed sources, which will directly take the existing data in the file all_observed_sources.list. Any new data can also be appended to this file. The second option under this is to plot by giving the data files.
* Discovered objects: to plot the pulsars, millisecond pulsars (MSPs), RRATs discovered in the survey. 4 options are given under this category
  * Phase-1: To plot objects discovered in phase-1 of the survey, new data can also be appended. (.csv file without any header is the accepted format)
  * Phase-2 : To plot objects discovered in phase-2 of the survey, new data can also be appended. (.csv file without any header is the accepted format)
  * New data files: To plot objects using the names of the pulsars (.csv file with appropriate header)
  * By giving the coordinates: To plot using particular coordinates (only one object at a time). The coordinates can be either Right Ascension-declination or Galactic latitude and longitude format.
* End: To terminate the input loop and see the final plot. The plot image is saved as <code>plot.png</code>

After the user gives input for any of the three categories, the user will be again given the same options in a loop until the option "End" is chosen.
For plotting more files on the figure already made, rerun the program/cell.

While plotting onto the existing graph, if the user is plotting sources, the plotted pulsars/RRATs might be overlapped. In such cases, it is required to re-plot the pulsar using the corresponding file/ coordinates.

## Output
The output of the program is a single figure containing the plots for all data files as given by the user. The figure contains a legend denoting the color and symbol used for a particular data. The labels used in the legend are the same as the file names. The normal pulsars, MSPs, and RRATs are all given different symbols. It is required that in order to change the markers/colors, necessary changes in the file (<code>config.py</code>) can be made. The following figure shows a sample output plot of the program.
![GHRSS_plot1](https://user-images.githubusercontent.com/101509174/164984008-261fcb9c-6680-409c-ba06-17eeec25eb90.png)

# Survey area plots
This code is the python program to plot the survey areas on the galatic coordinate system using the declination range or the latitude and longitude range. The output of the program is the single plot containing the shaded area with the sky temeperature map (Haslam 408 MHz Map)

## Running the program
The package <code>survey_area</code> contains the functions for plotting survey areas. It is required to run <code>main_survey_plots.py</code> file using the following command.
```
python3 main_survey_plots.py
```

Ensure that the Python environment has required python packages.

## Input
The user is given the choice of shading the survey area using 2 options
* declination range: maximum and minimum value of declination should be entered.
* Lattitude and longitude range: maximum and minimum value of the latitude and longitude should be entered.

## Output
The plot shows the shaded survey region according to the entered values with the sky temperature map.
