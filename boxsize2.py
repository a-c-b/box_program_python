from fractions import Fraction	
from decimal import Decimal

def depth_calc():
	cc = raw_input("How many cards will be in the collection? ")
	cc = float(cc)		#convert string of card count to a float for division
	a = (cc/10) * float(5)/16	#every 10 cards = 5/16"
	b = int(a)	#get the integer
	c = Fraction(a-b).limit_denominator(10)
	d = str(c)	
	print "\nYour depth of the box will be %d - %r inches or" %(b,d)
	print "in decimal, that would be %.2f inches \n\n" % a

def WOS1(deep, wide, long):
	a = (2*deep) + long 
	b = int(a)
	c = Fraction(a-b).limit_denominator(10)
	d = str(c)
	print "Width of stock = - %d - %r inches:" %(b,d) #wide variable goes unused
	return str(b)+"-"+d#(2*deep) + long
	
def LOS1(deep, wide, long):
	a = ((3*deep) + (2*wide))
	b = int(a)
	c = Fraction(a-b).limit_denominator(10)
	d = str(c)
	print "Length of stock = %d - %r inches" % (b, d)#long variable goes unused
	return str(b)+"-"+d#(3*deep) + (2*wide)

def box1():	
	## dimensions of paper for a folded over box - to include chase marks to make along the paper
	depth = raw_input ("\nHow deep is the box in decimal? ") # a variable
	width = raw_input("How wide is the card? ") #b variable
	length = raw_input("How long is the card? ") #c variable
	slop_width = raw_input("\nNow, how much extra space do you want on the width in fractions? ")
	slop_length = raw_input("How much extra space do you want on the length in fractions? ")

	slop_width = float(Fraction(slop_width).limit_denominator(10))		#asked for the input in fractions.  This converts the fractions to float.
	slop_length = float(Fraction(slop_length).limit_denominator(10))
	a = float(Fraction(depth).limit_denominator(10))
	b = float(Fraction(width).limit_denominator(10))+float(slop_width)
	c = float(Fraction(length).limit_denominator(10))+float(slop_length)
		
	# get the fractional values of the decimal results
	d = Fraction(a - int(a)).limit_denominator(10)
	e = Fraction(b - int(b)).limit_denominator(10)
	f = Fraction(c - int(c)).limit_denominator(10)

	print "\nSo, your box of %r inches deep x %r inches wide x %r inches long " % (depth, width, length)
	print "will be spec'd at %.3f inches deep, %.3f inches wide, %.3f inches long" % (a,b,c) 
	print "or %r-%r deep, %r-%r wide, %r-%r long\n\n\n" % (int(a), str(d), int(b), str(e), int(c), str(f))
	
	# call the function and send the dimensionsbox_dim.  Set the return value to a new variable
	width_of_stock = WOS1(a,b,c)
	length_of_stock = LOS1(a,b,c)

	print "The card stock would need to be %r inches wide by %r inches long.\n" % (width_of_stock, length_of_stock)# change it from %.3f - floating point variable 
	print "a = %.3f or %d - %r inches" % (a, int(a),str(d))
	print "b = %.3f or %d - %r inches" % (b, int(b), str(e))
	print "c = %.3f or %d - %r inches\n" % (c, int(c), str(f))
	
	#long side positions
	pos2 = a+b 
	pos3 = a+b+a 
	pos4 = a+b+a+b 
	pos5 = a+b+a+b+a
	#short side positions
	pos6 = a+c
	pos7 = a+c+a

	#long side mark intervals
	g = int(pos2); h = Fraction(pos2 - g).limit_denominator(10)
	i = int(pos3); j = Fraction(pos3 - i).limit_denominator(10)
	k = int(pos4); l = Fraction(pos4 - k).limit_denominator(10)
	m = int(pos5); n = Fraction(pos5 - m).limit_denominator(10)
	#short side mark intervals
	o = int(pos6); p = Fraction(pos6 - o).limit_denominator(10)
	q = int(pos7); r = Fraction(pos7 - q).limit_denominator(10)

	print "Your marks along the length(left to right) will be: a = %.3f, b = %.3f, a = %.3f, b = %.3f, a = %.3f " % (a,pos2,pos3,pos4,pos5)
	print "Your marks along the width (top to bottom) will be: a = %.3f, c = %.3f, a = %.3f  \n\n" % (a,pos6, pos7)

	print "Your marks along the length(left to right) will be: a = %r-%r, b = %r-%r, a = %r-%r, b = %r-%r, a = %r-%r " % (int(a), str(d),g, str(h),i,str(j),k,str(l),m,str(n))
	print "Your marks along the width (top to bottom) will be: a = %r-%r, c = %r-%r, a = %r-%r  \n\n" % (int(a), str(d),o,str(p),q,str(r))
	#exit(0)	#only use this if you want to exit out of the program

	
