from sys import stdin, stdout
import math
import random
def func(N,x,co):
# for T in range(int(input())):
    # N,x = list(map(int,stdin.readline().split()))
    # co = list(map(int,stdin.readline().split()))
    co = sorted(co)
    co_val = [1] * N
    print(co)
    days = 0
    position = 0
    n = 0
    # Find the initial Position
    for i in range(len(co)):
        if co[i] == x:
            position = i+1
            days += i+1
            x += x
            break
        elif co[i] > x:
            if i > 0 and 2*co[i-1] >= x:
                x = 2 * co[i-1]
            days += i
            position = i
            break
    # print(position)
    for pos in range(position,N):
        while co_val[pos]:
            print(f'value: {co[pos]}, x: {x}, days: {days}')
            if co[pos] <= x:
                co_val[pos] = 0
            days += 1
            x = 2 * min(x,co[pos])
            
    # print(x)
    print(days)

if __name__ == '__main__':
    for i in range(1):
        N = 20
        l1 = [random.choice(range(1, 50)) for _ in range(N)]
        x  = random.choice(range(1,50))
        print(f'x:{x}, N : {N}')
        # print(l1)
        func(N,x,l1)