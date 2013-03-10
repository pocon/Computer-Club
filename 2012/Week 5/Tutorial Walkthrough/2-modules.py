'''

Modules and the import command

A module is just a collection of related functions grouped together.
You can create your own modules quite easily, but we'll come back to
that at a later date. When you install Python, it comes with many
modules that can be used instead of having to write all the code
yourself, from scratch.

Now, if we want to actually use them, we have to let Python know, so we
tell it to import the module. Note: this should go right at the start
of your file. For example, to import the math module...

'''

import math

'''

So now we can use it. You might have noticed that we've used this module
(as well as sys) before. You should see Week 2's documentation for many
of the functions it includes. I'll just use a few here as examples. Note
that you must tell python where the function you are calling came from,
by using the dot notation of module.function.

'''

import math

print math.sqrt(4) # prints 2.0
print math.sqrt(2) # prints 1.41421356237

print math.log(2, 10) # prints 0.301029995664

print math.factorial(6) # prints 720

# Modules can also hold constants

print math.pi # prints 3.14159265359
print math.e # prints 2.71828182846

'''

There is extensive documentation for all the modules (including math)
at the Python Standard Library (docs.python.org/library). This describes
all the functions and how they can be used, as well as constants.

The modules are quite varied from manipulating dates and times (the
datetime module) to compressing files using 'gzip' (it's a bit like
.zip files). There are also many involving files, extra mathematical
types (like complex numbers, if you know what they are, to cryptographic
services. Unfortunately, quite a few of them require knowledge of objects,
which we'll get to at a later date.

Let's try out datetime. It has a few different objects within it but don't
worry about that for now, all that means for us is that we need to add an
extra part to the dot notation. It's now module.objecttype.function.
One of these objects is the date object. Let's try out a few functions.

'''

import datetime

print datetime.date.today() # This prints today's date in YYYY-MM-DD format.
print datetime.date.today().year # prints the year of today's date
print datetime.date.today().weekday() # prints the weekday where 0 is Monday
					# and 6 is Sunday
print datetime.date(2012, 02, 21) # prints the date of 21 Feb 2012
print datetime.date(2012, 02, 21).weekday() # gives 1 so 21 Feb 2012 was a
						# Tuesday

'''

There are also time objects:

'''

import datetime

print datetime.time(13, 34, 12) # prints 13:34:12 (the time in HH:MM:SS)
				# Note that it uses 24 hour time

'''

There are many other functions and other objects in this class including:
-the datetime object: combining a date and a time
-the timedelta object: representing the difference between two dates,
				time or datetimes.
-the tzinfo object: representing a timezone.

If you want to look up this module in more detail (or any other module),
remember to go to the Python Standard Library - it has every Standard
Module, their objects, their functions and how to use them.
