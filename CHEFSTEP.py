from sys import stdin, stdout

def main():
    ans = []
    for _ in range(int(stdin.readline())):
        N, K = list(map(int, stdin.readline().split()))
        tempans = list(map(lambda x : ('0','1') [int(x) % K == 0],stdin.readline().split()))
        ans.append(''.join(tempans))
    stdout.write('\n'.join(ans))
    
if __name__ == '__main__':
    main()