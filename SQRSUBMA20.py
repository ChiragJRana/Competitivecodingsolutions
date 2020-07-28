from sys import stdin, stdout
import numpy as np

def main():
    for _ in range(int(stdin.readline())):
        N, X = list(map(int,stdin.readline().split()))
        array = np.array(list(map(int,stdin.readline().split()))).reshape(N,1)
        matrix = array + array.T
        count = 0
        # print(matrix)     
        for length in range(1,N+1):
            for j in range(N-length+1):
                for k in range(N-length + 1):
                    if np.sum(matrix[j:j+length,k:k+length]) == X:
                        count += 1
        print(count)

if __name__ == '__main__':
    main()


# [[ 2  3  4  2 13]
#  [ 3  4  5  3 14]
#  [ 4  5  6  4 15]
#  [ 2  3  4  2 13]
#  [13 14 15 13 24]]
