def o(t):
 if type(t)==type(0):return t
 else:
  r=[]
  while len(t)>0:
   c,m=0,0
   while c<len(t):
    if a(t[c])<a(t[m]):m=c
    c+=1
   r.append(o(t[m]))
   del t[m]
  return r
def a(l,d=0):
 if type(l)==type(0):return l
 else:
  for i in l:
   d+=a(i)
  return d
print o(input("Order a list:"))
