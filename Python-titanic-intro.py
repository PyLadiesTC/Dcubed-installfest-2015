#####################
## GETTING STARTED ##
#####################
# We'll be practicing with the Kaggle 'Titanic: Machine Learning from Disaster' dataset available here:
# http://www.kaggle.com/c/titanic-gettingStarted/data.  Go ahead and download the 'train.csv' file and use the
# Python commands described below to help you get started exploring the dataset!

# You will need to enter the path to tell Python where to read the csv file from. Locate where you saved
# the train.csv file, and grab the entire path starting with "C:/..." and ending with ".../train.csv".

# Note that the way this is set up right now, the entire file will run when you hit shift + Enter.
# because the library imports at the top are needed for all the code below.

#%%
import csv as csv 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# We have to import the libraries we need for data analysis; csv is native to Python and the rest are included in Anaconda
# The csv module implements classes to read and write tabular data in CSV format
# NumPy is short for Numerical Pyhton and is used for scientific computing
# pandas contains data structures and functions useful for manipulation
# matplotlib is used for interactive plotting and data visualization

####################################################
## 1. LOAD THE TRAIN.CSV DATASET INTO A DATAFRAME ##
####################################################
csv_file_object = csv.reader(open('C:/Users/rox/Documents/GitHub/Dcubed-installfest-2015/train.csv', 'rb')) 
header = csv_file_object.next()
data=[] 
for row in csv_file_object:
    data.append(row)
data = np.array(data) 
# This sets up the data in the csv file as an ndarray object
# for whatever reason, this doesn't bring in last column: minor; thus the count is 12 not 13

###################################################################################
## 2. VIEW THE TABLE HEAD (i.e. the header row, plus the first few rows of data) ##
###################################################################################
print header
# prints header row, which consists of column names
print data[0]
# prints the 0th row of the array, which is the first record for a passenger
print pd.DataFrame(data, columns=header)
# uses a pandas data frame to print the header followed by the first several
# rows and the last several rows

###########################################
## 3. GET THE NUMBER OF ROWS AND COLUMNS ##
###########################################
print data.shape
# shape of an array is the dimensions: rows by columns (x,y).
# this should be (891, 13) but it didn't pull in the 'minor' column so it returns (891, 12)

################################################################################################
## 4. GET SUMMARY STATISTICS ON A COLUMN (i.e. minimum, maximum, mean, median, and quartiles) ##
################################################################################################
fare_col = data[:, 9]
# takes the fare column from the array and puts in a new array that just one column, entries are strings
# type(fare_col) is numpy.ndarray, type of elements is numpy.string
fare_col = fare_col.astype(np.float)
# makes copy of ndarray and converts elements from strings to floats so we can do calculations
print "mean: " + str(fare_col.mean())
# to print with the word "mean" in front, we have to make the value of the mean a string
print "min, max: " + str(fare_col.min()) + ", " + str(fare_col.max())

# It looks like the average (mean) fare for a trip on the Titanic was 32.20!

########################################
## 5. SORT ROWS AND MAKE A NEW COLUMN ##
########################################

# Order the rows by passenger fare, in ascending order
#titanicdata <- titanicdata[order(titanicdata$Fare), ]
#View(titanicdata) # use this command to view the sorted table, or click on the 'titanicdata' table in the 'Environment' tab in the right-hand panel in RStudio

# Order the rows by passenger fare, in descending order 
# (Note: You should notice that the most expensive fares were $512.3292!)
#titanicdata <- titanicdata[order(-titanicdata$Fare), ]

# Create a new column with a dummy variable indicating whether the passenger was under 18 years old (1) or over
# 18 years old (0)
#titanicdata$Minor <- factor(ifelse((titanicdata$Age < 18 ), 1 , 0 ))

# this section is still all R code
###########################################################
## 6. Plot the variables 'Age' vs. 'Survived' in boxplot ##
###########################################################
age = data[:, 5]
# Get just age column
# age = age.astype(np.float)
# Convert elements of age column into floats- doesn't work, maybe because there are nulls?
# I think I have to figure out how to make it into a list of values, somehow put in data frame and then plot it
survived = data[:, 1]
# Get just survived column
print survived
# elements of survived are numpy.string type and are 1 or 0

#%%
###########################################################
## 7. Plot the variables 'Age' vs. 'Fare' in scatterplot ##
###########################################################
#plot(titanicdata$Age, titanicdata$Fare, main="Scatterplot of Age vs. Fare", xlab="Age (in years)", ylab="Passenger Fare")
# this is still R code
