from sys import stdin, stdout

ans = []
def main():
    global ans
    N, K = tuple(map(int,stdin.readline().split()))
    minval = -1
    for val in tuple(map(int,stdin.readline().split())):
        if K % val == 0 and val > minval:
            minval = val
    ans.append(str(minval))
    
if __name__ == '__main__':
    for _ in range(int(input())):
        main()
    stdout.write('\n'.join(ans))