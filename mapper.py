#!/usr/bin/python
#above line for giving own name to executable

import sys
import string
#c=0			#count how many urls matched the keyword
x=[]			#to get all the "words" in each line, as a list x
#args = (sys.argv) 	#command line arguments
#keyword=str(args[1]) 	# 1st cmd line arg is wiki_search (args[0]), second is keyword
#print(keyword)
#file_name=str(args[2])	
		
for line in sys.stdin:	
	line.strip().split("\n")	
	if line.startswith('MENTION'):
		#print("A mention\n")
		continue
	if line.startswith('URL'):	
		continue
	if line.startswith('TOKEN'):
		x= line.split("\t")
		print '%s\t%s' % (str(x[1]), 1)	#keep count of urls matched
			



