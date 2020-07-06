#from sys import stdin,stdout
#T = int(stdin.readline())
#for i in range(T):
	#Solution Option 1
    # ll = int(stdin.readline())
    # max = 0
    # maxnum = []
    # arr = [int(x) for x in stdin.readline().split()]
    # indexval = ll-1                     
    # #for indexval in range(ll-1,0,-1):
    # while(indexval > max):
    #     count = 0
    #     maxval = []
    #     if arr[indexval] in maxnum:
    #         indexval -= 1
    #         continue
    #     for i in range(indexval-1,-1,-1): 
    #         if arr[i] % arr[indexval] == 0:
    #             count += 1
    #             maxval.append(arr[i])
    #             #print(arr[indexval],arr[i],"are the value")
    #     if max < count:
    #         max = count
    #         maxnum = maxval
    #     indexval -= 1
    # print(max)
    
    #Solution option 2
    # ll = int(stdin.readline())
    # max,maxval = 0,0
    # mydict = {0:0}
    # arr = [int(x) for x in stdin.readline().split()]
    # for item in arr:
    #     if (item in mydict) and (mydict[item] > maxval) :
    #         max = item
    #         maxval = mydict[item]
    #     mydict[item] = mydict.get(item,0) + 1
    #     for inte in range(1,int(item/2) + 1):
    #         if item % inte == 0:
    #             mydict[inte] = mydict.get(inte,0) + 1
    #   #  print(mydict,max)
    # print(maxval)
# the accepted Solution
from sys import stdin,stdout
import math
def rootsofnumber(n):
    empt = list()
    for inte in range(1,int(math.sqrt(n)+1)):
        if n % inte == 0:
            empt.append(inte)
            empt.append(int(n/inte))
    if n % (math.sqrt(n)) == 0:
        empt.remove(int(math.sqrt(n)))
    print(empt)
    return empt 

T = int(stdin.readline())
for i in range(T):
    ll = int(stdin.readline())
    arr = list(map(int,stdin.readline().split(" ")))
    mydict = dict()
    max = 0
    for item in arr:
        if item in mydict and mydict[item] > max:
            max = mydict[item]
            print('Enter the number')
        lis = rootsofnumber(item)
        for ite in lis:
            print('ite iterartion ',ite)
            mydict[ite] = mydict.get(ite,0) + 1
    print(max,mydict)    

                
        
    
