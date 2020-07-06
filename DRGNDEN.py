from sys import stdin,stdout
import random
import time
from collections import defaultdict, OrderedDict
def createdict(y,power):
    value = defaultdict(list) 
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
    flag = taste = 0
    sub_y = []
    sub_power = []
    # query = list(map(int,stdin.readline().split()))
    if query[0] == 1:
        power[query[1] - 1] = query[2]
        # continue
        return
    if query[1] > query[2]:
        sub_power = power[query[2]-1:query[1]]
        sub_power.reverse()
        sub_y = y[query[2]-1:query[1]]
        sub_y.reverse()
        [y_dict_keys,y_dict_values] = createdict(sub_y,sub_power)
    elif query[2] > query[1]:
        sub_power = power[query[1]-1:query[2]]
        sub_y = y[query[1]-1: query[2]]
        [y_dict_keys, y_dict_values] = createdict(sub_y,sub_power)
    else:
        flag = 1
        # continue
        # return
    print(f'y_dict_keys: {y_dict_keys}')
    print(f'y_dict_values: {y_dict_values}')
    print(f'sub_y: {sub_y}')
    length = len(sub_y)

    if sub_y[0] != y_dict_keys[0] or len(y_dict_values[0]) > 1 :
            print(f'''
                Center mei value is greater == first
                y_dict_keys[0] = {y_dict_keys[0]}
                first value == {sub_y[0]}
            ''')
            flag = 1
            # continue
            # return
    if not flag :
        for i in range(1,len(y_dict_keys)):
            if y_dict_keys[i] <= sub_y[-1]:
                break
            else:
                taste += y_dict_values[i][-1]
            
    taste += sub_power[0]
    taste += sub_power[-1]
    if flag :
        print(-1)
        # continue
        return
    print(taste)
    return

if __name__=='__main__':
    N = 30
    Q = 1
    power = [random.choice(range(1,10)) for i in range(N)]
    y = [random.choice(range(1,10)) for i in range(N)]
    query = [[2,random.choice(range(1,int(N/2))), random.choice(range(int(N/2),N+1))] for i in range(Q) ]
    # power = [5,13,24,26,25,24,5,6,2,4,52,2,4,2,2]
    # y = [5,2,6,7,2,3,5,9,6,2,4,5,3,6,5]
    # query = [[2,8,15],[2,8,1],[2,11,13],[2,1,15],[2,4,7]]
    print(y)
    for i in range(len(query)):
        # if y[query[i][1]-1] == y[query[i][1]]:
        #     y[query[i][1]-1] += 1
        #     print(y[query[i][1]])
        print(f'''query: {query[i]}''')
        function(N,y,power,query[i])
