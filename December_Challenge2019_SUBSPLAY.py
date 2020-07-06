from sys import stdin,stdout
from collections import defaultdict

for T in range(int(stdin.readline())):
    N = int(stdin.readline())
    tally = defaultdict(list)
    K = N
    for i,item in enumerate(input()):
        tally[item].append(i)
    for item in tally:
        if len(tally[item]) > 1:
            for i in range(len(tally[item])-1):
                temp = tally[item][i+1] - tally[item][i]
                if temp < K:
                    K = temp
    K = N - K
    print(K)
