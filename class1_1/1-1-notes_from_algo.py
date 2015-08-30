# Algorithms
# July 14, 2015

# https://github.com/datapolitan/lede_algorithms
# http://ledealgorithms.tumblr.com/

# Richard Dunks:
	# richard@datapolitan.com
# Chase Davis:
	# chase.davis@nytimes.com



########################################################################
# For Chase's talk, https://github.com/datapolitan/lede_algorithms/blob/master/class1_1/newsroom_examples.md



########################################################################
# 1: what is an ALGORITHM

# A precise set of instructions required to accomplish a task
# It can be roughly broken down into three components: 
	# 1. Inputs
	# 2. Operation: Each step in the operation must be clearly defined and work the same with any input
	# 3. Output
# recipe analogy ### see slides!
# addition analogy ### see slides!

# Why are they important?
	# accuracy
	# efficiency
# Why are we studying them in this class?



########################################################################
# 2: what is a FUNCTION

# Block of organized, reusable code 
# Ideally performs a single action
# Makes your code more modular
# Don't Repeat Yourself (DRY): If you find yourself repeating the same code sequence, it's time to write a function
# Helps make your code more readable and easier to maintain



# Why are functions important in an algorithms class? 

# Writing a function in Python:
def add( x,y ): # THE THREE ELEMENTS OF AN ALGORITHM: 1.INPUT
# keyword `def`
# function name `add`
# parameter/argument name(s) `x` and `y` (Technically, `x` and `y` are parameters and 5 and 6 below are arguments.) # They represent inputs you pass to the function. 
# colon
	xplusy = x + y # THE THREE ELEMENTS OF AN ALGORITHM: 2.OPERATION
	return xplusy # THE THREE ELEMENTS OF AN ALGORITHM: 3.OUTPUT
# indentation
# keyword `return`
# function result i.e. return value

# Calling a function in Python:
print add( 5,6 ) # 11



# Write a function to calculate the hypotenuse of a right triangle given the two legs

from numpy import sqrt
def calculate_hypotenuse( a,b ):
	return sqrt( a*a + b*b )
# OR,
def calculate_hypotenuse_using_powers( a,b ):
	return ( a**2 + b**2 )**.5

print calculate_hypotenuse( 3,4 )
# 5.0
print calculate_hypotenuse_using_powers( 3,4 )
# 5.0



# Some functions have default values,
# so we can pass different numbers of parameters/arguments to those functions:

print range( 10 ) # We pass 1 parameter/argument.
# You get
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	# This is a list of integers
	# of 0 or more  (a default value of the `range()` function)
	# and less than 10  (a value we passed)
	# being incremented by 1  (a default value of the `range()` function).

print range( 5,10 ) # We pass 2 parameters/arguments.
# You get
# [5, 6, 7, 8, 9]
	# This is a list of integers
	# of 5 or more  (a value we passed)
	# and less than 10  (a value we passed)
	# being incremented by 1  (a default value of the `range()` function).

print range( 5,10,2 ) # We pass 3 parameters/arguments.
# You get
# [5, 7, 9]
	# This is a list of integers
	# of 5 or more  (a value we passed)
	# and less than 10  (a value we passed)
	# being incremented by 2  (a value we passed).

print range()
# gives you an error, because you passed less parameters/arguments than the `range()` function needs.
print range( 5,10,2,300 )
# gives you an error, because you passed more parameters/arguments than the `range()` function needs.



########################################################################
# 3: what is a DATA STRUCTURE

# A DATA STRUCTURE is a way of organizing data in a computer program.
# • The method of organizing data differs across types, allowing for different applications
# • Important to use the right data structure for the proper task

# ALGORITHMs         store data in  DATA STRUCTUREs.
# DATA STRUCTUREs  provide data to  ALGORITHMs.



# 1. LIST
# The most versatile data structure in Python 

# 1-1. A list is mutable
	# - A list's length is changeable
	# - A list's elements are changeable
# 1-2. A list preserves order
# 1-3. A list's elements are accessible by indices; indices are consecutive numbers
# 1-4. A list allows elements of differing types
# 1-5. A list allows elements of UNhashable types
# 1-6. A list allows duplicate elements

# When to use lists:
# • When order matters 
# • When you can look up the value using a simple numerical index 
# • When your data might be changed, removed, or extended 
# • When your data doesn't need to be unique


# We create a list using square brackets `[]`
ourlist = [ 'a','b',[ 1,2,3 ],'a' ]
print ourlist
print type( ourlist ) # <type 'list'>


