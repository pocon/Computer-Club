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