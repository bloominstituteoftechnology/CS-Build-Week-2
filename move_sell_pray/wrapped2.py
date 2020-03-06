import json
from path import my_dict as path
from graph import Graph
g = Graph()
import requests
import sys
import random
from util import Stack, Queue
import copy
import time
import math
import json
from cpu import CPU
from mine import valid_proof, proof_of_work




path_reverse = {}
for i in path:
    path_reverse[i] = {y: x for x, y in path[i].items()}
g.vertices = path_reverse

def cooldown_func(response):
    cooldown = response["cooldown"]
    cooldown_rounded_up = math.ceil(cooldown)
    for i in range(0, cooldown_rounded_up):
        print(f'Remaining cooldown new move: {cooldown_rounded_up - i})', end="\r")
        time.sleep(1)
# curl -X POST -H 'Authorization: Token b9ac3ccda7673a719af4c4305ec9efacdef4c161' -H "Content-Type: application/json" -d '{"name":"nice jacket"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/take/
# curl -X POST -H 'Authorization: Token 6a879ef0d8d6851f96f1d1144cd3836007c07225' -H "Content-Type: application/json" https://lambda-treasure-hunt.herokuapp.com/api/adv/status/
token = 'Token b9ac3ccda7673a719af4c4305ec9efacdef4c161' #6a879ef0d8d6851f96f1d1144cd3836007c07225
token_2 = 'Token 6a879ef0d8d6851f96f1d1144cd3836007c07225'
url = 'https://lambda-treasure-hunt.herokuapp.com'
headers = {
    'Authorization': token,
}
headers_2 = {
    'Authorization': token_2,
}

response = requests.get(url + '/api/adv/init/', headers=headers)
response_2 = requests.get(url + '/api/adv/init/', headers=headers_2).json()

response = response.json()
print(response)
cooldown = response["cooldown"] 
headers = {
    'Authorization': token,
    'Content-Type': 'application/json',
}
moving = True
curr_id = response['room_id']
curr_id_1 = response['room_id']
curr_id_2 = response_2['room_id']
if curr_id_1 > 500:
    wrapped_curr_id_1 = True
else:
    wrapped_curr_id_1 = False
    
if curr_id_2 > 500:
    wrapped_curr_id_2 = True
else:
    wrapped_curr_id_2 = False

cooldown_func(response)

s = Stack()
visited = {curr_id: {}}
curr_room = response
reverse = {'n': 's',
            'e': 'w',
            's': 'n',
            'w': 'e'}
for direction in curr_room['exits']:
    print(direction)
    visited[curr_id][direction] = '?'
for id_in_path in path:
    # print(id_in_path)
    # print(path[id_in_path])
    # print(path_reverse[id_in_path])
    visited[id_in_path] = {}
    # print(visited)
    for direction in path[id_in_path]:
        visited[id_in_path][direction] = '?'
    
    
print(f'Initialize: {visited}\n')
    
traversal_path = []
room_info = {curr_id: curr_room}

def unvisited(graph):
    for i in graph:
        if '?' in graph[i].values():
            return True
    return False

def response_func(what='status'):
    response_status = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/status/', 
                                            headers=headers).json()
    cooldown_func(response_status)
    encumbrance = response_status['encumbrance']
    strength = response_status['strength']
    inventory = response_status['inventory']
    gold = response_status['gold']
    armor = response_status['bodywear']
    shoes = response_status['footwear']
    name = response_status['name']
    abilities = response_status['abilities']
    has_mined = response_status['has_mined']
    
    return encumbrance, strength, inventory, gold, armor, shoes, name, abilities, has_mined

# Get status and update variables
encumbrance, strength, inventory, gold, armor, shoes, name, abilities, has_mined = response_func()
print(f'Name: {name}')


Initial_name = 'User 20677'
shrined = [1,1,1]
# Go to shop function
            
