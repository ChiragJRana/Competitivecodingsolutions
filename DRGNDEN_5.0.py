from sys import stdin,stdout
import random 
import time
def function(N,y,power,query):
# if __name__ == '__main__':
    # N, Q = list(map(int,stdin.readline().split()))
    # y = list(map(int,stdin.readline().split()))
    # power = list(map(int,stdin.readline().split()))
    k = 1
    # for _ in range(Q):
    flag  = lm = start = end = 0
    # query = list(map(int,stdin.readline().split()))
    value = dict()
    if query[0] == 1:
        power[query[1] - 1] = query[2]
        # continue
        return
    if query[1] > query[2]:
        k = 1
    elif query[1] < query[2]:
        k = -1
    else:
        print(power[query[2] - 1])
        # continue
        return
    if max(y[query[2]-1:query[1]-1:k]) >= y[query[1]-1]:
        print(-1)
        # continue
        return

    for i in range(query[2]-1,query[1]+k-1,k):
        if lm < y[i] and not y[i] in value:
            lm = y[i]
            value[y[i]] = power[i]
    print(sum(value.values()))
    return

if __name__=='__main__':
    N = 100
    Q = 100
    power = random.sample(range(1,1000),N)
    y = sorted(random.sample(range(1,1000),N))
    query = [[2,random.choice(range(int(N/2),N+1)), random.choice(range(1,int(N/2)))] for i in range(Q) ]
    # power = [5,13,24,26,25,24,5,6,2,4,52,2,4,2,2]
    # y = [5,2,6,7,2,3,5,9,6,2,4,5,3,6,5]
    # query = [[2,8,15],[2,8,1],[2,11,13],[2,1,15],[2,4,7]]
    # ans 10, 61, 
    print(y)
    t1 = time.process_time()
    for i in range(len(query)):
        # if y[query[i][1]-1] == y[query[i][1]]:
        #     y[query[i][1]-1] += 1
        #     print(y[query[i][1]])
        # print(f'''query: {query[i]}''')
        function(N,y,power,query[i])
    t2 = time.process_time()
    print(f'Time :{t2-t1}')


# FInally got 10 points 