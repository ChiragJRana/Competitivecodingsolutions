# import functools
from sys import stdin,stdout

for T in range(int(input())):
    l,k = list(map(int,stdin.readline().split()))
    listy = list(map(lambda x : int(x) - k,(filter(lambda x : int(x) > k , stdin.readline().split()))))
    print(sum(listy))