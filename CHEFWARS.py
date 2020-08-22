import math
from sys import stdin, stdout
def main():
    ans = list()
    for _ in range(int(stdin.readline())):
        H, P = list(map(int,stdin.readline().split()))
        # print(H,P)
        while P > 0 and H > 0:
            H -= P
            P -= math.ceil(P/2)
        if H > 0 :
            ans.append(0)
        else:
            ans.append(1)
        # print(ans)
    stdout.write('\n'.join(map(str,ans)))




if __name__ == '__main__':
    main()