from sys import stdin,stdout

for test in range(int(stdin.readline())):
    mydict = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
    sum = 0
    for score in range(int(stdin.readline())):
        ch = list(map(int,stdin.readline().split()))
        if ch[0] in mydict and ch[1] > mydict[ch[0]]:
            mydict[ch[0]] = ch[1]
    for k,v in mydict.items():
        sum += v
    print(sum)