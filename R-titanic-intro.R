#####################
## GETTING STARTED ##
#####################
# We'll be practicing with the Kaggle 'Titanic: Machine Learning from Disaster' dataset available here:
# http://www.kaggle.com/c/titanic-gettingStarted/data.  Go ahead and download the 'train.csv' file and use the
# R commands described below to help you get started exploring the dataset!

# First off, make sure the 'train.csv' data is located within your R 'working directory' for the following code 
# to load right.  R always keeps track of your 'working directory', and when it's looking for files, all filepaths
# are interpreted relative to your current 'working directory'.

# So before you start, check your 'working directory' with:
getwd()

# If the 'train.csv' file is NOT in your current working directory, you can either: 1) move the file to the
# directory indicated when you run the getwd() command, or 2) change your working directory in RStudio so it 
# points to the directory where your file is already located. To change your working directory in RStudio, 
# use the 'Files' interface in the right-hand panel in RStudio, navigate through your file system until you 
# locate the directory where 'train.csv' is located.  Then, select 'More' > 'Set as working directory'.  
# After that, you're set, and R should be able to find the .csv file!


####################################################
## 1. LOAD THE TRAIN.CSV DATASET INTO A DATAFRAME ##
####################################################
titanicdata <- read.csv("train.csv", header=TRUE)


###################################################################################
## 2. VIEW THE TABLE HEAD (i.e. the header row, plus the first few rows of data) ##
###################################################################################
head(titanicdata)


###########################################
## 3. GET THE NUMBER OF ROWS AND COLUMNS ##
###########################################
nrow(titanicdata)
ncol(titanicdata)
# Note: If you're using RStudio, you should also see the 'titanicdata' dataset loaded in the "Environment" tab in
# the right-hand panel.  The table size will also be listed there in the format: "## obs. of ## varables"


################################################################################################
## 4. GET SUMMARY STATISTICS ON A COLUMN (i.e. minimum, maximum, mean, median, and quartiles) ##
################################################################################################
summary(titanicdata$Fare)
# It looks like the average (mean) fare for a trip on the Titanic was 32.20!


########################################
## 5. SORT ROWS AND MAKE A NEW COLUMN ##
########################################

# Order the rows by passenger fare, in ascending order
titanicdata <- titanicdata[order(titanicdata$Fare), ]
View(titanicdata) # use this command to view the sorted table, or click on the 'titanicdata' table in the 'Environment' tab in the right-hand panel in RStudio

# Order the rows by passenger fare, in descending order 
# (Note: You should notice that the most expensive fares were $512.3292!)
titanicdata <- titanicdata[order(-titanicdata$Fare), ]

# Create a new column with a dummy variable indicating whether the passenger was under 18 years old (1) or over
# 18 years old (0)
titanicdata$Minor <- factor(ifelse((titanicdata$Age < 18 ), 1 , 0 ))


###########################################################
## 6. Plot the variables 'Age' vs. 'Survived' in boxplot ##
###########################################################
boxplot(titanicdata$Age ~ titanicdata$Survived, main="Boxplot of Age vs. Survival status", names=c("Died", "Survived"), ylab="Age (in years)")


###########################################################
## 7. Plot the variables 'Age' vs. 'Fare' in scatterplot ##
###########################################################
plot(titanicdata$Age, titanicdata$Fare, main="Scatterplot of Age vs. Fare", xlab="Age (in years)", ylab="Passenger Fare")
