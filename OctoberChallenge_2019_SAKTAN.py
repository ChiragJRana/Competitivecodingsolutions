from sys import stdout, stdin
T = int(stdin.readline())
for i in range(T):
    mydictx = dict()
    mydicty = dict()
    n,m,q = [int(x) for x in stdin.readline().split()]
    for itre in range(q):
        x,y = [int(x) for x in stdin.readline().split()]
        mydictx[x] = mydictx.get(x,0) + 1
        mydicty[y] = mydicty.get(y,0) + 1
    countx = 0
    county = 0
    for k in mydictx:
        if mydictx[k] % 2 == 1:
            countx += 1
            # print(countx)
    for v in mydicty:
        if mydicty[v] % 2 == 1:
            county += 1
            # print(county)
    ans =  m*countx + n*county - 2*countx*county
    print(ans)
    