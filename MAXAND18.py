
from sys import  stdin, stdout
import numpy as np
for _ in range(int(input())):
    N, K = list(map(int,stdin.readline().split()))
    array = np.array(list(map(int,stdin.readline().split())))
    indexes = []
    index = np.arange(30)
    # print(index)
    # print(array)
    matrix = (((array[:,None] & (1 << np.arange(30)))) > 0).astype(int)
    # print(matrix)
    final_sum = np.sum(matrix, axis=0,keepdims=True) * 2**index
    final_sum = final_sum.tolist()[0]
    # print(final_sum)
    for i in range(K):
        indexes.append(final_sum.index(max(final_sum)) + 1)
        final_sum[indexes[-1]-1]=-1
        # print(final_sum, indexes)
    
    string = ['0']*30
    for i in indexes:
        string[i-1]= '1'
    string.reverse()
    print(int(''.join(string),2))
    