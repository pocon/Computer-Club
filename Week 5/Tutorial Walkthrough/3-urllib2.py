'''

After learning about modules and files, urllib2 is a bit of a mixture between the two. Check it out here:

http://docs.python.org/library/urllib2

Basically, it allows you to read HTTP Data as you would a file, so you can treat websites a files, more or less.

Here's how it works... (after that, read through urllib2 to see what else you can do but much of it is like with files)

'''

# Source Code Viewer:

import urllib2

page = urllib2.urlopen("http://docs.python.org/library/urllib2") # Specify the web address as the only argument, you can also provide POST data (if you don't know what this is, don't worry, it's not critical)

for line in page.readlines():
    print line


# Voila, you have yourself a Source Code Viewer. Isn't it cool you can interact with the web in the same way you can with local files?
