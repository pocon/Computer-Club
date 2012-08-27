#Bentley Carr
import urllib2
i,o=open("input.txt","r"),open("output.txt","w")
t=i.readlines()
for n in range(0,len(t)) :
    t[n]=t[n].strip()
    t[n]= [t[n],urllib2.urlopen("http://finance.yahoo.com/d/quotes.csv?s="+t[n]+"&f=pj1x").readline().split(",")[1]]
t.sort(key=lambda x:float(x[1][:-1]),reverse=True)
for n in range(0,len(t)):
    o.write(t[n][0]+" - "+t[n][1])
    if n != len(t)-1:
        o.write("\n")
o.close()