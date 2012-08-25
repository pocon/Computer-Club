import urllib2

class Government:
    has_gov = False
    def __init__(self):
        self.update()

    def update(self):
       if urllib2.urlopen("http://doesaustraliahaveagovernmentyet.com").readlines()[37].strip() == '<h1 id="yes">YES</h1>':
           self.has_gov = True
       else:
           self.has_gov = False


g = Government()

if g.has_gov:
    print "Yay! We have a government!"

else:
    print "Ohh, we don't have a government!"
