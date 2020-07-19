from sys import stdin, stdout
import math
for T in range(int(input())):
    N,x = list(map(int,stdin.readline().split()))
    co = sorted(list(map(int,stdin.readline().split())))
    infected = co.copy()
    days = 0
    a = 0
    b = 0
    if N > 1:
        for i in range(N-1):
            if infected[i] == x:
                x += x
            elif x > infected[i]:
                a = math.log(infected[i+1]/2*infected[i],2)
                b = math.log(infected[i+1]/x,2)
                if (a.is_integer() and  not b.is_integer()) or (a < 0 and not b < 0)  :
                    x = 2*infected[i]
                elif b.is_integer() or b < 0:
                    pass
                else:
                    na = math.pow(2,math.floor(a))*2*infected[i]
                    nb = math.pow(2,math.floor(b))*x
                    if na < nb:
                        x = 2*infected[i]
            else:
                while x <= 0.5*infected[i]:
                    infected[i] = min(2*(infected[i] - x), co[i])
                    x += x
                    days += 1
                if x == infected[i]:
                    x = 2*infected[i]
                else:
                    infected[i+1] = min(2*min(2*(infected[i+1]-x), co[i+1]), co[i+1])
                    x = 2*infected[i]
                    days += 1
            days += 1
    while x < co[-1]:
        co[-1] = min(2*(co[-1]-x), co[-1])
        x += x
        days += 1
    days += 1

    print(days) 
                    


                    
