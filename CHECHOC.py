from sys import stdin, stdout
import math
def main():
    ans = []
    for _ in range(int(stdin.readline())):
        N,M,X,Y = list(map(int,stdin.readline().split()))
        b1 = math.ceil(N*M/2)
        b2 = N*M - b1
        print(b1,b2)
        n1 = min(X,Y)
        n2 = min(Y - n1,X)
        print(n1,n2)
        ans.append(str(max(n1,n2)*b1 + min(n1,n2)*b2))
    stdout.write('\n'.join(ans))
    
if __name__ == '__main__':
    main()