import json
import ast


map_file = open('map.txt', 'rb').read()
data = json.loads(map_file)
coor = list(data.keys())


grid_start = 0
grid_end = 70
for i in coor:
    res = ast.literal_eval(i)

y = []
for i in range(0, grid_end):
    x = []
    for c in range(0, grid_end):
        x.append(0)
    y.append(x)


# print(y)

for i in coor:
    res = ast.literal_eval(i)
    y[res[0]][res[1]] = 1
    

for i in y:
    print(i)
    