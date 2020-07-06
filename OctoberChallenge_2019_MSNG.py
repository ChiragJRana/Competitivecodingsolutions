from sys import stdin,stdout
def base10(x,y):
    sum = 0
    le = len(y)
    for i in range(le):
        sum += int(y[-i-1])*(x ** i)
    return sum
for t in range(int(stdin.readline())):
    mydict = dict()
    base = 0
    for itr in range(int(stdin.readline())):
        x,y = stdin.readline().split(" ")
        mydict[int(x)] = y
        if int(x) != -1:
            base = int(x)
            number = y[:-1]
    if base != 0:
        print(base10(base,number))
    else:
        