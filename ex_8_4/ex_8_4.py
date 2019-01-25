fname = input('Enter file name:')
fh = open(fname)
#fh = open('romeo.txt')
fr = fh.read()
#print(fr)
split = fr.split()
lst = list()
for line in split:
    #print(line)
    look = lst.count(line)
    if look > 0:
        continue
    else:
        lst.append(line)
lst.sort()
print(lst)
#print(line.rstrip())
