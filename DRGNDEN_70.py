from sys import stdin,stdout
lmx = 0
def filterer(x):
    global lmx
    if lmx < y[x]:
        lmx = y[x]
        return True
    return False
N, Q = list(map(int,stdin.readline().split()))
y = list(map(int,stdin.readline().split()))
power = list(map(int,stdin.readline().split()))
queries = [list(map(int,stdin.readline().split())) for x in range(Q)]
k = 1
ans = []
append = ans.append
y_values = []
for query in queries:
    lmx = 0
    start = query[1]-1
    end = query[2]-1
    cost = 0      
    if query[0] == 1:
        power[start] = query[2]
        continue
    
    if start > end:
        k = 1
    elif start < end:
        k = -1
    else:
        append(power[end])
        continue   
    if max(y[end:start:k]) >= y[start]:
        append(-1)
        continue
    cost = sum(map(lambda x : power[x],filter(filterer,range(end,start+k,k))))
    
    # if abs(start - end) <= abs(y[start] - y[end]):
        # print('Loop 1 ')
    # for i in range(end,start+k,k):
    #     if lmx < y[i] :
    #         lmx = y[i]
    #         cost += power[i]    
    # else :
    #     print('Loop 2')
    #     print(k , 'K value')
    #     index = sub_y.index
    #     lmx = len(sub_y)
    #     y_values = sorted(list(dict.fromkeys(sub_y)), reverse = True)
    #     print(f'y_values: {y_values}')
    #     for yval in y_values:
    #         print('lmx is ', lmx)
    #         if index(yval) < lmx:
    #             lmx = index(yval)
    #             cost += power[end + k*lmx]
    append(cost)

stdout.write('\n'.join(map(str,ans)))


# Python Performance :: Avoid using Global variable i.e avoid .s rather define a variable outside the for loop and use it
# 15 5
# 5 2 6 7 2 3 5 9 6 2 4 5 3 6 5
# 5 13 24 26 25 24 5 6 2 4 52 2 4 2 2
# 2 8 15
# 2 8 1
# 2 11 13
# 2 1 15
# 2 4 7