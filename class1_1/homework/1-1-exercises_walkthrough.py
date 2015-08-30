# 1: exercise 1-1 walkthrough


########################################################################
# 1. Write a function that takes in a list of numbers and outputs the mean of the numbers using the formula for mean. Do this without any built-in functions like sum(), len(), and, of course, mean()


# This is one way of doing it:
def cavemanmean( numberlist ):
	numbersum = 0
	numberlen = 0
	for number in numberlist:
		numbersum += number
		numberlen += 1
	return float( numbersum ) / numberlen

import random
testlist = random.sample( range( 150 ),10 ) # Create a list to pass to the function
print testlist

from numpy import mean
print cavemanmean( testlist ),"should be the same as",mean( testlist ) # Compare with `numpy`'s `mean`


# Things to remember:

# 1. Whenever you can, go through a list only once to save time and space! 
def cavemanmean( numberlist ):
	numbersum = 0
	for number in numberlist: # We're going through the same list twice.
		numbersum += number
	numberlen = 0
	for number in numberlist: # We're going through the same list twice.
		numberlen += 1
	return float( numbersum ) / numberlen
# can just be
def cavemanmean( numberlist ):
	numbersum = 0
	numberlen = 0
	for number in numberlist: # We can go through it just once.
		numbersum += number
		numberlen += 1
	return float( numbersum ) / numberlen


# 2. Beware of INTEGER DIVISION!

# Dividing an integer by an integer only gets you an integer.
print 3/4
# 0

# Dividing when there's at least one float gets you a float.
print 3/4.0
# 0.75
print 3.0/4
# 0.75
print 3.0/4.0
# 0.75

def cavemanmean( numberlist ):
	numbersum = 0
	numberlen = 0
	for number in numberlist:
		numbersum += number
		numberlen += 1
	return numbersum / numberlen # This does integer division, so the return value might NOT be correct
# should be
def cavemanmean( numberlist ):
	numbersum = 0
	numberlen = 0
	for number in numberlist:
		numbersum += number
		numberlen += 1
	return float( numbersum ) / numberlen # To avoid that, you CAST (change the type of) one of the numbers to a float


# 3. Be careful what list you pass to the function to test it!

# For example, the following works ONLY as long as we know we're only going to pass lists created with `range()`
# because in that case we are guaranteed that the last element of the list is the length of the list minus 1.
def cavemanmean_for_ranges( numberlist ):
	numbersum = 0
	for number in numberlist:
		numbersum += number
	return float( numbersum ) / ( numberlist[-1] + 1 )

from random import randrange
testlist = range( randrange( 1,101 ) ) # a list created with `range()`, length varies from 1 to 100
print len( testlist ),"the length of the list"
print testlist[-1],"the last element of the list"

from numpy import mean
print cavemanmean( testlist ),"should be the same as",mean( testlist ) # Compare with `numpy`'s `mean`


# Further improvements:

# 4a. What happens if we pass the function an empty list?

# Sebastian mentioned we could do a try-catch. We haven't seen them in class yet, but it looks something like this:
def cavemanmean( numberlist ):
	try:
		numbersum = 0
		numberlen = 0
		for number in numberlist:
			numbersum += number
			numberlen += 1
		return float( numbersum ) / numberlen
	except Exception,e:
		print e

# We'll get there, but for now you can just do a "ghetto try-catch":
def cavemanmean( numberlist ):
	if numberlist: # Check if `numberlist` is NOT empty
		numbersum = 0
		numberlen = 0
		for number in numberlist:
			numbersum += number
			numberlen += 1
		return float( numbersum ) / numberlen
	else:
		print "List is empty!"
		return


# 4b. What happens if we pass the function an argument that is NOT a list of numbers?
# See try-catch above. We'll cover it eventually.


# Python quirks:

# floating point precision
# Floats in Python aren't what they seem. For example,
print 0.1 + 0.2 # You get 0.30000000000000004
# Because of the approximated way floats are stored, they can be slightly off when we're doing calculations. It's not our fault.

# DYNAMIC TYPING
# In Python, it's just assumed what the variable's value's type is, and we can change a variable's value to another value of a different type.
ourvariable = 0      # `ourvariable` is an integer
ourvariable = "zero" # `ourvariable` is now a string
ourvariable = 0.0    # `ourvariable` is now a float
# In certain other languages, we have to specify what type we want the variable to be and stick with that type.


########################################################################
# 2. Create your own version of the Mayoral Excuse Machine (http://dnain.fo/1CCHKmI) in Python that takes in a name and location, selects an excuse at random and prints an excuse ("Sorry, Richard, I was late to City Hall to meet you, I had a very rough night and woke up sluggish"). Use the "excuses.csv" in the Github repository. Extra credit if you print the link to the story as well.

