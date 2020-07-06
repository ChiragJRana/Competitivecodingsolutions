from sys import stdin,stdout


if __name__ == '__main__':
    N, Q = list(map(int,stdin.readline().split()))
    y = list(map(int,stdin.readline().split()))
    power = list(map(int,stdin.readline().split()))
    k = 1
    for _ in range(Q):
        flag  = lm = start = end = 0
        query = list(map(int,stdin.readline().split()))
        value = dict()
        if query[0] == 1:
            power[query[1] - 1] = query[2]
            continue
        
        if query[1] > query[2]:
            k = 1
        elif query[1] < query[2]:
            k = -1
        else:
            print(power[query[2] - 1])
            continue
        if max(y[query[2]-1:query[1]-1:k]) >= y[query[1]-1]:
            print(-1)
            continue

        for i in range(query[2]-1,query[1]+k-1,k):
            if lm < y[i] and not y[i] in value:
                lm = y[i]
                value[y[i]] = power[i]
        print(sum(value.values()))
