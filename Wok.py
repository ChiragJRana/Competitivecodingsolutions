from collections import OrderedDict, defaultdict
lisss = [9,9,9,2,4,5,9,6,6,8,2,2,3,3,5,6]
liss = defaultdict(list)
print(liss)
for i,item in enumerate(lisss):
    liss[item].append(i)
liss = OrderedDict(sorted(liss.items(), reverse = True))
print(liss)
print(liss[next(iter(liss))])
print(list(liss.keys()))
print(list(liss.values()))