# This is one way of doing it:
import csv
with open( "excuse.csv","rU" ) as ourfile:
	excuselist = list( csv.DictReader( ourfile ) )

name = raw_input( "Who are you? " )
location = raw_input( "Where were you supposed to meet Mayor de Blasio? " )
import random
excuse = random.choice( excuselist )
print "Sorry, "+name+", I was late to "+location+" to meet you, "+excuse["excuse"]+"\n(see: "+excuse["hyperlink"]+")"


# Opening a file as a CONTEXT MANAGER using `with` (considered "more Pythonic")

# We've opened files before
import csv
ourfile = open( "excuse.csv","rU" )
excuselist = list( csv.DictReader( ourfile ) )
# But actually when we're done with using a file we're supposed to close them, too, so as not to run out of resources (Could happen if we're opening a lot of files) or overwrite or confuse files that we're opening and writing to.
ourfile.close()

# An alternative is to open a file using `with`.
# If we open the file using `with`, we don't have to remember to `.close()` it, because it is guaranteed to automatically close once we're done running the indented code.
import csv
with open( "excuse.csv","rU" ) as ourfile:
	excuselist = list( csv.DictReader( ourfile ) )


# Opening a file in UNIVERSAL NEWLINE MODE

# In a text file, the end of lines are marked with an invisible NEWLINE character. Unfortunately, there's more than one newline character, and different operating systems use different ones:
# old Macs use \r (carriage return)
# Macs     use \n (newline)
# Windows  use \r\n

# When we're opening a file in Python, to tell Python that we want all of these recognized as newline characters, we need to open the file in UNIVERSAL NEWLINE MODE with `'rU'`.
open( "excuse.csv","rU" )

# 'r' means we want to read the file. (If we wanted to write to the file, we'd have 'w' there instead of 'r'.)
# 'U' is for universal newline mode.


# How is a file read?

# A line in a text file looks something like this:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n

# Python puts a pointer to the start of the file
# Goes on until you hit \n (a newline character) at the end of the file
# Moves the pointer down (`next` as in `header = next( ourfile )`)


# Getting input from users

person = raw_input( "Enter your name: " )
# Enter your name: # and you can type in your name
print person
# This prints the name you typed in above


# Randomly selecting an element from the `excuses` list

selector = random.choice( range( 11 ) ) # `selector` is one random element from the list [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
excuse = excuses[selector]['excuse']
url    = excuses[selector]['hyperlink'] 
# can just be
selector = random.randrange( 11 ) # `selector` is one integer 0 or more and less than 11
excuse = excuses[selector]['excuse']
url    = excuses[selector]['hyperlink'] 
# can just be
e = random.choice( excuses ) # `e` is one random element from the list `excuses`
excuse = e['excuse']
url    = e['hyperlink']


########################################################################
# 3. Modify the code below (in Exercise3.ipynb) that prints every prime number between 1 and 100 to only print every other prime number. Extra credit if you can modify the code to speed it up.


for num in range(1,101): # for-loop through the numbers
	prime = True # boolean flag to check the number for being prime
	for i in range(2,num): # for-loop to check for "primeness" by checking for divisors other than 1
		if (num%i==0): # logical test for the number having a divisor other than 1 and itself
			prime = False # if there's a divisor, the boolean value gets flipped to False
	if prime: # if prime is still True after going through all numbers from 1 - 100, then it gets printed
		print num


# This is one way of making it quicker:
from math import sqrt
for num in range(1,101):
	prime = True
	for i in range( 2,int( sqrt( num ) )+1 ): # I mentioned this in lab so I'll mention it here too: If you checked all the numbers from 2 to the square root of `num`, you know there aren't any more divisors, so look no further.
		if (num%i==0):
			prime = False
			break # Once you find a divisor, you know `num` is NOT a prime number, so you don't need to look further. So `break` out of the `for` loop.
	if prime:
		print num


# This is one way of making it print every other prime number:
from math import sqrt
primecount = 0 # 
for num in range(1,101):
	prime = True
	for i in range( 2,int( sqrt( num ) )+1 ):
		if (num%i==0):
			prime = False
			break
	if prime:
		if primecount % 2 == 0: # 
			print num
		primecount += 1 # 

# OR,
# DISadvantage: There are two loops, and it takes up more storage
from math import sqrt
primelist = [] # 
for num in range(1,101):
	prime = True
	for i in range( 2,int( sqrt( num ) )+1 ):
		if (num%i==0):
			prime = False
			break
	if prime:
		primelist.append( num ) # 

for p in primelist[::2]: # 
	print p
# OR,
for i in range( 0,len(primelist),2 ): # 
	print primelist[i]


