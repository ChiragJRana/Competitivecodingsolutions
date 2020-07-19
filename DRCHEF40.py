from sys import stdin, stdout
infected = []
co = []
N = 0
days =0
k = 0
flag = 0
def findanddump(x,j):
    flag = 0
    for i in range(N-1,j,-1):
        if 0.5*infected[i] > x:
            flag = 1
    if not flag:
        infected[N-1] -= x 

def nextday(i):
    global infected
    global co
    for i in range(i,N):
        if infected[i] != co[i]:
            infected[i] = min(2*infected[i], co[i])

for T in range(int(input())):
    N,x = list(map(int,stdin.readline().split()))
    co = sorted(list(map(int,stdin.readline().split())))
    infected = co.copy()
    pos = 0
    days = 0
    while pos != N: # To iterate till the end of the string
        nextday(pos)
        print(infected)
        for i in range(pos,N): # this loop will be broken to update the value of nextdays
            if infected[i] == x:
                print('X is equal')
                days += 1
                pos = i+1
                infected[i] = 0
                x += x
                break
            if infected[i] > x:
                print('Dumping Value')
                if x > 0.5*infected[i]:
                    findanddump(x,i)
                else:
                    infected[i] -= x
                days += 1
                x += x
                break
            if infected[i] < x:
                print('X is Bigger')
                if i != N-1 and 2*infected[i] >= infected[i+1]:
                    x = 2*infected[i]
                if i == N-1:
                    x = 2*infected[i]
                infected[i] = 0
                days += 1
                pos += 1
                break
    print(days)