from sys  import stdin , stdout
for t in range(int(stdin.readline())):
    length = int(stdin.readline())
    sum = 1
    desum = 1
    mylist = list(map(int,stdin.readline().split()))
    count = mylist.count(2)
    for i in range(1,count+1):
        sum = sum*i
    try:
        desum = sum / (count*(count-1))
    except ZeroDivisionError:
        print(0)
        continue
    sum = sum / (2*desum)
    print(int(sum))
