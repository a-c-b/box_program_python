# box_program_python

## Scope
I'm currently working on an extensive project to hand set 52 poems, or 35,967 characters
and print them using [a platen press](https://en.wikipedia.org/wiki/Letterpress_printing)
to letterpress print a small book of poetry.  For this project I am also constructing
boxes to contain the individual poems as this book will not be a bound book.  People
can choose which poems they'd like to have in the collection.  They can select one poem,
or collect all 52.  Not all poems will be available for printing until the end of 2017.

### Project Description

The first part of the project was to determine how to lay out each "page" of the book.
Each "page" will be a 4x6 hand-cut card of archival paper which is actuall a 2-ply
matboard selected because of its textural qualities and the way it took the printing ink.

The ink is hand mixed.  The artwork is original to me and I have hand-carved the linoblocks
for the prints.  The edition size will be limited to 50 copies of boxes and poems then the
form will be dismantled, the type put away and the edition will be dead.  

I am using python to help me some of the design / engineering decisions.  I am in the process
of learning the language, so felt that addressing some of the questions and tasks using 
python would be a fun way to incorporate my learning and challenge myself.  This also gives me 
continued opportunity to work with version control, github, and updating my portfolio.

##19Oct2015 - Program descriptions:

#### [boxsize2.py](https://github.com/andrea345/box_program_python/blob/master/boxsize2.py):
The function of boxsize2.py is to do fractional math for me.  I'm also working with data type conversions,
definition syntax, looping, and inputs.

There are now two box types which are spec'd out in this little program.  One is a fold over box, and
the second is a lidded one.  The program is supposed to add the slop factors to the values for me
as well as work with decimal to fractional (& vv) conversions because I don't know the decimal equivalent
of 5/16" of an inch.  The program also spits out where to make my cut marks on a piece of paper.

####[boxNCards.py](https://github.com/andrea345/box_program_python/blob/master/boxNcards.py)
This is my inventory data entry program.  Its function is to capture the title, the number of words,
characters, the longest line words & characters, and the number of lines in the poem.  It then calculates
the expected length and width of the poem when using an [8point Spartan Medium](https://books.google.com/books?id=eTJ8khmZie0C&pg=PA440&lpg=PA440&dq=8+point+spartan+medium+type&source=bl&ots=g7Fk_1NrzY&sig=QWEwfwPjog7_JtAEJV2PDsCrgtE&hl=en&sa=X&ved=0CB0Q6AEwAGoVChMIj5S75b3PyAIVyC2ICh2zhQEc#v=onepage&q=8%20point%20spartan%20medium%20type&f=false)
font.  It also calculates the expected amount of time to hand-set the type for the body of the poem.
This stands at a little over 246 hours of typesetting.

I calculated the number of cards required to support the book of poetry from the inch-lengths of the various
poems.  Once the number of cards was known, the thickness of the box could be calculated.  Thus, returning me
to the function of boxsize2.py.  My hope is that in progressing my way through _Learning Python the Hard Way_,
I'll learn to tie the modules together.  I've been working on the book for as of this writing.

## The Results
#### [boxsize2.py](https://github.com/andrea345/box_program_python/blob/master/boxsize2.py) output
```ascii
Do you want to calculate the depth first from the number of cards in the collection (Y/N)?y
How many cards will be in the collection? 60

Your depth of the box will be 1 - '7/8' inches or
in decimal, that would be 1.88 inches


What type of box do you want to make
1.  The folded over box?
2. A box with a lid?
> 2

How deep is the box bottom in decimal? 1.88
How deep is the box top in decimal? 1.88
How wide is the card? 4
How long is the card? 6

Now, how much extra space do you want on the width in fractions? 1/8
How much extra space do you want on the length in fractions? 1/8
What kind of thickness is your stock + printed paper in fractions? 1/16

So, your box bottom of '1.88' inches deep x '4' inches wide x '6' inches long
will be spec'd at 1.875 inches deep, 4.125 inches wide, 6.125 inches long
or 1-'7/8' deep, 4-'1/8' wide, 6-'1/8' long

The top will have '1/10' of an inch clearance built in for the cardstock thickness.

For each box the bottom:
1 rectangle at:
b = 4 - '1/8' inches wide by c = 6 - '1/8' inches
2 rectangles at:
a = 1 - '7/8' inches wide by b = 4 - '1/8' inches
2 rectangles at:
a = 1 - '7/8' inches wide by c = 6 - '1/8' inches

For each box the top:
1 rectangle at:
b = 4 - '2/9' inches wide by c = 6 - '2/9' inches
2 rectangles at:
a = 1 - '7/8' inches wide by b = 4 - '2/9' inches
2 rectangles at:
a = 1 - '7/8' inches wide by c = 6 - '2/9' inches

Do another (y/n)? y
What type of box do you want to make
1.  The folded over box?
2. A box with a lid?
> 1

How deep is the box in decimal? 1.88
How wide is the card? 4
How long is the card? 6

Now, how much extra space do you want on the width in fractions? 1/8
How much extra space do you want on the length in fractions? 1/8

So, your box of '1.88' inches deep x '4' inches wide x '6' inches long
will be spec'd at 1.875 inches deep, 4.125 inches wide, 6.125 inches long
or 1-'7/8' deep, 4-'1/8' wide, 6-'1/8' long



Width of stock = - 9 - '7/8' inches:
Length of stock = 13 - '7/8' inches
The card stock would need to be '9-7/8' inches wide by '13-7/8' inches long.

a = 1.875 or 1 - '7/8' inches
b = 4.125 or 4 - '1/8' inches
c = 6.125 or 6 - '1/8' inches

Your marks along the length(left to right) will be: a = 1.875, b = 6.000, a = 7.875, b = 12.000, a = 13.875
Your marks along the width (top to bottom) will be: a = 1.875, c = 8.000, a = 9.875


Your marks along the length(left to right) will be: a = 1-'7/8', b = 6-'0', a = 7-'7/8', b = 12-'0', a = 13-'7/8'
Your marks along the width (top to bottom) will be: a = 1-'7/8', c = 8-'0', a = 9-'7/8'


Do another (y/n)? n
```


#### [boxNcards.py](https://github.com/andrea345/box_program_python/blob/master/boxNcards.py) output
```ascii
Which file do you want to use for input?
> poem.txt
Filename 'poem.txt'.
If you don't want that, hit CTRL-C (^C).
If you do want that, hit RETURN.
?
Opening the file...





What is the title of the poem? The Visit
What are the total number of words in the piece? 268
What are the total number of characters in the piece? 1500
How many words are in the longest line? 12
How many characters are in the longest line? 62
How many lines in the poem? 38



The poem will be 5.28 inches long.
The max width of the poem with be 2.48 inches wide.
The expected amount of time for basic typesetting will be 9.57 hours, or 574.29 minutes.



The list is:  ['The Visit', '268', '1500', '12', '62', '38', '5.28', '2.48', '574.29', '9.57']


Do another (y/n)? y
Input Accepted
What is the title of the poem? Response  to 'Live'
What are the total number of words in the piece? 280
What are the total number of characters in the piece? 1414
How many words are in the longest line? 6
How many characters are in the longest line? 36
How many lines in the poem? 61



The poem will be 8.47 inches long.
The max width of the poem with be 1.44 inches wide.
The expected amount of time for basic typesetting will be 10.00 hours, or 600.00 minutes.



The list is:  ["Response  to 'Live'", '280', '1414', '6', '36', '61', '8.47', '1.44', '600.00', '10.00']


Do another (y/n)? n
Input Accepted
```
#### poems.txt output
```txt
Title, TotWords, TotChar, LLWords, LLChar, NumLines, InchesLong, CharWidth, Min2Set, Hr2Set
The Visit,268,1500,12,62,38,5.28,2.48,574.29,9.57
Response  to 'Live',280,1414,6,36,61,8.47,1.44,600.00,10.00

```