# We can add an OBJECT to the end of a list
ourlist = [ 'a','b',[ 1,2,3 ],'a' ]
ourlist.append( "new" )
print ourlist # ['a', 'b', [1, 2, 3], 'a', 'new']

# We can add an object at the index we want
ourlist = [ 'a','b',[ 1,2,3 ],'a' ]
ourlist.insert( 2,"new" )
print ourlist # ['a', 'b', 'new', [1, 2, 3], 'a']

# We can extend a list with the elements of another list
# (Effectively, we're adding mupltiple objects to the end of a list.)
ourlist = [ 'a','b',[ 1,2,3 ],'a' ]
ourlist.extend( [ 'x','y',78 ] ) 
print ourlist


# We can remove the last element & return its value
ourlist = [ 'a','b',[ 1,2,3 ],'a' ]
ourpopvalue = ourlist.pop()
print ourlist # ['a', 'b', [1, 2, 3]]
print ourpopvalue # 'a'

# We can remove the element at the index we want & return its value
ourlist = [ 'a','b',[ 1,2,3 ],'a' ]
ourpopvalue = ourlist.pop( 1 )
print ourlist # ['a', [1, 2, 3], 'a']
print ourpopvalue # 'b'

# We can remove the first occurrence of a value (Note that `.remove()` DOESN'T return anything)
ourlist = [ 'a','b',[ 1,2,3 ],'a' ]
ourremovevalue = ourlist.remove( 'a' )
print ourlist # ['b', [1, 2, 3], 'a']
print ourremovevalue # None


# We can sort a list IN PLACE (This modifies the original list)
ourlist = [ 'a','b',[ 1,2,3 ],'a' ]
ourlist.sort()
print ourlist # [[1, 2, 3], 'a', 'a', 'b']

# We can reverse the order of a list in place (This modifies the original list)
ourlist = [ 'a','b',[ 1,2,3 ],'a' ]
ourlist.reverse()
print ourlist # ['a', [1, 2, 3], 'b', 'a']

# We can shuffle a list in place (This modifies the original list)
ourlist = [ 'a','b',[ 1,2,3 ],'a' ]
import random
random.shuffle( ourlist )
print ourlist # ['a', 'a', 'b', [1, 2, 3]] # should be different every time.


# We can count the number of occurrences of value
ourlist = [ 'a','b',[ 1,2,3 ],'a' ]
print ourlist.count( 'a' ) # 2


# We can find the index of the first occurence of a value 
ourlist = [ 'a','b',[ 1,2,3 ],'a' ]
print ourlist.index( 'a' ) # 0



# 2. SET
# Like lists, but with NO duplicate elements

# 2-1. A set is mutable
	# - A set's length is changeable
	# - A set's elements are changeable
# 2-2. A set DOESN'T preserve order
# 2-3. A set's elements are NOT accessible by indices
# 2-4. A set allows elements of differing types
# 2-6. A set DOESN'T allow elements of UNhashable types # e.g. NO lists
# 2-5. A set DOESN'T allow duplicate elements

# It has its advantages:
	# Using the `in` operator with a set is faster than with a list
# e.g.
import time,random
number_list = range( 9999 )
number_set = set( number_list )
a = time.clock()
for i in range( 1000 ):
	random.randrange( 99999 ) in number_list
b = time.clock()
print "1000 random checks on list: ",b-a,"seconds" # I got 0.210752 seconds
a = time.clock()
for i in range( 1000 ):
	random.randrange( 99999 ) in number_set
b = time.clock()
print "1000 random checks on set: ",b-a,"seconds" # I got 0.008604 seconds

# When to use sets:
# • When you only need unique values 
# • When the data types you're working with are relatively basic (hashable)
# • When your data changes 
# • When you need to manipulate your sets mathematically (set supports operations like union, intersection, difference, etc)
# e.g. deduplicating names


# We create a set using the keyword `set` OR curly brackets `{}`
ourset = set( [ "alpha","beta","gamma","delta","epsilon" ] )
# OR,
ourset = { "alpha","beta","gamma","delta","epsilon" } # Python 2.7 or newer
print ourset
print type( ourset ) # <type 'set'>


# 2-3. A set's elements are NOT accessible by indices
## ourset[0] # doesn't work

# 2-5. A set DOESN'T allow duplicate elements
ourlist = [ 1,2,2,3,3,3 ]
ourset = set( ourlist )
print ourlist
print ourset # set([1, 2, 3])


# We can add an element to a set
ourset = set( [ "alpha","beta","gamma","delta","epsilon" ] )
ourset.add( "omega" )
print ourset # set(['epsilon', 'beta', 'delta', 'alpha', 'omega', 'gamma'])


