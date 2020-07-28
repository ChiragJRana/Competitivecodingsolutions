from sys import stdin, stdout
import numpy as np

def main():
    ans = []
    for _ in range(int(stdin.readline())):
        N, X = list(map(int,stdin.readline().split()))
        array = np.array(list(map(int,stdin.readline().split())))
        # matrix = array + array.T
        count = 0
        adsum = 0
        sumval = 0
        # print(matrix)
        valid = list(filter(lambda x: (X/x).is_integer() ,range(1,N+1)))
        print(valid)
        for length in valid:
            sumval = np.sum(array[:length])
            for j in range(N-length+1):
                adsum = np.sum(array[:length])
                for k in range(N-length + 1):
                    # print("sum",(sumval + adsum)*length)
                    if (sumval + adsum)*length == X:
                        count += 1
                    if k+length != N:
                        adsum += array[k+length] - array[k]
                if j+length != N:
                    sumval += array[j+length] - array[j]
        ans.append(str(count))
    stdout.write('\n'.join(ans))

if __name__ == '__main__':
    main()


# [[ 2  3  4  2 13]
#  [ 3  4  5  3 14]
#  [ 4  5  6  4 15]
#  [ 2  3  4  2 13]
#  [13 14 15 13 24]]
