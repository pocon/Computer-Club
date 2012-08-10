def fibonnaci(a):
 if (a==1 or a==2):
  return 1 # since the first and second fibonnaci numbers are both defined as 1 (1,1,2,3,5,8...)
 else:
  return fibonnaci(a-1)+fibonnaci(a-2)

print fibonnaci(input("Find the nth fibonnaci number: "))

# Don't try to follow the function in your head, otherwise your brain will probably explode. Unless you enter some negative number, if you think about it the function will call itself with smaller and smaller values of a until it hits 1 or 2, upon which it returns 1 and all the recursive calls are resolved.
