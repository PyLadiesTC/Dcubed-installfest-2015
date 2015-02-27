# coding: utf-8

# # Python Practice with Titanic
# 
# ## Getting Started

# We'll be practicing with the Kaggle 'Titanic: Machine Learning from Disaster' dataset available here:
# http://www.kaggle.com/c/titanic-gettingStarted/data.  Go ahead and download the 'train.csv' file and use the
# Python commands described below to help you get started exploring the dataset!
# 
# You will need to enter the path to tell Python where to read the csv file from. Locate where you saved
# the train.csv file, and grab the entire path starting with "C:/..." and ending with ".../train.csv". If you put
# the file in the same directory as this notebook, then you can simply load it as "train.csv"
# 
# This version of the example is run as a single script file. Using Python to execute the code in this script
# should print some output and display a boxplot graph of the Titanic dataset.

# ## 0. Load necessary libraries
# 
# First we import the libraries we need for data analysis; these are all included with Anaconda
# 
# * NumPy is short for Numerical Python and is used for scientific computing
# * pandas contains the DataFrame class and many tools for data analysis
# * matplotlib is used for interactive plotting and data visualization
# 

# In[1]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ## 1. LOAD THE TRAIN.CSV DATASET INTO A DATAFRAME
# 
# Pandas can fill a DataFrame from many different sources, including .csv files, but also web URLs, database queries, etc...

# In[39]:

titanicdata = pd.read_csv('train.csv')
titanicdata


# ## 2. VIEW THE TABLE HEAD
# 
# In the notebook, this should display the first ten rows as a nicely formatted HTML table.
# 
# This is the same syntax Python uses for arrays and other "indexable" objects. Notice that counting starts from zero.

# In[3]:

titanicdata[0:10]


# ## 3. GET THE NUMBER OF ROWS AND COLUMNS

# In[4]:

titanicdata.shape


# ## 4. GET SUMMARY STATISTICS (i.e. minimum, maximum, mean, median, and quartiles)
# 
# The average (mean) fare for a trip on the Titanic was 32.20.
# 
# Notice that describe() doesn't bother to compute statistics for the columns that are non-numeric.

# In[5]:

titanicdata.describe()


# ## 5. SORT ROWS AND MAKE A NEW COLUMN ##
# 
# Let's order the rows by passenger fare and take a look at the most expensive fares.

# In[8]:

titanicdata = titanicdata.sort(columns='Fare', ascending=False)
titanicdata[0:5]


# Looks like PC 177755 was a really swanky ticket!
# 
# Now let's create a new column with a boolean value indicating whether the passenger was a minor (under 18) and view a few of them.

# In[38]:

titanicdata['isMinor'] = (titanicdata['Age'] < 18.0)
titanicdata[titanicdata['isMinor'] == True][0:5]


# ## 6. Plot the variables 'Age' vs. 'Survived' in boxplot ##
# 
# The built-in plots are powerful, but let's also demonstrate some simple options to customize and combine these plots.

# In[122]:

# Start with the default boxplot style
ax = titanicdata.boxplot(column='Age', by='Survived', return_type='axes', figsize=(10,5))

# Now add the actual data points, with some jitter to reduce overplotting, color coded by sex
color = titanicdata.Sex.apply(dict(male='red', female='green').get)
x = titanicdata.Survived + np.random.normal(0, 0.01, len(titanicdata.Age)) + 1
plt.scatter(x, titanicdata.Age, c=color, alpha=0.2)

ax['Age'].set_xlabel('Passenger Status')
ax['Age'].set_ylabel('Passenger Age')
ax['Age'].set_title('Boxplot of Age vs. Survival Status')
ax['Age'].xaxis.set_ticklabels(['Died', 'Survived'])


