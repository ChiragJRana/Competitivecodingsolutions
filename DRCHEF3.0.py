from sys import stdin, stdout
co = []
co_val = []
# dumpers = []
# def double(dump):
#     global co_val
#     global co
#     for i in dump:
#         if co_val[i[0]]:
            # co[i[0]] = min(2*co[i[0]],co[1])
for T in range(int(input())):
    N,x = list(map(int,stdin.readline().split()))
    co = list(map(int,stdin.readline().split()))
    co = sorted(co)
    co_val = [1] * N
    # print(co)
    days = 0
    i = 0
    pos = 0
    while co_val[pos]:
        # Dumping of the medicine to the next value
        print(co[pos])
        if co[pos] == x:
            pos += 1
            days += 1
            x += x
            continue
        if x > 0.5*co[pos]:
            print('Dumping on : ',pos)
            k = 0
            while pos != N-1 and x >= 0.5*co[pos+k]:
                k += 1
                print(co[pos], days, x)
            print('Dumping on : ',pos)
            # Now x <= 0.5*co[pos]
            if pos == N-1:
                while x < co[pos]:
                    co[-1] = min(2*(co[-1]-x),co[-1])
                    x = 2*x
                    days += k
                    print(co[pos], days, x)
                days += 1
                break
            else :
                print(co[pos], days, x)
                x += x
                days += 1
            print(co[pos], days, x)
        elif x < 0.5*co[pos]:
            print(co[pos],days)
            x = 2*x
            days += 1
        print(f'value: {co[pos]}, x: {x}, days: {days}')    
        if i == 10:
            break
        i += 1
        

    # print(x)
    print(days)

# if __name__ == '__main__':
#     for i in range(1):
#         N = 20
#         l1 = [random.choice(range(1, 50)) for _ in range(N)]
#         x  = random.choice(range(1,50))
#         print(f'x:{x}, N : {N}')
#         # print(l1)
#         func(N,x,l1)