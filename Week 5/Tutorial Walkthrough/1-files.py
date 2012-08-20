# In Python, you can also manipulate files (it's pretty boring when a program can't actually do anything with the main storage space, only play with memory)

# We can use the "open" function to create objects that refer to a file, with the following syntax:

myfile=open("file.txt","w")

# the open object takes two arguments, the first the name of the file (file.txt) and the second what we are doing to it. In this case, "w" means we are opening the file to write to it.

# Note that file.txt must be/will be created in the same directory as your python program

# If file.txt does not exist, it will be created. If it already exists, it will be overwritten with the new file

# We can use the write() method to write to a file object

myfile.write("Random stuff goes here")
myfile.write("More random stuff")
myfile.write("End of random stuff")

myfile.close() # The close() method makes the file available for reading (ie when you've done writing to it)

# calling open() with the second argument as "r" will open the file for reading, allowing you to read data from the file. You will get an error if the file does not exist

myfile=open("file.txt","r")

# the read() method will read and return the entire contents of the file, as a string

stuff=myfile.read()
print stuff

# Note that neither newlines nor spaces are printed, since none of these were written. read() can also take a single integer as an argument specifying how many characters it should read next

# Using the newline escape sequence

myfile=open("file2.txt","w")

# The sequence "\n" is a special representation of a newline character

myfile.write("Random stuff\nCheese\nEnd")

myfile.close()

print open("file2.txt","r").read()

# Notice how we now have new lines

myfile=open("file2.txt","r")

# the readline() method returns all the characters up to and including each new line character

print myfile.readline(),
print myfile.readline(),
print myfile.readline(),

# the readlines() method returns all the lines as a list of strings, representing each line:

myfile=open("file2.txt","r")

print myfile.readlines()

# Note: read(), readline(), and readlines() all return empty strings when they reach the end of the file

# You can also loop through lines in readlines (as it's just a list, really):

myfile = open("file2.txt", "r")

for line in myfile.readlines():
    print line
