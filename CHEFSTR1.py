# July 2020 Div 2 
from functools import reduce
from sys import stdin,stdout
for _ in range(int(input())):
    lisy_len = int(input())
    lisy = list(map(int,stdin.readline().split()))
    count = 0
    for i in range(1,lisy_len):
        count += abs(lisy[i] - lisy[i-1])
    print(count - lisy_len + 1)