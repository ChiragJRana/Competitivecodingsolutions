from sys import stdin,stdout
from collections import defaultdict, OrderedDict
import time
import random
def createdict(y,power,k):
    value = defaultdict(list)
    if k:
        for i in range(len(y)-1,0,-1):
            value[y[i]].append(power[i])
        value = OrderedDict(sorted(value.items(),reverse=True))
        return [list(value.keys()),list(value.values())]

    for i in range(len(y)):
        value[y[i]].append(power[i])
    value = OrderedDict(sorted(value.items(),reverse=True))
    return [list(value.keys()),list(value.values())]

# if __name__ == '__main__':
def function(N,y,power,query):
    # N, Q = list(map(int,stdin.readline().split()))
    # y = list(map(int,stdin.readline().split()))
    # power = list(map(int,stdin.readline().split()))
    # for _ in range(Q):
        
    flag = taste = start = end=  0
    # query = list(map(int,stdin.readline().split()))
    value = defaultdict(list)

    if query[0] == 1:
        power[query[1] - 1] = query[2]
        # continue
        return
    if query[1] > query[2]:
    
        for i in range(query[1]-1,query[2]-2,-1):
            value[y[i]].append(power[i])
        # [ value[i].append(j) for i,j in zip(y[query[1]-1,query[2]-2,-1], power[query[1]-1,query[2]-2,-1])]
        value = OrderedDict(sorted(value.items(),reverse=True))

    elif query[1] < query[2]:
        
        for i in range(query[1]-1, query[2]):
            value[y[i]].append(power[i])
        # map(lambda i : value[y[i]].append(power[i]) , range(query[1]-1, query[2]))
        value = OrderedDict(sorted(value.items(),reverse=True))
        # print(value)
    else:
        print(power[query[2] - 1])
        # continue
        return
    y_dict_keys,y_dict_values = [list(value.keys()),list(value.values())]
    start = y[query[1]-1]
    end = y[query[2]-1]
    
    if start != y_dict_keys[0] or len(y_dict_values[0]) > 1 or start == end :
            flag = 1
            # continue
    if not flag:
        for i in range(1,len(y_dict_keys)):
            if y_dict_keys[i] <= end:
                break
            else:
                taste += y_dict_values[i][-1]
                
        taste += power[query[1]-1]
        taste += power[query[2]-1]
        print(taste)
    else:
        print(-1)
    return
        

if __name__=='__main__':
    N = 10
    Q = 10
    # power = [random.choice(range(1,100000000)) for i in range(N)]
    # y = sorted([random.choice(range(1,100000000)) for i in range(N)])
    # query = [[2,random.choice(range(1,int(N/2))), random.choice(range(int(N/2),N+1))] for i in range(Q) ]
    power = [5,13,24,26,25,24,5,6,2,4,52,2,4,2,2]
    y = [5,2,6,7,2,3,5,9,6,2,4,5,3,6,5]
    query = [[2,8,15],[2,8,1],[2,11,13],[2,1,15],[2,4,7]]
    # ans 10, 61, 
    # print(y)
    t1 = time.process_time()
    for i in range(len(query)):
        # if y[query[i][1]-1] == y[query[i][1]]:
        #     y[query[i][1]-1] += 1
        #     print(y[query[i][1]])
        # print(f'''query: {query[i]}''')
        function(N,y,power,query[i])
    t2 = time.process_time()
    print(f'Time :{t2-t1}')
# # 9 2 5 6 7 2 3 4 5 6 7 8 9 10 8 
# 5 13 24 26 25 24 5 6 2 4 52 2 4 2 2 
