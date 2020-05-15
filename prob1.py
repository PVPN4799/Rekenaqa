import re
def minion_game(string):
    stuart = dict()
    kevin = dict()
    list = ['A','E','I','O','U']
    k = len(string)
    t1 = 0
    t2 = 0
    for j in range (k):
        for i in range (j,k):
            st = string[j:i+1]
            grp = re.findall(st,string)
            print(grp)
            if st[0] in list:
                kevin[grp] = kevin.get(grp,0)+1
            else:
                stuart[grp] = stuart.get(grp,0)+1
    print(stuart)
    print(kevin)

tst = input()
minion_game(tst)
