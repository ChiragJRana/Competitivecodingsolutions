# from sys import stdin,stdout
# import copy
# if __name__ == '__main__':
#     numrow,numcol,rot = list(map(int,stdin.readline().split()))
    
#     # print(newmat[0][0])
#     givmat = [list(map(int,stdin.readline().split())) for _ in range(numrow)]
#     newmat = copy.deepcopy(givmat)
#     for r in range(numrow):
#         for c in range(numcol):
#             x = min(r,numrow-1-r)
#             y = min(c,numcol-1-c)
#             mini = min(x,y)
#             maxRow = numrow - mini -1
#             maxCol = numcol - mini -1
#             row = r
#             col = c
            
#             newrot = rot % ((maxRow + 2 + maxCol)*2 - 4)
#             # print(newrot)
#             for k in range(newrot):
#                 if row == mini and col < maxCol:
#                     col += 1
#                 elif col == maxCol and row < maxRow:
#                     row += 1
#                 elif row == maxRow and col > mini:
#                     col -= 1
#                 elif col == mini and row > mini:
#                     row -= 1
#             newmat[r][c] = givmat[row][col]
#             # print(givmat)
#             # print(newmat)
#             # print(f'r,c :: {r},{c} and row , col :: {row},{col}')
#     for item in newmat:
#         print(' '.join([str(x) for x in item]))

rows, cols, rotations = [int(x) for x in input().strip().split(" ")]
num_layers = int(min(rows, cols)/2)
layers = [[] for x in range(num_layers)]
data = []
for row in range(rows):
    data.append([int(x) for x in input().strip().split(" ")])

rows -= 1
cols -= 1

for current_layer in range(num_layers):
    i = j = current_layer
    while i < rows-current_layer:
        layers[current_layer].append(data[i][j])
        i += 1
    while j < cols-current_layer:
        layers[current_layer].append(data[i][j])
        j += 1
    while i > current_layer:
        layers[current_layer].append(data[i][j])
        i -= 1
    while j > current_layer:
        layers[current_layer].append(data[i][j])
        j -= 1

new_layers = []
for layer in layers:
    rots = rotations % len(layer)
    new_layers.append(list(layer[-rots:] + layer[:-rots]))

for current_layer in range(num_layers):
    i = j = current_layer
    while i < rows-current_layer:
        data[i][j] = new_layers[current_layer].pop(0)
        i += 1
    while j < cols-current_layer:
        data[i][j] = new_layers[current_layer].pop(0)
        j += 1
    while i > current_layer:
        data[i][j] = new_layers[current_layer].pop(0)
        i -= 1
    while j > current_layer:
        data[i][j] = new_layers[current_layer].pop(0)
        j -= 1  

for row in range(rows+1):
    for col in range(cols+1):
        print(data[row][col], end=" ")
    print()

