<!--lint disable no-literal-urls-->
<p align="center">
  <a href="https://Oso.com/">
    <img
      alt="Oso"
      src="http://clipart-library.com/images/ki8pMekir.png" width="192" height="120" 
    />
  </a>
</p>

�HONEY� 

Honeybees are disappearing at an alarming rate. As a consequence, the production of honey is also on the decline. This project is a simple demonstration of sourcing relatively clean data and using it to build a DataFrame that can be easily queried for the purpose of analysis and used for machine learning predictions.

# Table of contents

* [Support](#support)
* [Overview](#overview)
* The Process
  * [Imports](#imports)
  * [Data Analysis](#Data-Analysis)
  * [Data Cleaning](#data-cleaning)
  * [Data Export](#data-Export)

* [Current Project Team Members](#current-project-team-members) 

* [Collaborators](#collaborators)
  
## Support

Looking for help? Send an email for direct support &lt;hizstor@gmail.com&gt;

## Overview
Honey was built with PyCharm 2020.3.3 running Python 3.9.1.

Honey is designed to take a look at a set of data that shows the downward trend of honey production across the united states and predict production for the years to come. The data is already clean and requires little to no manipulation before modeling. The information will be loaded into a Pandas Dataframe grouped by year and then used to train and a model that will predict future honey production. 


## Imports
Libraries that must be imported to python environment for code to run successfully 

* **pandas**: Used to build DataFrames.
* **matplotlib.pyplot**: as plt, used for used to visualize data. 
* **numpy**: as np, a system for working with arrays.   
* **LinearRegression**: from sklearn.linear_model, built in functions for ML modeling.   



## Web Scraping

SPC will navigate to [CollegeBoard] website page that has a list of PDFs for each state and territory in the USA as well as a single PDF containing national data. Each file is identified by a .pdf href and downloaded to a local machine. The files are renamed at this time so they will be easier to reference in later steps. This will obtain the PDFs from the most recent reported year (currently 2020.) If earlier data sets are desired the code can easily be modified to collect that data from multiple years.
    
## PDF Conversion

The most challenging part of this project is converting information contained in a PDF to data easily accessed in python. The current code only extracts the data from a specific section of each PDF. This can be expanded as desired if information from other portions of the PDFs would be considered useful. SPC extracts this data by iterating through each PDF that was downloaded, identifying tables in the PDF and putting that data into a python list so it can be cleaned. 

## Data Cleaning

As is the case with most data obtained from outside sources, this data has a lot of erroneous or poorly organized information. SPC cleans the data so that it can more easily be utilized and understood. Erroneous data is removed and relevant data is reorganized in a way that can be used to create functional lists, dictionaries or DataFrames in Python. This part of the process also combines the data organized by state. 

## Data Export

Now that the data is clean it can be exported in the desired format. For this project it was exported as a csv file structured as a simple Python dictionary and as a csv file structured as a Pandas DataFrame. The code can easily be modified to export the data in other formats as desired.  

## Current project team members
* [OsoSuerte](https://github.com/OsoSuerte) -
**Ben Sadler** &lt;hizstor@gmail.com&gt; (he/him)


<!--lint disable prohibited-strings-->

### Collaborators

* [OsoSuerte](https://github.com/OsoSuerte) -
**Ben Sadler** &lt;hizstor@gmail.com&gt; (he/him)

<!--lint enable prohibited-strings-->

[Honey]: https://reports.collegeboard.org/sat-suite-program-results/
