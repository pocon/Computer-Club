from collections import defaultdict

distribution = defaultdict(int) # default dict just sets up the dictionary with the value specified as default if none is there (here an int, by default 0). More info: http://blog.ludovf.net/python-collections-defaultdict/
phrase = 0

while phrase != '':
    if phrase != 0:
        for word in phrase.split(' '):
            distribution[word.lower()] += 1


    phrase = raw_input("Type A Phrase: ")

print "--> Word Distribution: "
for key in sorted(distribution, key=distribution.get, reverse=True):
    print str(distribution[key]) + "\t" + key 
