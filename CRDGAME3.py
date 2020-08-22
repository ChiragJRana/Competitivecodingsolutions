from sys import stdin, stdout
import math
ans = []
def main():
    global ans
    cc, rr = list(map(lambda x : math.ceil(int(x)/9),stdin.readline().split()))
    if cc < rr:
        ans.append(f'0 {cc}')
    else:
        ans.append(f'1 {rr}')

if __name__ == '__main__':
    for _ in range(int(stdin.readline())):

        main()
    stdout.write('\n'.join(ans))