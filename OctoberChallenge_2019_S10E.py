# cook your dish here
from sys import stdin, stdout
t = int(stdin.readline())
for case in range(t):
    leng = int(stdin.readline())
    arr = [int(x) for x in stdin.readline().split()]
    minval = arr[0]
    ans = 1
    for item in arr[1:5]:
        if item < minval :
            minval = item
            ans += 1
    for i in range(5,leng):
        if arr[i] < min(arr[i-5:i]):
            ans += 1
    print(ans)
