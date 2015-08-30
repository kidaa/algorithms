#1. Write a function that takes in a list of numbers
#and outputs the mean of the numbers using the formula for mean. 
#Do this without any built-in functions like sum(), len(), and, 
#of course, mean()
numbers = [1,2,3,4,5,6,7,8,9,0,4,2,5,6,1,3,4,3,2,6]
def i_am_mean(i_am_nothing):
	for number in numbers:
		n = 0
		n += number
	counts = 0
	for number in numbers:
		counts += 1
		return n/counts

print i_am_mean(numbers)

#2. Create your own version of the Mayoral Excuse Machine (http://dnain.fo/1CCHKml) 
#in Python that takes in a name and location, selects and excuse at random and prints and excuse
#(Sorry, Richard, I was late to City Hall to meet you, I had a very rough night and woke up sluggish").
#Use the excuses.csv in the Github repository.
#Extra credit if you print the link to the story as well.

import csv
file_A = open("excuse.csv","rU")
excuse = list(csv.DictReader(file_A))
#print excuse

import random
random_excuse = random.choice(excuse)
#print random_excuse
name = raw_input( "What is your name? " )
location = raw_input("Where you want to go?")
print "Sorry, "+name + ",I was late to " + location +" to meet you,"+random_excuse['excuse']+" (see:"+random_excuse['hyperlink']+")"


# list_A = []
# for i in range(len(excuse)):
#     list_A.append(excuse[i]['excuse'])
# print list_A
# # or
# list_A = []
# for e in excuse:
# 	list_A.append( e['excuse'] )
# print list_A
# # or
# list_A = [ e['excuse']  for e in excuse ]
# print list_A
#Above three are the same


#3. Modify the code below(in Exercise3.ipynb) that prints every prime number between 1
#and 100 to only print every other prime number. Extra credit if you can modify the
#code to speed it up.


#a) The following code will print the prime numbers between 1 and 100. 
#Modify the code so it prints every other prime number from 1 to 100
count = 1
for num in range(1,101): 
    prime = True 
    for i in range(2,num): 
        if (num % i == 0): 
            prime = False 
    if prime: 
    	count += 1
    	if (count%2 == 0):
        	print num


#b) Extra Credit: Can you write a procedure that runs faster than the one above?
noprime = [j for i in range(2, 8) for j in range(i * 2, 101, i)]
prime = [x for x in range(1, 101) if x not in noprime]
print prime
#[1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]



#4. The code in Exercise4.ipynb is meant to search for New York Times articles on 
#gay marriage and look at the mean and median word count, 
#but the code has some problems. Follow the instructions in the 
#notebook to fix the code and submit your fixed code.

# The writer of this code wants to count the mean and median article length for 
# recent articles on gay marriage in the New York Times. 
# This code has several issues, including errors. 
# When they checked their custom functions against the numpy functions, 
# they noticed some discrepancies. 
# Fix the code so it executes properly, retrieves the articles, 
# and outputs the correct result from the custom functions, compared to the numpy functions.
import requests # a better package than urllib2
api_key = "4445753bc497cf8e89b42a2bd7bc5de3:0:72206189"
url = "http://api.nytimes.com/svc/search/v2/articlesearch.json?q=gay+marraige&api-key=4445753bc497cf8e89b42a2bd7bc5de3%3A0%3A72206189"
response = requests.get(url)
data = response.json()
# data['response']['docs'][0]['word_count']
# data['response']['docs'][1]['word_count']
# data['response']['docs'][2]['word_count']
# data['response']['docs'][3]['word_count']
wc_list = []
for i in range(0,len(data['response']['docs'])):
    wc_list.append(data['response']['docs'][i]['word_count'])
print wc_list
#[295, 2676, 2676, 3959]
def my_mean(input_list):
    list_sum = 0
    list_count = 0
    for el in input_list:
        list_sum += el
        list_count += 1
    return list_sum / float(list_count)

def my_median(input_list):
    return sorted(input_list)[len(input_list)/2]

print my_mean(wc_list)
#2401.5
print my_median(wc_list)
#2676
import numpy as np
print np.mean(wc_list)
#2401.5
print int(np.median(wc_list))
#2676


#5. Watch this video on how Yelp determines whether to recommend a review:
#https://youtu.be/PniMEnM89iY
#Based on the video, think about the features necessary for the algorithm to dtermine
#whether to recommend a review and write a short blogpost on the class
#Tumblr discussing what features you think Yelp is using and how they might 
#quantifying what they are trying to measure