# We can remove an element from a set
ourset = set( [ "alpha","beta","gamma","delta","epsilon" ] )
ourset.remove( "alpha" )
print ourset # set(['epsilon', 'beta', 'gamma', 'delta'])


# We can get the union, intersection, difference, symmetric difference of sets
ourset1 = set( [ 1,2,3 ] )
ourset2 = set( [ 3,4,5 ] )
print ourset1 | ourset2 # set([1, 2, 3, 4, 5])  # 1, 2, 3, 4, 5
print ourset1 & ourset2 # set([3])              #       3      
print ourset1 - ourset2 # set([1, 2])           # 1, 2         
print ourset2 - ourset1 # set([4, 5])           #          4, 5
print ourset1 ^ ourset2 # set([1, 2, 4, 5])     # 1, 2,    4, 5 



# 3. TUPLE
# "Tuple" (as in "quintuple") rhymes with "supple."
# Like an UNchangeable (IMmutable) list

# 3-1. A tuple is IMmutable
	# - A tuple's length is NOT changeable
	# - A tuple's elements are NOT changeable
# 3-2. A tuple preserves order
# 3-3. A tuple's elements are accessible by indices; indices are consecutive numbers
# 3-4. A tuple allows elements of differing types
# 3-6. A tuple allows elements of UNhashable types
# 3-5. A tuple allows duplicate elements

# It has its advantages:
	# (tuples provide better performance because of their IMmutability)
	# - More memory-efficient than a list
	# - Looking up elements is faster

# When to use tuples:
# • When your data doesn't change 
# • When performance is important


# We create a tuple using parentheses `()` OR, well, nothing but the values separated by comma
ourtuple = ( 'a','b',[ 1,2,3 ],'a' )
# OR,
ourtuple = 'a','b',[ 1,2,3 ],'a'
print ourtuple
print type( ourtuple ) # <type 'tuple'>


# 3-1. A tuple is IMmutable
	# - A tuple's length is NOT changeable
	# - A tuple's elements are NOT changeable
## ourtuple.append( "epsilon" ) # AttributeError: 'tuple' object has no attribute 'append'
## ourtuple[0] = "frog emoji" # TypeError: 'tuple' object does not support item assignment

# 3-3. A tuple's elements are accessible by indices; indices are consecutive numbers
print ourtuple[0] # 'alpha'
print ourtuple[-2] # 'gamma'
print ourtuple[1:4] # ('beta', 'gamma', 'delta')



# 4. DICTIONARY

# 4-0. A dictionary stores data as key-value pairs
# 4-1. A dictionary is mutable
	# - A dictionary's length is changeable
	# - A dictionary's values are changeable
# 4-2. A dictionary DOESN'T preserve order
# 4-3. A dictionary's values are accessible by keys; keys can be custom numbers or strings
# 4-4. A dictionary allows values of differing types
# 4-6. A dictionary allows values of UNhashable types
# 4-5. A dictionary DOESN't allow duplicate keys
#      A dictionary allows duplicate values

# When to use a dictionary:
# • When you need to lookup values by a custom key 
# • When you need a fast way to lookup values 
# • When your data needs to be modified


# Dictionary variants:
# `collections.OrderedDict` preserves order
# `collections.defaultdict` is a more flexible implementation for creating a dictionary and adding values


# 4-3. A dictionary's values are accessible by keys; keys can be custom numbers or strings
voweldict = { 1:'a',2:'e',3:'i',4:'o',5:'u' }
print voweldict[2] # 'e'

state_dict = { "NY":"New York" }
print state_dict["NY"] # New York
print state_dict[0] # gives you a KeyError



########################################################################
# 4: exercises



# 1. Write a function that takes in a list of numbers and outputs the mean of the numbers using the formula for mean. Do this without any built-in functions like sum(), len(), and, of course, mean()


# The SCOPE of variables

# The following gives you `NameError: name 'nums' is not defined`:
def somefunction():
	nums = [ 1,2,3,4,5 ]
	return "whatever"
for i in nums:
	print i
# Remember, what happens in a function stays in a function.

# The following works:
nums = [ 1,2,3,4,5 ]
for i in nums:
	print i


# When we're looping, we need to pay attention where a variable is being assigned a value

# We assign the value of `a` OUTside the `for` loop
a = 0
for i in range( 5 ):
	# We assign the value of `b` INside the `for` loop
	b = 0

	# We print the values of `a` and `b`
	print "================================================\nThis is loop "+str(i)
	print "The value of `a` is "+str(a)+" and the value of `b` is "+str(b)+"."
	
	# We increment `a` and `b` by 1
	a += 1
	b += 1

