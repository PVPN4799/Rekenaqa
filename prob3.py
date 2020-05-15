trials = int(input())
res = list()
for i in range(trials):
    num = int(input())
    line = input()
    lst = line.split()
    nl = list()
    flag = 1
    if(lst[0]<=lst[-1]):
        nl.append(lst[-1])
        nl.append(lst[0])
    else:
        nl.append(lst[0])
        nl.append(lst[-1])
    lst = lst[1:-1]
    while len(lst) >= 1:
        if lst[0]<=lst[-1]:
            if lst[-1]<=nl[-1]:
                nl.append(lst[-1])
                lst = lst[0:-1]
            else:
                flag = 0
                break
        else:
            if lst[0]<=nl[-1]:
                nl.append(lst[0])
                lst = lst[1:len(lst)]
            else:
                flag = 0
                break
    if flag == 1: res.append('Yes')
    else: res.append('No')
for i in res:
    print(i)
