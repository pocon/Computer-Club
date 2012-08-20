f = open("1-Test_Input.txt", "r+")

for line in f.readlines():
    m = line.split(' ')
    print m[0] + m[1], # comma supresses newline, to make sure there's no extra space between lines
