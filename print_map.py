import json
import ast


map_file = open('map.txt', 'rb').read()
data = json.loads(map_file)
coor = list(data.keys())
current_state = json.loads(open('current_state.txt', 'rb') .read())
me = ast.literal_eval(current_state['coordinates'])

current_shop = json.loads(open('shop.txt', 'rb') .read())
shop = ast.literal_eval(current_shop['coordinates'])
# print(shop)

   
        
    

def Reverse(lst): 
    return [ele for ele in reversed(lst)] 

grid_start = 0
grid_end = 100
# for i in coor:
#     res = ast.literal_eval(i)

grid = []
for i in range(0, grid_end):
    x = []
    for c in range(0, grid_end):
        x.append('.')
    grid.append(x)



for i in coor:
    res = ast.literal_eval(i)
    grid[res[1]][res[0]] = '0'

grid[me[1]][me[0]] = '5'
grid[shop[1]][shop[0]] = '4'

grid = Reverse(grid[40:])
for i in grid:
    print(i[40:])

# grid = Reverse(grid[50:])
# for i in grid:
#     print(i[50:])
    
# for i in data:
#     print(data[i]['room_id'])
#     print(data[i]['title'])
#     # print(data[i]['description'])
#     # print(data[i]['items'])
#     # coor= ast.literal_eval(data[i]['coordinates'])
#     # print(coor)
#     print('\n')



