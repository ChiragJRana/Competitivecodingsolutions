from sys import stdin,stdout
import random
from collections import OrderedDict
def funct(N,l1,l2):
# for _ in range(int(input())):
    # N = int(input())
    A = {}
    B = {}
    cost = 0
    flag = 0
    A_B = []
    A_B_count = []
    # for item in list(map(int,stdin.readline().split())):
    for item in l1:
        A[item] = A.get(item,0) + 1
        B[item] = 0

    # for item in list(map(int,stdin.readline().split())):
    for item in l2:
        B[item] = B.get(item,0) + 1
        if item not in A.keys():
            A[item] = 0
    A = OrderedDict(sorted(A.items()))
    B = OrderedDict(sorted(B.items()))
    # print(A)
    # print(B)
    for item in A.keys():
        if ((A[item] + B[item]) % 2) != 0:
            flag = 1
            break
        A_B.append(item)
        A_B_count.append(A[item] - B[item]) 
    # print(A_B)
    # print(A_B_count)

    for i in range(len(A_B)):
        # print(A_B)
        # print(A_B_count)
        # print(i, f'Cost:{cost}')
        # print('================================================================')
        if A_B[i] <= 2 * A_B[0]:
            cost += A_B[i] * abs(A_B_count[i]) / 2
            if A_B_count[i] > 0:
                j = len(A_B) - 1
                while A_B_count[i] > 0:
                    # print('First Loop',j)
                    if A_B_count[j] < 0:
                        k = min(A_B_count[i],abs(A_B_count[j]))
                        A_B_count[j] += k
                        A_B_count[i] -= k
                    j -= 1
            elif A_B_count[i] < 0:
                j = len(A_B)-1
                while A_B_count[i] < 0:
                    if A_B_count[j] > 0:
                        k = min(abs(A_B_count[i]),A_B_count[j])
                        A_B_count[j] -= k
                        A_B_count[i] += k
                    j -= 1
        else :
            cost += A_B[0] * abs(A_B_count[i]) / 2
    if not flag:    
        print(int(cost))
    else:
        print(-1)

if __name__ == '__main__':
    for item in range(20):
        N = 200000
        l1 = [random.choice(range(1, 1000000000)) for _ in range(N)]
        l1.extend(l1)
        random.shuffle(l1)
        l2 = l1[N:]
        l1 = l1[:N]
        funct(N,l1,l2)
    # funct(8,[1,2], [1,2])

    # Actual Solution on the codechef site itself