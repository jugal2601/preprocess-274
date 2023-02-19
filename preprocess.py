
import string
import sys
from sys import *

def command_line():
	""" This function ensures that the value of mode is inputted correctly, if inputted correctly
		calls the required functions, otherwise exits the function and prints an error message with the
		required format of input"""

	# ensures that if the length of the command line argument is 2, check that the second value of input
	# is as required by the function to work.	
	if len(sys.argv)>=2:
		if sys.argv[1]=="keep-digits":
			s=pre_process()
			x=keep_digits(s)
			remove_stop_words(x)
		elif sys.argv[1]=="keep-stops":
			s=pre_process()
			y=keep_digits(s)
			z=remove_digits(y)
			print(*z)
		elif sys.argv[1]=="keep-symbols":
			s=pre_process()
			w=remove_digits(s)
			remove_stop_words(w)
		# otherwise exists the function and prints the allowed inputs
		else:
			sys.exit("Incorrect value of mode given, allowed format is \"python3.py preprocess.py <keep-digits/keep-stops/keep-symbols>\"")

	# if length is less than 2, call all the functions in the appropriate order.		
	else:
		s=pre_process()
		x=keep_digits(s)
		y=remove_digits(x)
		z=remove_stop_words(y)


			

def pre_process():
	""" This function takes in the input of words from the user and returns it as a list"""
	
	text_01=list(map(str,input().lower().split()))
	return(text_01)

def keep_digits(text_01):
	""" This function takes in a list and ensures that no numbers 
		are removed from the list and also removes all the punctuations from words & numbers. 
		Later appends the new results to another list "text_02" and then returns it"""

	text_02=[]
	# for loop iterating over the list that was inputted to the function 
	# and removing all punctutaions, and then appending the new results to another list
	for i in text_01:
	    result=""
	    for j in i:
	        if j in string.ascii_lowercase or j.isnumeric():
	            result+=j
	    text_02.append(result)
	return(text_02)


def remove_digits(b):
	""" This function takes in a list as an input and removes all the digits that are attached
		 to any words (if any) ex. this function will remove the "8" from "l8r" 
		 but wont remove a number if it is only a number and no other characters.
		 The function then appends the new results to the list "text_03" and then returns it"""

	text_03=[]
	# for loop iterating over the input list to remove the numbers that are attached to any other character
	# and then appends the results to a new list and returns it.
	for k in b:
	    results=""
	    if k.isnumeric()==False:
	        for l in k:
	            if l.isnumeric()==False:
	                results+=l
	        text_03.append(results)
	    else:
	        text_03.append(k)
	return(text_03)

def remove_stop_words(a):
	""" This function takes in a list and checks if the words in the list are stop-words or not,
		if they are, it removes them otherwise appends them to a new list "processed_words" 
		and prints the new list """

	stop_words= ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you",
	"your","yours", "yourself", "yourselves", "he",
	"him", "his", "himself", "she", "her","hers",
	"herself", "it", "its", "itself", "they", "them",
	"their", "theirs","themselves", "what", "which","who",
    "whom", "this", "that", "these", "those","am", "is", "are",
    "was", "were", "be","been", "being", "have", "has", "had","having",
    "do", "does", "did", "doing", "a", "an","the", "and", "but", "if","or",
    "because", "as", "until", "while", "of", "at", "by", "for", "with",
    "about", "against", "between", "into", "through", "during", "before", 
    "after","above", "below", "to", "from", "up", "down", "in", "out", "on",
    "off", "over","under", "again", "further", "then", "once", "here", "there",
    "when", "where","why", "how", "all", "any", "both", "each", "few", "more",
    "most", "other","some", "such", "no", "nor", "not", "only", "own", "same",
	"so", "than","too", "very", "s", "t", "can", "will", "just", "don",
	"should", "now"]
	processed_words=[]
	# for loop iterating over the inputted list to remove all the stop words and 
	# appending and printing all the other words.
	for m in a:
		if m not in stop_words:
			processed_words.append(m)
	print(*processed_words)

if __name__=="__main__":

	command_line()