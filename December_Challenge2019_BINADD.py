from sys import stdin, stdout
carry = 0
count = 0
for i in range(int(stdin.readline())):
    count = 0
    carry = 0
    stra = reversed(list(map(int,stdin.readline())))
    strb = reversed(list(map(int,stdin.readline())))
    while len(stra) != len(strb):
        if len(stra) > len(strb):
            strb.append(0)
        else:
            stra.append(0)
    
    for i in range(len(strb)):
        carry += stra[i] + strb[i]
        if carry == 2:
            cur +=1
        else :
            cur = carry/2

        ans = max(ans,cur)    
    print(ans)