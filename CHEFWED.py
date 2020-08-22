from sys import stdin, stdout
import numpy as np
import math
from collections import Counter
from functools import reduce
ans = []
tables = 1

def cut_val_increment(breakcount,start,end,val):
    rv = range(start,end)
    breakcount[rv] += val

def recurrsive_cut(my_arr,K):
    global tables
    print(my_arr)
    # declare the conflict array count
    breakcount = np.zeros(len(my_arr))
    # create a dict of values and count greater than 1
    counter = [x for x in Counter(my_arr).most_common() if x[1] > 1]
    print(counter)
    #calculate the inefficiency
    ineff = sum([x[1] for x in counter])
    print(ineff)
    if ineff > K:
        tables += 1
        # find the optimal break point 
        for item in counter:
            ind = np.where(my_arr == item[0])[0]
            # this will generate the breaking point
            cut_val_increment(breakcount,ind[0],ind[-1],int(item[1]))
        print(breakcount)
        cut_index = np.where(breakcount == np.amax(breakcount))[0][0]
        print(cut_index)
        # return recurrsive_cut(my_arr[:cut_index + 1],K) + recurrsive_cut(my_arr[cut_index+1:],K)
        z =  min(recurrsive_cut(my_arr[:cut_index+1],K) + recurrsive_cut(my_arr[cut_index+1:],K))
        if z > ineff:
            tables -=1
            return ineff
        return z
    else :
        # means this table is set properly in terms of K 
        print(f'passed value: {ineff}')
        return ineff


def main():
    global tables
    tables = 1
    N, K = list(map(int, stdin.readline().split()))
    values = np.array(stdin.readline().split())
    cost = recurrsive_cut(values,K)
    ans.append(str(tables*K + cost))

if __name__ == '__main__':
    for _ in range(int(stdin.readline())):
        main()
    
    print('\n'.join(ans))

# 3
# 5 1
# 5 1 3 3 3
# 5 14
# 1 4 2 4 4
# 5 2
# 3 5 4 5 


# 1
# 11 5
# 5 5 5 5 5 5 5 5 5 5 5 
# creates problems 