def go_to_pirate(curr_id, pyrate=467, come_back=False):
    """
    parms curr_id: ID of current location
    parms pyrate: ID of shop location
    parms come_back: Boolean, if True goes back to where it started, 
                    False continues from shop
    Return sold, curr_id:  sold: True if it sold any items, curr_id: New location ID
    """
    # find shortest path using Breadth First Search. Returns list of ids [1,4,60]
    traversal_path = g.bfs(curr_id, pyrate)
    i = 0
    temp_list = []
    while i + 1 < len(traversal_path):
        print(traversal_path[i])
        direction = path_reverse[traversal_path[i]][traversal_path[i+1]]        
        data = '{"direction":"' + direction + '", "next_room_id":"' + str(traversal_path[i+1]) + '"}'
        reverse_data = '{"direction":"' + reverse[direction] + '", "next_room_id":"' + str(traversal_path[i]) + '"}'
        temp_list.insert(0,reverse_data)
        next_room = requests.post(url + '/api/adv/fly/', headers=headers, data=data).json()
        i +=1
        cooldown_func(next_room)
    
    data_name = '{"name":"[MALI-BOT]", "confirm":"aye"}'

    response_name = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/change_name/', 
                                  headers=headers, data=data_name).json()
    print(response_name['messages'])
    

    if come_back == True:
        for i in temp_list:
            next_room = requests.post(url + '/api/adv/fly/', headers=headers, data=i).json()
            cooldown_func(next_room)
            
    print("NAME CHANGED ============= Let's Mine!!!\n")
    curr_id = next_room['room_id']
    return pyrate
    
def go_to_shrine(curr_id, shrine=[374,461,22]):
    for ind in range(len(shrined)):
        print(shrined)
        if shrined[ind] == 0:
            sh = shrine[ind]
            
    traversal_path = g.bfs(curr_id, sh)
    
    i = 0
    temp_list = []
    while i + 1 < len(traversal_path):
        print(traversal_path[i])
        direction = path_reverse[traversal_path[i]][traversal_path[i+1]]
        data = '{"direction":"' + direction + '", "next_room_id":"' + str(traversal_path[i+1]) + '"}'
        reverse_data = '{"direction":"' + reverse[direction] + '", "next_room_id":"' + str(traversal_path[i]) + '"}'
        temp_list.insert(0,reverse_data)
        next_room = requests.post(url + '/api/adv/fly/', headers=headers, data=data).json()
        i +=1
        cooldown_func(next_room)
    response_shrine = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/pray/', 
                                                headers=headers).json()
    print('=========Shrined!=================\n')
    cooldown_func(response_shrine)
    shrined[ind] = 1
    print(shrined)
    print(response_shrine)
    curr_id = next_room['room_id']
    return curr_id
import itertools
def dash_fly(curr_id,destination, headers=headers):
    traversal_path = g.bfs(curr_id, destination)
    i = 0
    ids = []
    directions = []
    print(len(traversal_path))
    print(f'traversal_path: {traversal_path}')
    while i + 1 < len(traversal_path):
        # print(traversal_path[i])
        direction = path_reverse[traversal_path[i]][traversal_path[i+1]]
        directions.append(direction)
        ids.append(traversal_path[i+1])
        i += 1
    print(len(ids))
    print(len(directions))
    print('Getting listy')
    listy = [list(v) for g,v in itertools.groupby(directions)]
    print(ids)
    print(listy)
    temp_length = 0
    counter = 0
    for i in range(len(listy)):
        length = len(listy[i])
        temp_length += length
        # print(ids[counter:temp_length])
        ids_str = str(ids[counter:temp_length]).strip('[]').replace(" ", "")
        # print(ids_str)
        direction = listy[i][0]
        print(directions)
        print(direction)
        print(ids_str)
        num_rooms = str(len(ids[counter:temp_length]))
        counter = temp_length
        if length > 1:
            print('DASHING')
            dash_data = '{"direction":"'+ direction +'", "num_rooms":"' + num_rooms + '", "next_room_ids":"' + str(ids_str) + '"}'
            print(dash_data)
            next_room = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/dash/', 
                          headers, data=dash_data).json()
            print(next_room)
            print(f"room: {next_room['room_id']}")
            print(f"Name: {name}")
            cooldown_func(next_room)
        else:
            print('FLYING')
            fly_data = '{"direction":"' + direction + '", "next_room_id":"' + ids_str + '"}'
            next_room = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/fly/', 
                                headers=headers, data=fly_data).json()
            print(f"room: {next_room['room_id']}")
            cooldown_func(next_room)
        
    return destination


