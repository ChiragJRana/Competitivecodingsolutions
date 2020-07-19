from sys import stdin,stdout

if __name__ == '__main__':
    N, Q = list(map(int,stdin.readline().split()))
    y = list(map(int,stdin.readline().split()))
    power = list(map(int,stdin.readline().split()))
    queries = [list(map(int,stdin.readline().split())) for x in range(Q)]
    k = 1
    ans = []
    # value = dict()
    sub_y = []
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
            sub_y = y[end:start+k:k]
        elif start < end:
            k = -1
            sub_y = y[start:end-k:-k][::-1]
        else:
            append(power[end])
            continue        
        
        for i in range(end,start,k):
            if lmx < y[i] :
                lmx = y[i]
                if y[i] >= y[start+k]:
                    cost = -1
                    break
                cost += power[i]

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