def box2():	
	#  Box2 will have a bottom box with a top which slides over the bottom.
	depth = raw_input ("\nHow deep is the box bottom in decimal? ") # a variable
	depth_top = raw_input ("How deep is the box top in decimal? ") # a variable
	width = raw_input("How wide is the card? ") #b variable
	length = raw_input("How long is the card? ") #c variable
	
	slop_width = raw_input("\nNow, how much extra space do you want on the width in fractions? ")
	slop_length = raw_input("How much extra space do you want on the length in fractions? ")
#	slop_top_depth = raw_input("How much extra depth do you want on the top in fractions? ")
	slop_top = raw_input("What kind of thickness is your stock + printed paper in fractions? ") #need to add a slop factor for building the top so it fits over the bottom box
	
	slop_width = float(Fraction(slop_width).limit_denominator(10))
	slop_length = float(Fraction(slop_length).limit_denominator(10))
	slop_top = float(Fraction(slop_top).limit_denominator(10))
	
	a = float(Fraction(depth).limit_denominator(10))
	at = float(Fraction(depth_top).limit_denominator(10))
	b = float(Fraction(width).limit_denominator(10))+float(slop_width)
	bt = float(Fraction(width).limit_denominator(10))+float(slop_width)+float(slop_top)	
	c = float(Fraction(length).limit_denominator(10))+float(slop_length)
	ct =float(Fraction(length).limit_denominator(10))+float(slop_length)+float(slop_top)	
	
	# get the fractional values of the decimal results
	d = Fraction(Decimal(a - int(a))).limit_denominator(10)
	e = Fraction(Decimal(b - int(b))).limit_denominator(10)
	f = Fraction(Decimal(c - int(c))).limit_denominator(10)
	dt = Fraction(Decimal(at - int(at))).limit_denominator(10)
	et = Fraction(Decimal(bt - int(bt))).limit_denominator(10)
	ft = Fraction(Decimal(ct - int(ct))).limit_denominator(10)
	st = Fraction(slop_top).limit_denominator(10)
	

	print "\nSo, your box bottom of %r inches deep x %r inches wide x %r inches long " % (depth, width, length)
	print "will be spec'd at %.3f inches deep, %.3f inches wide, %.3f inches long" % (a,b,c) 
	print "or %r-%r deep, %r-%r wide, %r-%r long\n" % (int(a), str(d), int(b), str(e), int(c), str(f))
	
	print "The top will have %r of an inch clearance built in for the cardstock thickness.\n" %(str(st))
	print "For each box the bottom: "
	print "1 rectangle at: "
	print "b = %d - %r inches wide by c = %d - %r inches " % (int(b), str(e), int(c), str(f))
	print "2 rectangles at: "
	print "a = %d - %r inches wide by b = %d - %r inches " % (int(a), str(d), int(b), str(e))
	print "2 rectangles at: "
	print "a = %d - %r inches wide by c = %d - %r inches\n " % (int(a), str(d), int(c), str(f))	

	print "For each box the top: "
	print "1 rectangle at: "
	print "b = %d - %r inches wide by c = %d - %r inches " % (int(bt), str(et), int(ct), str(ft))
	print "2 rectangles at: "
	print "a = %d - %r inches wide by b = %d - %r inches " % (int(at), str(dt), int(bt), str(et))
	print "2 rectangles at: "
	print "a = %d - %r inches wide by c = %d - %r inches\n " % (int(at), str(dt), int(ct), str(ft))	

	#exit(0)	
	
def boxcalc():
	print "What type of box do you want to make "
	print "1.  The folded over box?"
	print "2. A box with a lid?"
	boxtype = raw_input("> ")
	if boxtype == '1':
		box1()
	elif boxtype == '2':		
		box2()

RA = 1	
d_calc = raw_input("Do you want to calculate the depth first from the number of cards in the collection (Y/N)?")
if d_calc in ['y', 'Y', "yes", "Yes", "YES", "yes"]:
	depth_calc()
while RA == 1:		
	boxcalc()
	RunAgain = raw_input("Do another (y/n)? ")
	if RunAgain in ['y', 'Y', "yes", "Yes", "YES", "yes"]:
		RA = 1
	else:
		RA = 0
	