def go_to_wishing_well_snitch(curr_id_1, curr_id_2, wishing_well=55, alternative=False):
    new_room_id = dash_fly(curr_id_2, wishing_well, headers=headers_2)

    print('===================== Wishing Well ===================')
    # name_of_well = next_room['Wishing Well']
    snitch_room_copy = ''
    while True:
        data_items = '{"name":"Wishing Well"}'
        response_examin = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/examine/', 
                                                        headers=headers_2, data=data_items).json()
        well_desc = response_examin['description'].split('\n')
        print(f'well_desc: {well_desc}')
        # code = response['description']
        filename = 'wishing_well.txt'
        well_desc.pop()
        well_desc.append('00010011')
        with open(filename, 'w') as f:
            for line in well_desc[2:]:
                f.write(line)
                f.write('\n')
        print('=================== DECODING MESSAGE ====================')
        ls8 = CPU()
        ls8.load(filename)
        snitch_room = ls8.run()
        snitch_room = int(snitch_room.replace(" ",""))
        if snitch_room_copy == snitch_room:
            continue
        f = open("snitch_room.txt","w")
        f.write(str(visited))
        f.close()
        snitch_room_copy = int(snitch_room)
        print('=================== Going to to get snitch ===================')
        snitch_room = dash_fly(curr_id_1, snitch_room, headers=headers)
        
        data = '{"name":"golden snitch"}'
                        
        take_snitch = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/take/', 
                                                headers=headers, data=data).json()


        # cooldown_func(take_snitch)
        print('================ snitch grabbed ===============')
        print(take_snitch)
           
    return snitch_room
    
def force_got_to(curr_id, destination=445):
    
    print('=================== Going to mine ===================')
    mine_room = dash_fly(curr_id, destination)

    message = proof_of_work(headers)
    print(f'Mining message: {message}')
    mine_response = requests.get('https://lambda-treasure-hunt.herokuapp.com/api/bc/get_balance/', 
                                 headers=headers).json()

    print('================ Mined new coin ===============')
    print(mine_response)
    cooldown_func(mine_response)
    return destination

def warp(headers):
    response = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/warp/', headers=headers).json()
    # response_2 = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/warp/', headers=headers_2).json()
    cooldown_func(response)
    curr_id = response['room_id']
    # curr_id = response_2['room_id']
    print(response)
    return curr_id
    


def find_new_move_room(visited, current_room, curr_id_1, curr_id_2, encumbrance, 
                       strength, inventory, gold, armor, shoes, name, 
                       abilities, has_mined, wrapped_curr_id_1, wrapped_curr_id_2):
    sold = False
    
    if wrapped_curr_id_1 == False:
        curr_id_1 = warp(headers)
        wrapped_curr_id_1 = True
    # Wishing Well
    elif wrapped_curr_id_2 == False:
        curr_id_2 = warp(headers_2)
        wrapped_curr_id_2 = True
    elif (wrapped_curr_id_2 == True) & (wrapped_curr_id_1 == True):
        print('========================= Getting that snitch ==================')
        while True:
            curr_id_1, curr_id_2 = go_to_wishing_well_snitch(curr_id_1, curr_id_2, wishing_well=555)
    
        
    if curr_id not in visited:
        for direction in ['n','s','w','e']:
            print(direction)
            visited[curr_id][direction] = '?'
    not_in_path = False
    if curr_id in path:
        known_ids = path[curr_id]
        print(f'known_ids: {known_ids}')
    else:
        not_in_path = True
    room_exits = visited[curr_id]
    print(f'room_exits: {room_exits}\n')
    dirs = []
    for direction in room_exits:
        dirs.append(direction)
    random.shuffle(dirs)
    for direction in dirs:
        if room_exits[direction] == '?':
            
            if not_in_path:
                data = '{"direction":"' + direction + '"}'
            else:
                next_room_id_pred = known_ids[direction]
                print(f'next_room_id_pred: {next_room_id_pred}')
                data = '{"direction":"' + direction + '", "next_room_id":"' + str(next_room_id_pred) + '"}'
            
            next_room = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/fly/', 
                                      headers=headers, data=data).json()
            cooldown_func(next_room)
                
            next_room_id = next_room['room_id']
            if ('snitch' in next_room['players']) or ('snitch' in next_room['title']) or ('snitch' in next_room['description']) | (next_room_id == 986):
                print(f'Room Info: {next_room}')
                while True:
                    
                    cmds = input("-> ").lower().split(" ")
                    if cmds[0] in ["examine", "wear", "undress","choose",'transmogrify', 'take']:
                        # player.travel(cmds[0], True)
                        if len(cmds[1:]) == 2:
                            t = cmds[1] + " " + cmds[2]
                        elif len(cmds[1:]) == 3:
                            t = cmds[1] + " " + cmds[2] + " " + cmds[3]
                        # if cmds[0] == 'examine':
                        #     data = '{"name":"' + str(i) +'"}'
                        # else:
                        data = '{"name":"' + str(t) +'"}'
                        
                        take_examin = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/'+cmds[0]+'/', 
                                                headers=headers, data=data).json()
                        cooldown_func(take_examin)
                        print(take_examin)
                    elif cmds[0] == "q":
                        break
            
                
            return direction, next_room, next_room_id, encumbrance, strength, inventory, gold, armor, shoes, name, abilities, wrapped_curr_id_1, wrapped_curr_id_2
        
    return None, None, None, encumbrance, strength, inventory, gold, armor, shoes, name, abilities, wrapped_curr_id_1, wrapped_curr_id_2
    
