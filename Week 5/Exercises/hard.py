import urllib2

s = raw_input("Stock: ")
print ""

u = urllib2.urlopen("http://finance.yahoo.com/d/quotes.csv?s=" + s + "&f=pj1x")

l = u.readline().split(',')

print "Price: " + l[0]
print "Exchange: " + l[2][:-1] # as Exchange is on the last part of the line, it contains a \n character which leads to incorrect formatting
print "Market Cap: " + l[1]
