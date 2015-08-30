#-*- coding: utf-8 -*-
########################################################################
########################################################################
# 1: exercise 1-1 walkthrough

# There is more than one way to accomplish a task in code
# Some solutions are more elegant than others
# Elegance isn’t a requirement, but becomes important when working with lots of data (or many operations)
# The built-in functions are generally going to be more efficient and robust


########################################################################
########################################################################
# 2: basic DESCRIPTIVE STATISTICS with the PANDAS module

# "We are drowning in information but starved for knowledge." - John Naisbitt

# Why statistics?
	# Tools for extracting meaning from data
	# Commonly understood ways of communicating meaning to others

# basic DESCRIPTIVE STATISTICS
	# Quantitatively describe the main features of a data set
	# Help distinguish distributions and make them comparable

	# measures of central tendency
	# • Quantitative data tends to cluster around some central value
	# • Contrasts with the spread of data around that center (i.e. the variability in the data)
	# • Measures of central tendency help us understand our data
	# • Measures of central tendency are often used as inputs to algorithms

	# 1. MEAN is a more precise measure and more often used
	# 2. MEDIAN is better when there are extreme outliers
	# 3. MODE is used when the data is categorical (as opposed to numeric)

	# measures of variability 
	# • Describe the distribution of our data

	# 4. RANGE
	#    QUAR(N)TILES
	#    INTER-QUARTILE RANGE
	#    OUTLIERs

	# 5. STANDARD DEVIATION
	#    VARIANCE

# (Didn't have time for these)
# calculate COEFFICIENT OF CORRELATION
# calculate COEFFICIENT OF DETERMINATION
# perform LINEAR REGRESSION


########################################################################
# Fill out this Google Doc: http://bit.ly/1f59Fki

# To avoid confusion,
# save the data set in your Lede folder,
# and in terminal move to the Lede folder
# before firing up iPython notebook or running python

# In iPython notebook or in Sublime Text,
import pandas as pd
	# the PANDAS module
	# similar to the R programming language
	# combines libraries like `numpy`, makes charting easy

	# `as` is for when we want an ALIAS for our module.
	# We're too lazy to type out "pandas", so we tell Pyton we're just going to type "pd"

# Read in our data set
ourdataframe = pd.read_excel( "height_weight.xlsx" )
# OR,
ourdataframe = pd.read_csv( "Data_Collection_Sheet.csv" )


########################################################################
# HISTOGRAM
# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.hist.html

# • Charts the frequency of instances in the data
# • Shows the frequency distribution
# • Values are grouped into class intervals
# • Best to have a consistent size to class intervals (SLIDE34)
# http://mathematica.stackexchange.com/questions/59520/histogram-with-variable-bin-size

# If you're doing this in iPython notebook, run
## %matplotlib inline
# to make the plots show up in the notebook and NOT on another window.
	# anyone use MATLAB before? `matplotlib` is a Python version of that

ourdataframe.hist()
# or perhaps
ourdataframe['age (years)'].hist() # just one of the columns
# or perhaps
ourdataframe['age (years)'].hist( bins=5 ) # change the bin size to 5 # (SLIDE37)
# or perhaps
ourdataframe[['age (years)','siblings (not including you)']].hist( bins=4 ) # just two of the columns

# If you're doing this NOT in iPython notebook, also run
from matplotlib import pyplot
pyplot.show()


########################################################################
# DATA DISTRIBUTIONS
# NORMAL    distribution # (SLIDE39)
# LONG-TAIL distribution # (SLIDE40)
# BI-MODAL  distribution # (SLIDE41)


########################################################################
# A bunch of descriptive statistics at a glance
print ourdataframe.describe()
#        height (inches)  age (years)  siblings (not including you)
# count        22.000000    22.000000                      22.00000
# mean         66.623477    29.500000                       1.50000
# std           3.239595     7.676495                       1.05785
# min          61.000000    22.000000                       0.00000
# 25%          65.000000    24.250000                       1.00000
# 50%          66.500000    27.000000                       1.00000
# 75%          67.537375    32.000000                       2.00000
# max          74.000000    49.000000                       3.00000


########################################################################
# 1. MEAN

# • A representative value for the data
# • Usually what people mean by “average”
# • Calculate by adding all the values together and dividing by the number instances
# • Sensitive to extremes
# if an 8-year-old walked into the room and we added his height and age, those means would go way down

print ourdataframe.mean()
# height (inches)                 66.623477
# age (years)                     29.500000
# siblings (not including you)     1.500000
# dtype: float64

# dtype: float64 # the datatype pandas uses to encode the data


