from sys import stdin,stdout
from collections import defaultdict, OrderedDict
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

if __name__ == '__main__':
    N, Q = list(map(int,stdin.readline().split()))
    y = list(map(int,stdin.readline().split()))
    power = list(map(int,stdin.readline().split()))
    for _ in range(Q):
        
        flag = taste = start = end=  0
        query = list(map(int,stdin.readline().split()))
        
        if query[0] == 1:
            power[query[1] - 1] = query[2]
            continue

        if query[1] > query[2]:
            y_dict_keys,y_dict_values = createdict(y[query[2]-1:query[1]],power[query[2]-1:query[1]],1)
        elif query[2] > query[1]:
            y_dict_keys, y_dict_values = createdict(y[query[1]-1: query[2]],power[query[1]-1:query[2]],0)
        else:
            print(power[query[2] - 1])
            continue
        
        start = y[query[1]-1]
        end = y[query[2]-1]

        print(start, end, "New Value")
        
        if start != y_dict_keys[0] or len(y_dict_values[0]) > 1 :
                print(-1)
                continue
        for i in range(1,len(y_dict_keys)):
            if y_dict_keys[i] <= end:
                break
            else:
                taste += y_dict_values[i][-1]
                
        taste += power[query[1]-1]
        taste += power[query[2]-1]
        
        print(taste)

