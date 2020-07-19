from sys import stdin,stdout
from functools import reduce

lmx = 0
k = 1
ans = []
append = ans.append

def filterer(x):
    global lmx
    if lmx < y[x]:
        lmx = y[x]
        if y[x] >= y[start]:
            raise ValueError
        return power[x]
    return 0

N, Q = tuple(map(int,stdin.readline().split()))# 10 ** 5
y = tuple(map(int,stdin.readline().split()))# 10 ** 5
power = list(map(int,stdin.readline().split())) # 10 ** 5
queries = (tuple(map(int,stdin.readline().split())) for x in range(Q)) # 10 ** 5
# print(power)
# print(y)
start = end = 0
for query in queries: # 10 ** 5 = n
    start = query[1]-1
    end = query[2]-1

    if query[0] == 1: 
        power[start] = query[2]
        continue

    if start > end:
        k = 1
    elif start < end:
        k = -1
    else:
        append(power[end])
        continue   
    cost = lmx = 0
    try:
        cost = reduce(lambda x,y : x + y,map(filterer,range(end,start,k))) # 10 ** 10
    except:
        print('ERROR')
        append(-1)
        continue
    print(y[start])
    cost += power[start]
    append(cost)

stdout.write('\n'.join(map(str,ans)))