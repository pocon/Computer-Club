database={"patrick":"d$%^&8dj","tom":"qwertyuiop","garfield":"d3njd8e1","root":"password123"}
user=raw_input("local login: ")
if user in database.keys():
 password=raw_input("Password: ")
 if password in database.values():
  print "Welcome - successfully logged in as "+user
 else:
  print "Error - incorrect password"
else:
 print "Error - Username does not exist"
