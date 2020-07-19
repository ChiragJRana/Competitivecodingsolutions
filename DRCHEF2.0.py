from sys import stdin, stdout
# import math
# import random
# def func(N,x,co):
for T in range(int(input())):
    N,x = list(map(int,stdin.readline().split()))
    co = list(map(int,stdin.readline().split()))
    co = sorted(co)
    co_val = [1] * N
    print(co)
    days = 0
    position = 0
    n = 0
    infected = 0
    tempx = 0
    # Find the initial Position
    for i in range(len(co)):
        if co[i] == x:
            position = i+1
            x += x
            break
        elif co[i] > x:
            if i > 0 and 2*co[i-1] >= x:
                x = 2 * co[i-1]
                position = i-1
            else :
                position = i
            break

    # print(position)
    for pos in range(position,N):
        infected = co[pos]
        # print('---------------------------------------------')
        # print(f'infected: {infected} of {co[pos]}, x: {x}, days: {days}')
                
        while True:
            if infected < x :
                # print('Infected are less than cures')
                if co[pos+1] > 2*infected:
                    # print('next infected are more than twice of infected so skip')
                    # print(f'skipped {co[pos]}')
                    co_val[pos] += 1
                    break
                else:
                    # print('Cure this count and move to next')
                    co_val[pos] += 1
                    x = 2*infected
                    break
            else :
                # print('Reduce the values ')
                infected = 2*(infected-x)
                x = 2*x
                co_val[pos] += 1
                
    infected = co[-1]
    while co_val[-1]:
        # print(f'infected: {infected} of {co[-1]}, x: {x}, days: {days}')
        if infected < x:
            break
        co_val[-1] += 1
        infected = 2*(infected -x)
        x = 2*x 
                
            
            
            
            
    print(co_val)
    print(sum(co_val))

# if __name__ == '__main__':
#     for i in range(1):
#         N = 20
#         l1 = [random.choice(range(1, 50)) for _ in range(N)]
#         x  = random.choice(range(1,50))
#         print(f'x:{x}, N : {N}')
#         # print(l1)
#         func(1,4,[43])