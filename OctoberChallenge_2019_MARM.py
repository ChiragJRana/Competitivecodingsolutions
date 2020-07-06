# from sys import stdin,stdout
# T = int(stdin.readline())
# for test in range(T):
#     N,K =[ int(x) for x in stdin.readline().split()]
#     arr = [int(x) for x in stdin.readline().split()]
#     if K > (3*N):
#         K = (K % 3*N) + 3*N
#     for i in range(K):
#         p = i%N
#         arr[p] ^= arr[-(p+1)]
#     print(*arr)

