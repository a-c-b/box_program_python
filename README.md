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

#### boxsize2.py:
The function of boxsize2.py is to do fractional math for me.  I'm also working with data type conversions,
definition syntax, looping, and inputs.

There are now two box types which are spec'd out in this little program.  One is a fold over box, and
the second is a lidded one.  The program is supposed to add the slop factors to the values for me
as well as work with decimal to fractional (& vv) conversions because I don't know the decimal equivalent
of 5/16" of an inch.  The program also spits out where to make my cut marks on a piece of paper.

####boxNCards.py
This is my inventory data entry program.  Its function is to capture the title, the number of words,
characters, the longest line words & characters, and the number of lines in the poem.  It then calculates
the expected length and width of the poem when using an [8point Spartan Medium](https://books.google.com/books?id=eTJ8khmZie0C&pg=PA440&lpg=PA440&dq=8+point+spartan+medium+type&source=bl&ots=g7Fk_1NrzY&sig=QWEwfwPjog7_JtAEJV2PDsCrgtE&hl=en&sa=X&ved=0CB0Q6AEwAGoVChMIj5S75b3PyAIVyC2ICh2zhQEc#v=onepage&q=8%20point%20spartan%20medium%20type&f=false)
font.  It also calculates the expected amount of time to hand-set the type for the body of the poem.
This stands at a little over 246 hours of typesetting.

I calculated the number of cards required to support the book of poetry from the inch-lengths of the various
poems.  Once the number of cards was known, the thickness of the box could be calculated.  Thus, returning me
to the function of boxsize2.py.  My hope is that in progressing my way through _Learning Python the Hard Way_,
I'll learn to tie the modules together.  I've been working on the book for as of this writing.
