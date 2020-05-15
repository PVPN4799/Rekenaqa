import re
name = input("Enter file:")
if len(name) < 1 : name = "regex_sum_536789.txt"
handle = open(name)

total = 0
for line in handle:
    numb = re.findall('[0-9]+',line)
    for n in numb:
        total = total + int(n)
print(total)
