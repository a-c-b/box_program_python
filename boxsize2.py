from fractions import Fraction	
from decimal import Decimal

def WOS1(deep, wide, long):
	a = (2*deep) + long 
	b = int(a)
	c = Fraction(Decimal(a - b))
	d = str(c)
	print "Width of stock = - %d - %r inches:" %(b,d) #wide variable goes unused
	return str(b)+"-"+d#(2*deep) + long
	
def LOS1(deep, wide, long):
	a = ((3*deep) + (2*wide))
	b = int(a)
	c = Fraction(Decimal (a-b))
	d = str(c)
	print "Length of stock = %d - %r inches" % (b, d)#long variable goes unused
	return str(b)+"-"+d#(3*deep) + (2*wide)

def box1():	
	## dimensions of paper for a folded over box - to include chase marks to make along the paper
	depth = raw_input ("\nHow deep is the box in fractions? ") # a variable
	width = raw_input("How wide is the card? ") #b variable
	length = raw_input("How long is the card? ") #c variable
	slop_width = raw_input("\nNow, how much extra space do you want on the width in fractions? ")
	slop_length = raw_input("How much extra space do you want on the length in fractions? ")

	slop_width = float(Fraction(slop_width))
	slop_length = float(Fraction(slop_length))
	a = float(Fraction(depth))
	b = float(Fraction(width))+float(slop_width)
	c = float(Fraction(length))+float(slop_length)
	
	# get the fractional values of the decimal results
	d = Fraction(Decimal(a - int(a)))
	e = Fraction(Decimal(b - int(b)))
	f = Fraction(Decimal(c - int(c)))

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
	g = int(pos2); h = Fraction(Decimal(pos2 - g))
	i = int(pos3); j = Fraction(Decimal(pos3 - i))
	k = int(pos4); l = Fraction(Decimal(pos4 - k))
	m = int(pos5); n = Fraction(Decimal(pos5 - m))
	#short side mark intervals
	o = int(pos6); p = Fraction(Decimal(pos6 - o))
	q = int(pos7); r = Fraction(Decimal(pos7 - q))

	print "Your marks along the length(left to right) will be: a = %.3f, b = %.3f, a = %.3f, b = %.3f, a = %.3f " % (a,pos2,pos3,pos4,pos5)
	print "Your marks along the width (top to bottom) will be: a = %.3f, c = %.3f, a = %.3f  \n\n" % (a,pos6, pos7)

	print "Your marks along the length(left to right) will be: a = %r-%r, b = %r-%r, a = %r-%r, b = %r-%r, a = %r-%r " % (int(a), str(d),g, str(h),i,str(j),k,str(l),m,str(n))
	print "Your marks along the width (top to bottom) will be: a = %r-%r, c = %r-%r, a = %r-%r  \n\n" % (int(a), str(d),o,str(p),q,str(r))
	#exit(0)	#only use this if you want to exit out of the program

	
def box2():	
	#  Box2 will have a bottom box with a top which slides over the bottom.
	depth = raw_input ("\nHow deep is the box bottom in fractions? ") # a variable
	depth_top = raw_input ("How deep is the box top in fractions? ") # a variable
	width = raw_input("How wide is the card? ") #b variable
	length = raw_input("How long is the card? ") #c variable
	
	slop_width = raw_input("\nNow, how much extra space do you want on the width in fractions? ")
	slop_length = raw_input("How much extra space do you want on the length in fractions? ")
#	slop_top_depth = raw_input("How much extra depth do you want on the top in fractions? ")
	slop_top = raw_input("What kind of thickness is your stock + printed paper in fractions? ") #need to add a slop factor for building the top so it fits over the bottom box
	
	slop_width = float(Fraction(slop_width))
	slop_length = float(Fraction(slop_length))
	slop_top = float(Fraction(slop_top))
	
	a = float(Fraction(depth))
	at = float(Fraction(depth_top))
	b = float(Fraction(width))+float(slop_width)
	bt = float(Fraction(width))+float(slop_width)+float(slop_top)	
	c = float(Fraction(length))+float(slop_length)
	ct =float(Fraction(length))+float(slop_length)+float(slop_top)	
	
	# get the fractional values of the decimal results
	d = Fraction(Decimal(a - int(a)))
	e = Fraction(Decimal(b - int(b)))
	f = Fraction(Decimal(c - int(c)))
	dt = Fraction(Decimal(at - int(at)))
	et = Fraction(Decimal(bt - int(bt)))
	ft = Fraction(Decimal(ct - int(ct)))
	st = Fraction(slop_top)
	

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
	
def start():
	print "What type of box do you want to make "
	print "1.  The folded over box?"
	print "2. A box with a lid?"
	boxtype = raw_input("> ")

	if boxtype == '1':
		box1()
	elif boxtype == '2':		
		box2()

RA = 1
while RA == 1:		
	start()
	RunAgain = raw_input("Do another (y/n)? ")
	if RunAgain in ['y', 'Y', "yes", "Yes", "YES", "yes"]:
		RA = 1
	else:
		RA = 2
	