def go_back(traversal_path, visited, curr_room):
    print("----------------GOING BACK-------------------------")
    while True:
        next_move = s.pop()
        print(str(next_move[0]))
        traversal_path.append(next_move[0])
        print(str(next_move[1]))
        data = '{"direction":"' + next_move[0] + '", "next_room_id":"' + str(next_move[1]) + '"}'
                
        next_room = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/fly/', headers=headers, data=data).json()
        cooldown_func(next_room)
        
        print(f"{next_room['messages']}\n")
        
        next_room_id = next_room['room_id']

        if '?' in visited[next_room_id].values():
            return next_room['room_id']
        if s.size() == 0:
            return next_room['room_id']

s.push(curr_id)
n = 0
while s.size() > 0:
    print(n)
    if n == 0:
        s.pop()
    n += 1
    cooldown = response["cooldown"]
    print(f"You're in room {curr_id}\n")
    
    cooldown_rounded_up = math.ceil(cooldown)
    
    for i in range(0, cooldown_rounded_up):
        print(f'Remaining cooldown 1: {cooldown_rounded_up - i})', end="\r")
        time.sleep(1)
    
    if direction == "exit":
        moving = False

    if curr_id not in visited:
        print('not in visited')
        visited[curr_id] = {}
        for direction in curr_room['exits']:
            visited[curr_id][direction] = '?'
    next_move, next_room, next_room_id, encumbrance, strength, inventory, gold, armor, shoes, name, abilities, wrapped_curr_id_1, wrapped_curr_id_2 = find_new_move_room(visited, 
                                                                                   curr_room, 
                                                                                   curr_id_1, curr_id_2, 
                                                                                   encumbrance, 
                                                                                   strength, 
                                                                                   inventory,
                                                                                   gold, 
                                                                                   armor, 
                                                                                   shoes,
                                                                                   name,
                                                                                   abilities,
                                                                                   has_mined,
                                                                                   wrapped_curr_id_1,
                                                                                   wrapped_curr_id_2
                                                                                   )
    
    if next_move == None:
        print(f"Reached a deadend:\n")
        curr_id = go_back(traversal_path, visited, curr_room)
        continue
    else:
        traversal_path.append(next_move)
        print(f"Going {next_move} towards {next_room_id}\n")
        visited[curr_id][next_move] = next_room_id
        room_info[curr_id]['exit_id'] = visited[curr_id]
        if next_room_id not in visited:
            visited[next_room_id] = {}
            for direction in next_room['exits']:
                visited[next_room_id][direction] = '?'
        visited[next_room_id][reverse[next_move]] = curr_id
        
        room_info[next_room_id] = next_room
        room_info[next_room_id]['exit_id'] = visited[next_room_id]
        
        s.push([reverse[next_move], curr_id])
        curr_id = next_room_id
    print("======================== Moved to new room =========================")
    print(f'Total rooms visited: {len(visited)}')

    # Save map info
    f = open("visited.txt","w")
    f.write(str(visited))
    f.close()
    
    f = open("room_info.txt","w")
    f.write(str(room_info))
    f.close()