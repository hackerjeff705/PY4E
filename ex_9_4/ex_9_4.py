name = raw_input("Enter file name: ")

if len(name) < 1 : name = "mbox-short.txt"

handle = open(name)
hst = dict()

for line in handle:
    if not line.startswith("From:") :
        continue
    else :
        words = line.split()
        word = words[1]
        #print(type(word))
        #print(word)
        hst[word] = hst.get(word, 0) + 1
#print(hst)

bigcount = None
bigword = None
for word,count in hst.items():
    if bigcount is None or count > bigcount :
        bigword = word
        bigcount = count

print(bigword, bigcount)
