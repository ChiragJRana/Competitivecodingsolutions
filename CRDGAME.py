# July 2020 Div 2 
from sys import stdin,stdout
for _ in range(int(input())):
    score_chef = 0
    score_morty = 0
    for turn in range(int(input())):
        chef,morty = list(map(lambda x : sum([int(c) for c in x]), stdin.readline().split()))
        if chef > morty:
            score_chef += 1
        elif morty > chef:
            score_morty += 1
        else:
            score_chef += 1
            score_morty += 1
    if score_chef > score_morty:
        print(0, score_chef)
    elif score_morty > score_chef:
        print(1, score_morty)
    else:
        print(2, score_chef)