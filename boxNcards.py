def numlines(lines):
		i = (float(lines)/18)* 2.5 #every 18 lines in 8 pt = 2.5" long
		print "/nPrinting i now %f2" % i
		return i				#return the number of inches for the poem
		
def charwide(char):
		w = (float(char)/50) * (2+3/16) #every 50 charachters is 2 3/16" wide approx
		return w	#return the widest width expected for a line
		
def typehours(wordz):
	t = (float(wordz)/70)*150 	#it took me 2.5 hours to set 70 words in 8 pt. type.  
	return t 			#return minutes

def Funkshun (RA, book):	#pass the RunAgain variable for the initial run and the file name for the book.
	while RA < 2:
		poem = []		#empty list to capture info
		
		title = raw_input("What is the title of the poem? ") 
		wordz = raw_input("What are the total number of words in the piece? ") 
		char = raw_input("What are the total number of characters in the piece? ")
		LLwordz = raw_input("How many words are in the longest line? ") 
		LLchar = raw_input("How many characters are in the longest line? ") 
		lines = raw_input("How many lines in the poem? ") 
		
		#d = raw_input ("\nHow many cards do you want to calculate? ") 
		
		#convert the string inputs to recognizeable numbers
		lines = lines
		char = int(char)
		wordz = int(wordz)
		LLchar = int(LLchar)
		LLwordz = int(LLwordz)
		
		in_long = numlines(lines)
		LLchar_width = charwide(LLchar)
		time = typehours(wordz)
		timeh = time/60
		#print d
		#in_long = float(in_long)
		
		print "\n %f2 \n" % in_long
		print "The poem will be %.2f inches long." % in_long
		print "The max width of the poem with be %.2f inches wide. "% LLchar_width
		print "The expected amount of time for basic typesetting will be %.2f hours, or %.2f minutes."  % (timeh, time)
		print "\n\n"
		
		# creating string variables so can move the list to a line
		# which will be appended to a file.
		
		wordzs = str(wordz)
		chars = str(char)
		LLwordzs = str(LLwordz)
		LLchars = str(LLchar)
		in_longs = str("%.2f"%in_long)
		LLchar_widths = str("%.2f"%LLchar_width)
		times = str("%.2f"%time)
		timehs = str("%.2f"%timeh)
		liness = str(lines)
		
		poem.append(title)
		poem.append(wordzs)
		poem.append(chars) 
		poem.append(LLwordzs)
		poem.append(LLchars)
		poem.append(liness)
		poem.append(in_longs)
		poem.append(LLchar_widths)
		poem.append(times)
		poem.append(timehs)
		
		print "The list is: ", poem
		print "\n"
		
		linea = ','.join(poem)
		book.write(linea)
		book.write("\n")
		
		RunAgain = raw_input("Do another (y/n)? ")
			
		if RunAgain in ['y', 'Y', "yes", "Yes", "YES", "yes"]:
			RA = 1
		else:
			RA = 2

def AddPoems():
	print "Which file do you want to use for input?" 
	filename = raw_input("> ")
	print "Filename %r." % filename  
	print "If you don't want that, hit CTRL-C (^C)."
	print "If you do want that, hit RETURN."
	raw_input("?")
	print "Opening the file..."
	book = open(filename, 'a+') # open the filename object in write mode
	RA = 1		#variable to track whether to Run the module Again
	print "\n"
	Funkshun(RA, book)	
	book.close()	#close the file

			
		
from fractions import Fraction	
from decimal import Decimal

start



 ##  command to create the empty file:  
 #echo "Title, TotWords, TotChar, LLWords, LLChar, NumLines, InchesLong, CharWidth, Min2Set, Hr2Set" > tmb.txt




