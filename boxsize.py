
def WOS(deep, wide, long):
	a = (2*deep) + long 
	b = int(a)
	c = Fraction(Decimal(a - b))
	d = str(c)
	print "Width of stock = - %d - %r inches:" %(b,d) #wide variable goes unused
	return str(b)+"-"+d#(2*deep) + long
	
def LOS(deep, wide, long):
	a = ((3*deep) + (2*wide))
	b = int(a)
	c = Fraction(Decimal (a-b))
	d = str(c)
	print "Length of stock = %d - %r inches" % (b, d)#long variable goes unused
	return str(b)+"-"+d#(3*deep) + (2*wide)

from fractions import Fraction	
from decimal import Decimal


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
#likes = raw_input(prompt)

# call the function and send the dimensionsbox_dim.  Set the return value to a new variable
width_of_stock = WOS(a,b,c)
length_of_stock = LOS(a,b,c)
# width_of_stock = (2*a) + c
# length_of_stock = (3*a) + (2*b)

print "The card stock would need to be %r inches wide by %r inches long.\n" % (width_of_stock, length_of_stock)# change it from %.3f - floating point variable 
print "a = %.3f or %d - %r inches" % (a, int(a),str(d))
print "b = %.3f or %d - %r inches" % (b, int(b), str(e))
print "c = %.3f or %d - %r inches\n" % (c, int(c), str(f))
# print "Fraction of an inch for depth variable a = %r " % d
# print "Fraction of an inch for width variable b = %r" % e
# print "Fraction of an inch for length variable c = %r\n" % f

#long side positions
pos2 = a+b 
pos3 = a+b+a 
pos4 = a+b+a+b 
pos5 = a+b+a+b+a
#short side positions
pos6 = a+c
pos7 = a+c+a

g = int(pos2); h = Fraction(Decimal(pos2 - g))
i = int(pos3); j = Fraction(Decimal(pos3 - i))
k = int(pos4); l = Fraction(Decimal(pos4 - k))
m = int(pos5); n = Fraction(Decimal(pos5 - m))

o = int(pos6); p = Fraction(Decimal(pos6 - o))
q = int(pos7); r = Fraction(Decimal(pos7 - q))

# get the fractional values of the decimal results
# d = Fraction(Decimal(a - int(a)))
# e = Fraction(Decimal(b - int(b)))

print "Your marks along the length(left to right) will be: a = %.3f, b = %.3f, a = %.3f, b = %.3f, a = %.3f " % (a,pos2,pos3,pos4,pos5)
print "Your marks along the width (top to bottom) will be: a = %.3f, c = %.3f, a = %.3f  \n\n" % (a,pos6, pos7)

print "Your marks along the length(left to right) will be: a = %r-%r, b = %r-%r, a = %r-%r, b = %r-%r, a = %r-%r " % (int(a), str(d),g, str(h),i,str(j),k,str(l),m,str(n))
print "Your marks along the width (top to bottom) will be: a = %r-%r, c = %r-%r, a = %r-%r  \n\n" % (int(a), str(d),o,str(p),q,str(r))

print o; print p; print

