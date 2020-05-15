name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

count = dict()
for line in handle:
    if not line.startswith('From '):
        continue
    words = line.split()
    count[words[1]] = count.get(words[1],0)+1
print (count)
bigkey = None
bigcount = None
for aa,bb in count.items():
    if bigkey is None or bb > bigcount:
        bigkey = aa
        bigcount = bb
print(bigkey,bigcount)
