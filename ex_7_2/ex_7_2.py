# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
n = 0
tot = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    n = n + 1
    pos = line.find('0')
    num = float(line[pos:pos+6])
    tot = tot + num
    avg = tot / n
print('Average spam confidence:', avg)
