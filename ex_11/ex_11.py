import re

fname = input("Enter file name: ")

fo = open(fname)
tot = 0

for line in fo:
    split = line.rstrip()
    stuff = re.findall('([0-9]+)', split)
    #for each line find and extract any values
    if not stuff:
        continue
        #if the line does not have any values, ignore this line
    else:
        for word in stuff:
            num = int(word)
            tot = tot + num
            #if the line has values do the following:
            #convert each element into an integer and add this to the total
print(tot)
