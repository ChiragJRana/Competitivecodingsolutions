from sys import stdin, stdout


def main():
    N = int(input())
    l1 = [0]
    l2 = [0]
    winner = max_val = 0
    litofvalues = [tuple(map(int,stdin.readline().split())) for _ in range(N)]
    for i in range(N):
        l1.append(l1[-1] + litofvalues[i][0])
        l2.append(l2[-1] + litofvalues[i][1])
        if abs(l2[-1] - l1[-1]) > max_val:
            winner = (2,1) [l1[-1] > l2[-1]]
            max_val = abs(l2[-1] - l1[-1])
    print(winner, max_val)
if __name__ == '__main__':
    main()