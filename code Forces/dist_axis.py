from sys import stdin, stdout

ans = []

def main():
    n,k = list(map(int,stdin.readline().split()))
    if n < k:
        ans.append(str(k-n))
    elif int(n&1) == int(k&1):
        ans.append(str(0))
    else:
        ans.append(str(1))
    
if __name__ == '__main__':
    for _ in range(int(stdin.readline())):
        main()
    stdout.write('\n'.join(ans))