########################################################################
# 2. MEDIAN

# • The “middle” value of a data set # (SLIDE43)
	# – Center value of a data set with an odd number of values
	# – Sum of two middle values divided by 2 if the number of items in a data set is even
# • Resistant to extreme values

print ourdataframe.median()
# height (inches)                 66.5
# age (years)                     27.0
# siblings (not including you)     1.0
# dtype: float64


########################################################################
# (SLIDE44)
# mean and median  are the same  for normal distributions
# mean and median  may diverge   for other distributions 


########################################################################
# 3. MODE

# • most frequent value in a data set # (SLIDE45)
# • often used for categorial data
# oft used for signal processing

print ourdataframe.mode()
#    name  height (inches)  age (years)  siblings (not including you)
# 0   NaN               67           23                             1


########################################################################
# 4. QUAR(N)TILES, RANGE, INTER-QUARTILE RANGE

# • Median splits the data set into two equal groups
# • Quartiles split the data into four equal groups

# MIN           (0% point)
# 1ST QUARTILE (25% point)
# 2ND QUARTILE (50% point) = MEDIAN
# 3RD QUARTILE (75% point)
# MAX         (100% point)

print ourdataframe.quantile( q=0 ) # does the same thing as `ourdataframe.min()`
# height (inches)                 61
# age (years)                     22
# siblings (not including you)     0
# dtype: float64

print ourdataframe.quantile( q=.25 )
# quartiles
# height (inches)                 65.00
# age (years)                     24.25
# siblings (not including you)     1.00
# dtype: float64

print ourdataframe.quantile( q=.5 ) # does the same thing as `ourdataframe.median()`
# height (inches)                 66.5
# age (years)                     27.0
# siblings (not including you)     1.0
# dtype: float64

print ourdataframe.quantile( q=.75 )
# height (inches)                 67.537375
# age (years)                     32.000000
# siblings (not including you)     2.000000
# dtype: float64

print ourdataframe.quantile( q=1 ) # does the same thing as `ourdataframe.max()`
# height (inches)                 74
# age (years)                     49
# siblings (not including you)     3
# dtype: float64


# RANGE (0%-100% length)
# • The gap between the minimum value and the maximum value

print ourdataframe['height (inches)'].max() - ourdataframe['height (inches)'].min()
# 13.0


# INTER-QUARTILE RANGE (IQR) (25%-75% length) # (SLIDE57)
# https://community.qlik.com/blogs/qlikviewdesignblog/2014/08/18/recipe-for-a-box-plot

print ourdataframe['height (inches)'].quantile( q=.75 ) - ourdataframe['height (inches)'].quantile( q=.25 )
# 2.5373749999999973


# OUTLIERs are any data points beyond 1.5 IQR # (SLIDE58)


########################################################################
# BOX AND WHISKER PLOT
# whiskers, dots for outliers
# http://flowingdata.com/2008/02/15/how-to-read-and-use-a-box-and-whisker-plot/

ourdataframe.boxplot()
# or perhaps, for a box plot of just one column,
ourdataframe.boxplot( column='height (inches)' )

pyplot.show()


########################################################################
# 5. STANDARD DEVIATION, VARIANCE

# STANDARD DEVIATION

# • The average distance of each data point from the mean
# • Larger the standard deviation, the greater the spread # (SLIDE50)

# real world application: poll of standard deviation +-3 and +-10; you would know that the poll with +-3 standard deviation has less variability

# Formula for standard deviation # (SLIDE50)
# 1. Subtract the mean from each data point
# 2. Square the result
# 3. Sum them together
# 4. Divide by the number of instances (minus 1 if it's a sample NOT the population)
# 5. Take the square root

print ourdataframe.std()
# height (inches)                 3.239595
# age (years)                     7.676495
# siblings (not including you)    1.057850
# dtype: float64

# Useful for comparing across different data sets
# e.g. duration of times when 311 calls are open -- 311 calls, service calls, are made when street lights are out or there's noise or there's a pothole, refers to whatever agency

# normal distributions -- 68-95-99.7 rule # (SLIDE53)
# long-tail distributions -- standard deviation is a little less useful


# VARIANCE

# Calculate the same way you would calculate standard deviation, but don't take the square root at the end
# Usually not in a unit that you can use; can't meaningfully compare the data


########################################################################
########################################################################
# 3:

# One thing we didn't get into was some of the epic fails of statistics. If you all come out of this class managing to avoid these mistakes, I will be proud:
# http://simplystatistics.org/2012/11/26/the-statisticians-at-fox-news-use-classic-and-novel-graphical-techniques-to-lead-with-data/
