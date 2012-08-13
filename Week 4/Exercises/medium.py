threshold = input("Hot Threshold: ")
cur_heatwave = 0
max_heatwave = 0

temp = raw_input("Enter Temp: ") # Input will give us an error if you leave it blank

while temp:
    if int(temp) > threshold:
        cur_heatwave +=1
    
    elif cur_heatwave != 0:
        cur_heatwave = 0

    if max_heatwave < cur_heatwave:
        max_heatwave = cur_heatwave

    temp = raw_input("Enter Temp: ")

print "Longest Heatwave: %d" % max_heatwave
