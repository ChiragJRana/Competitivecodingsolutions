from sys import stdin, stdout
l1 = []
l2 = []
for i in range(5):
    print(l1,l2)
    l1.append(stdin.read(1))
    stdin.read(1)
    l2.append(stdin.read(1))
    stdin.read(1)

print(l1,l2)