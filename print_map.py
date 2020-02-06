import json
import ast


map_file = open('map.txt', 'rb').read()
data = json.loads(map_file)
coor = list(data.keys())

current_state = json.loads(open('current_state.txt', 'rb') .read())
me = ast.literal_eval(current_state['coordinates'])

grid_start = 0
grid_end = 100
for i in coor:
    res = ast.literal_eval(i)

grid = []
for i in range(0, grid_end):
    x = []
    for c in range(0, grid_end):
        x.append(0)
    grid.append(x)


# print(y)

for i in coor:
    res = ast.literal_eval(i)
    grid[res[1]][res[0]] = 1

grid[me[1]][me[0]] = 5

grid = grid[50:]
for i in grid:
    print(i[50:])
    