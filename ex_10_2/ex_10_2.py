name = input("Enter file name: ")

if len(name) < 1 : name = "mbox-short.txt"

handle = open(name)
hst = dict()

for line in handle:
    if not line.startswith("X-DSPAM-Processed:") :
        continue
    else :
        words = line.split()
        word = words[4]
        hr = word[:2]
        hst[hr] = hst.get(hr, 0) + 1

#tmp = list()
#for k, v in hst.items() :
    #tmp.append((k, v))
#tmp = sorted(tmp)

#or
tmp = sorted( [ (k,v) for k,v in hst.items() ])

n = len(tmp)
for k, v in tmp[:n] :
    print(k, v)