# Understanding/debugging the original code by printing out something at each step:
for num in range(1,101): # for-loop through the numbers
	print "==========================================================="
	print "'num' is "+str(num)+" here"
	prime = True # boolean flag to check the number for being prime
	print "We assume 'num' is a prime number."
	if num <= 1:
		prime = False
		print "'num' is NOT a prime number because it is less than or equal to 1."
	for i in range(2,num): # for-loop to check for "primeness" by checking for divisors other than 1
		if (num%i==0): # logical test for the number having a divisor other than 1 and itself
			prime = False # if there's a divisor, the boolean value gets flipped to False
			print "'num' is NOT a prime number because it is divisible by "+str(i)+"."
	if prime: # if prime is still True after going through all numbers from 1 - 100, then it gets printed
		print num 
		print "'num' is a prime number."


########################################################################
# 4. The code in Exercise4.ipynb is meant to search for New York Times articles on gay marriage and look at the mean and median word count, but the code has some problems. Follow the instructions in the notebook to fix the code and submit your fixed code.

# The writer of this code wants to count the mean and median article length for recent articles on gay marriage in the New York Times. This code has several issues, including errors. When they checked their custom functions against the numpy functions, they noticed some discrepancies. Fix the code so it executes properly, retrieves the articles, and outputs the correct result from the custom functions, compared to the numpy functions.

## import requests # a better package than urllib2
##
## def my_mean(input_list):
## 	list_sum = 0
## 	list_count = 0
## 	for el in input_list:
## 		list_sum += el
## 		list_count += 1
## 	return list_sum / list_count
##
## def my_median(input_list):
## 	list_length = len(input_list)
## 	return input_list[list_length/2]
##
## api_key = "ffaf60d7d82258e112dd4fb2b5e4e2d6:3:72421680"
## url = "http://api.nytimes.com/svc/search/v2/articlesearch.json?q=gay+marriage&api-key=%s" % API_key
## r = requests.get(url)
## wc_list = []
## for article in r.json()['response']['docs']:
## 	wc_list.append(article['word_count'])
##
## import numpy as np
##
## print my_mean(wc_list)
## print np.mean(wc_list)
##
## print my_median(wc_list)
## print np.median(wc_list)


import requests

def my_mean(input_list):
	list_sum = 0
	list_count = 0
	for el in input_list:
		list_sum += el
		list_count += 1
	return float( list_sum ) / list_count # Avoid integer division!

def my_median(input_list):
	sorted_list = sorted( input_list ) # Sort the list first!
	list_length = len(sorted_list)
	half_length = list_length/2 # Getting the half length first, so we don't have do this over and over
	# If `list_length` is 2, `half_length`   is 1
	#                        `half_length-1` is 0
	# If `list_length` is 3, `half_length`   is 1
	if list_length % 2 == 0: # Split different cases for even and odd lengths!
		return (sorted_list[half_length-1] + sorted_list[half_length] ) / 2.0
	else:
		return sorted_list[half_length]

api_key = "ffaf60d7d82258e112dd4fb2b5e4e2d6:3:72421680"
url = "http://api.nytimes.com/svc/search/v2/articlesearch.json?q=gay+marriage&api-key=%s" % api_key # Watch out for cases! `api_key` and `API_key` are NOT the same. Avoid `NameError: name 'API_key' is not defined`
r = requests.get(url)
wc_list = []
for article in r.json()['response']['docs']:
	wc_list.append( int( article['word_count'] ) ) # Type cast the counts into integers! Avoid `TypeError: cannot perform reduce with flexible type`

import numpy as np

print my_mean(wc_list)
print np.mean(wc_list)

print my_median(wc_list)
print np.median(wc_list)


# Ways of putting strings together:

# STRING INTERPOLATION (considered to be more "Pythonic")
api_key = "ffaf60d7d82258e112dd4fb2b5e4e2d6:3:72421680"
url = "http://api.nytimes.com/svc/search/v2/articlesearch.json?q=gay+marriage&api-key=%s" % api_key

first_name = "Richard"
last_name = "Dunks"
full_name = "%s %s" % ( first_name,last_name ) # `%s`'s are placeholders, and the stuff inside the parentheses are what goes in them
print full_name # Richad Dunks
# We can use `%s` for strings, numbers, pretty much anything.
# We don't really need `%i` or `%r`

# STRING CONCATENATION
first_name = "Richard"
last_name = "Dunks"
full_name = first_name+" "+last_name
print full_name


########################################################################
# 5. Watch this video on how Yelp determines whether to recommend a review:
	# https://youtu.be/PniMEnM89iY
	# Why Does Yelp Recommend Reviews?
# Based on the video, think about the features necessary for the algorithm to determine whether to recommend a review and write a short blogpost on the class Tumblr discussing what features you think Yelp is using and how they might quantifying what they're trying to measure
