from sys import stdin, stdout
ans = []
for _ in range(int(input())):
    N = int(input())
    chef = chefu = 0

    # myans = [tuple(map(lambda x : x[0]*x[2]/(x[1] + x[2]),x[0]*x[1]/(x[1] + x[2]) ,tuple(map(int,stdin.readline().split())))) for _ in range(N)]
    myans = (tuple(map(int,stdin.readline().split())) for _ in range(N))
    myfinallist = tuple(map(lambda x : (x[0]*x[2]/(x[1] + x[2]),x[0]*x[1]/(x[1] + x[2])) , ))
    for item in myfinallist:
        chef += item[0]
        chefu += item[1]
    
    ans.append(' '.join((str(chef),str(chefu))))
    print(myfinallist)
stdout.write('\n'.join(ans)) 


