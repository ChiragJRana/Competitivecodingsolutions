from sys import stdin, stdout
import math
ans = []
def main():
    
    global ans
    arr = list(input())
    babe = input()

    for i in list(babe):
        arr.pop(arr.index(i))
    arr = ''.join(sorted(arr))
    ptr = ''

    for i in range(len(arr)):
        if arr[i] < babe[0]:
            continue
        if arr[i] == babe[0]:
            ptr = babe + arr[i:]  
            j = i + 1
            while j < len(arr) + 1:
                temp = arr[i:j] + babe + arr[j:]
                if temp < ptr:   
                    ptr = temp
                    j += 1
                else:
                    break
            ptr = arr[:i] + ptr
            break                 
        if arr[i] > babe[0]:
            ptr = arr[:i] + babe + arr[i:]
            break
    if len(ptr) != len(arr) + len(babe):
        ptr = arr + babe
    ans.append(ptr)
    
if __name__ == '__main__':
    for _ in range(int(stdin.readline())):
        main()
    stdout.write('\n'.join(ans))