# This prints
# ================================================
# This is loop 0
# The value of `a` is 0 and the value of `b` is 0.
# ================================================
# This is loop 1
# The value of `a` is 1 and the value of `b` is 0.
# ================================================
# This is loop 2
# The value of `a` is 2 and the value of `b` is 0.
# ================================================
# This is loop 3
# The value of `a` is 3 and the value of `b` is 0.
# ================================================
# This is loop 4
# The value of `a` is 4 and the value of `b` is 0.


for i in range( 3 ):
	print "`i` is",i
	for j in range( 3 ):
		print "   `j` is",j
print "`i` is",i
# This prints
# `i` is 0
#    `j` is 0
#    `j` is 1
#    `j` is 2
# `i` is 1
#    `j` is 0
#    `j` is 1
#    `j` is 2
# `i` is 2
#    `j` is 0
#    `j` is 1
#    `j` is 2
# `i` is 2



# 2. Create your own version of the Mayoral Excuse Machine (http://dnain.fo/1CCHKmI) in Python that takes in a name and location, selects an excuse at random and prints an excuse ("Sorry, Richard, I was late to City Hall to meet you, I had a very rough night and woke up sluggish"). Use the "excuses.csv" in the Github repository. Extra credit if you print the link to the story as well.


# Getting input from users

person = raw_input( "Enter your name: " )
# Enter your name: # and you can type in your name
print person
# This prints the name you typed in above


# FILE I/O

# Opening a file in UNIVERSAL NEWLINE MODE

# In a text file, the end of lines are marked with an invisible NEWLINE character. Unfortunately, there's more than one newline character, and different operating systems use different ones:
# old Macs use \r (carriage return)
# Macs     use \n (newline)
# Windows  use \r\n

# When we're opening a file in Python, to tell Python that we want all of these recognized as newline characters, we need to open the file in UNIVERSAL NEWLINE MODE with `'rU'`.
open( "excuse.csv","rU" )


# FILE PATHS

# To avoid confusion, so far we've put our .py files and .csv files in the same folder, and in terminal we always moved to that folder before running a .py file.
# But if the folder we're running Python from and the folder with the .csv file are different, we need to specify the FILE PATH to the .csv file.

# Here's how to tell Python where `excuse.csv` is relative to the folder we're running Python from:

# If the folder with `excuse.csv` is the folder we're running Python from,
# you don't need anything.
open( "excuse.csv","rU" )

# If the folder with `excuse.csv` is the "super-folder" of the folder we're running Python from,
# you need to add `../`.
open( "../excuse.csv","rU" )

# If the folder with `excuse.csv` (Let's say that folder is named "cumberbatch") is a sub-folder of the folder we're running Python from,
# you need to add `cumberbatch/`.
open( "cumberbatch/excuse.csv","rU" )

# You can put these together.
# `../`          means "go up   one folder"
# `cumberbatch/` means "go down one folder named 'cumberbatch'"

# e.g.
open( '../lede_algorithms/class1_1/exercise/excuse.csv','rU' )
# means
# From the folder we're running Python from,
# go up   one folder                                  (../)
# go down one folder named 'lede_algorithms'          (lede_algorithms/)
# go down one folder named 'class1_1'                 (class1_1/)
# go down one folder named 'exercise'                 (exercise/)
# and there we shall find the file named 'excuse.csv' (excuse.csv)


# Opening a file as a CONTEXT MANAGER using `with`

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



# 3. Modify the code below (in Exercise3.ipynb) that prints every prime number between 1 and 100 to only print every other prime number. Extra credit if you can modify the code to speed it up.



# 4. The code in Exercise4.ipynb is meant to search for New York Times articles on gay marriage and look at the mean and median word count, but the code has some problems. Follow the instructions in the notebook to fix the code and submit your fixed code.


# INTEGER DIVISION

# Dividing an integer by an integer only gets you an integer.
print 3/4
# 0

# Dividing an integer by a float (or vice versa) gets you a float.
print 3/4.0
# 0.75
print 3.0/4
# 0.75



# 5. Watch this video on how Yelp determines whether to recommend a review:
	# https://youtu.be/PniMEnM89iY
	# Why Does Yelp Recommend Reviews?
# Based on the video, think about the features necessary for the algorithm to determine whether to recommend a review and write a short blogpost on the class Tumblr discussing what features you think Yelp is using and how they might quantifying what they're trying to measure
