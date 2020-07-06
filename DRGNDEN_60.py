from sys import stdin,stdout

if __name__ == '__main__':
    N, Q = list(map(int,stdin.readline().split()))
    y = list(map(int,stdin.readline().split()))
    power = list(map(int,stdin.readline().split()))
    queries = [list(map(int,stdin.readline().split())) for x in range(Q)]
    k = 1
    ans = []
    value = dict()
    append = ans.append
    clear = value.clear
    get = value.get
    
    for query in queries:
        lm = 0
        start = query[1]-1
        end = query[2]-1
        clear()
                
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
        
        for i in range(end,start+k,k):
            if lm < y[i] :
                lm = y[i]
                value[y[i]] = get(y[i],power[i])

        append(sum(value.values()))

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