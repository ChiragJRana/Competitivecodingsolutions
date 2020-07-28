from functools import reduce
chirag = 'c h i r a g'
rag = 'i a g'
chirag = chirag.split()
rag = rag.split()
ans = [chirag.pop(chirag.index(i)) for i in rag]
print(ans)
print(chirag)