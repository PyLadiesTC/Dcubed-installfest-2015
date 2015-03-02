Install R
=========

## Installing the R base software
To install R, all you have to do is head to one of R's CRAN servers and download the proper R installer for your operating system.  "CRAN" stands for "Comprehensive R Archive Network", which is the worldwide network of computers responsible for hosting and serving the R base software and packages for you to use and enjoy.  The [CRAN mirrors site](http://cran.r-project.org/mirrors.html) lets you take a look at where all of these CRAN-networked computers are located.  

When choosing a CRAN mirror, just pick one close to where you live, and R will do the rest!  (And don't worry--you don't have to be **too** precise about distance here...it's just generally best to pick a mirror that's closer to you for faster download times.)  So, since we're in Minnesota, let's head to a CRAN mirror that's hosted nearby at [Iowa State University](http://streaming.stat.iastate.edu/CRAN/).

### For Windows
Then, from the mirror page, click on **base** to get the basic R installation. Then download the following:
* R-3.1.2-win.exe (54 MB) (R base distribution for Windows)

Double-click the .exe file and it will walk you through the standard Windows installation process.

Note: If you're using Windows, you may notice that R automatically installs two different versions of the software--one for 32-bit and one for 64-bit systems.  Simply launch the version that corresponds to the version of Windows you're running.  If you've got a new-ish computer, it's likely you're running 64-bit Windows, and if you've got an old-ish computer, you may still be on 32-bit Windows.  But it never hurts to check!  To see whether you're running 32-bit or 64-bit Windows, right-click on "My Computer", then click "Properties".  Look for the "System type" listed there, which will tell you which version you're running.


### For Mac
From the mirror page, click "Download R for (Mac) OS X" and grab one of the following files:
* R-3.1.2-mavericks.pkg (55 MB) (R base distribution for Mac 10.9)
* R-3.1.2-snowleopard.pkg (68 MB) (R base distribution for Mac 10.6)

Note: R doesn't yet have a package released specifically for Yosemite yet, so if you've already upgraded to Yosemite, go ahead and grab the "mavericks" file and it should work just fine!

Double-click the .dmg file and it will walk you through the standard installation process for your operating system.


## Installing RStudio
Now that you've got the R base software installed, you may notice if you launch R right away that it opens up a somewhat ugly-looking console for you to interact with that kind of feels like a "black box".  Let's fix that and give you a richer set of features to surround your R console and make it more user-friendly...

Enter [RStudio](http://www.rstudio.com/), R's super-spiffy integrated development environment (IDE)!  For beginners--and actually, for everyone--it's a great idea to go ahead and install RStudio right away to save yourself a bunch of headaches.  Once you've got it set up, RStudio makes it really easy to manage your data, script files, plots, and packages as you go along.

Head to the [RStudio download page](http://www.rstudio.com/products/rstudio/download/) and pick the latest version of R Studio that works with your operating system.  The latest versions should be something like:
* RStudio-0.98.1102.exe (45 MB) (R Studio for Windows)
* RStudio-0.98.1102.dmg (38.4 MB) (R Studio for Mac)

After that, double-click the .exe file (for Windows) or .dmg (for Mac), and it will walk you through the standard installation process for your operating system.

Once you've got RStudio installed, that should be all you need to get going!  From now on, you can just click on the RStudio logo and launch that, and it will auto-load the R software you just installed on your computer for you to use within the IDE.


## Installing Packages
There are a number of add-on libraries (or "packages", in R speak) that are popular in the R community.  Packages are essentially extensions for the R base software that you can download to do some fun, quirky, and useful things you may need when working on different projects.  In fact, one of R's biggest draws is its rich set of packages optimized for data analysis and visualization that users have created for it over the years.  A few suggestions for packages to look into as you're getting started:

### Datasets
* *datasets* - A library that contains tons of sample datasets.

### Special Data Analysis
* *xts* - A package for time series analysis.

### Data Tidying
* *dplyr* - R's built-in options for sorting and subsetting data are decent, but not always as quick or intuitive as some would like.  This library gives you functions to help sort, slice up, and manipulate your data more efficiently. Think about it as creating pivot tables in R.
* *tidyr* - Another one of the R famous Hadley Wickham's creation. This is a companion to dplyr to make data munging and pivoting data much easier.
* *data.table* - A package to quickly handling, munging, and cleaning up large datasets.
* *lubridate* - A package that may help you with date and time conversions.

### Machine Learning
* *caret* - Package that contains many helpful machine learning functions.

### Data Visualization
* *googleVis* - Lets you generate Google Charts from within R.
* *ggplot2* - R's built-in plotting options can look a little ugly, so this is a popular library that people use to improve the look of their plots.  Great for design-minded folks who are frustrated with the "default" look of R!  A word of caution: this library has a somewhat complex syntax unto itself, so it can take some time to learn, and even has entire books devoted to mastering it.
* *gridExtra* - If you want to put multiple ggplot graphs next to each other, you will need to use this package.
* *RColorBrewer* - Helps you generate nice, ColorBrewer-approved color schemes that you can apply to your plots.
* *shiny* - Create interactive R apps in R!


Installing packages is really easy!  For example, to install the "datasets" and "dplyr" packages, first make sure you're online, then head to the R console and execute:
````R
install.packages("datasets")
install.packages("dplyr")

# Or install all packages at once with
install.packages(c("datasets", "dplyr"))
````

R may then prompt you to choose a CRAN mirror.  Again, just pick a mirror that's close to where you're located, and R will do the rest!

## [Resources and Tutorials](resources.md)
