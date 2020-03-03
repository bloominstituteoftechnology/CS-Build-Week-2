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

# curl -X POST -H 'Authorization: Token 6a879ef0d8d6851f96f1d1144cd3836007c07225' -H "Content-Type: application/json" https://lambda-treasure-hunt.herokuapp.com/api/adv/status/
token = 'Token b9ac3ccda7673a719af4c4305ec9efacdef4c161' #6a879ef0d8d6851f96f1d1144cd3836007c07225
url = 'https://lambda-treasure-hunt.herokuapp.com'
headers = {
    'Authorization': token,
}

response = requests.get(url + '/api/adv/init/', headers=headers)
response = response.json()
print(response)
cooldown = response["cooldown"] 
headers = {
    'Authorization': token,
    'Content-Type': 'application/json',
}
moving = True

curr_id = response['room_id']

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
    
    
    return encumbrance, strength, inventory, gold, armor, shoes, name, abilities

# Get status and update variables
encumbrance, strength, inventory, gold, armor, shoes, name, abilities = response_func()
print(f'Name: {name}')


Initial_name = 'User 20677'
shrined = [0,0,0]
# Go to shop function
def go_to_shop(curr_id, inventory, shop=1, come_back=False):
    """
    parms curr_id: ID of current location
    parms inventory: Current items in inventory
    parms shop: ID of shop location
    parms come_back: Boolean, if True goes back to where it started, 
                    False continues from shop
    Return sold, curr_id:  sold: True if it sold any items, curr_id: New location ID
    """
    # find shortest path using Breadth First Search. Returns list of ids [1,4,60]
    traversal_path = g.bfs(curr_id, shop)
    i = 0
    temp_list = []
    while i + 1 < len(traversal_path):
        print(traversal_path[i])
        # Gets direction from the revered path w, e, s or n                        
        direction = path_reverse[traversal_path[i]][traversal_path[i+1]]
        # Create data to send through post, direction and ID of next room  
        data = '{"direction":"' + direction + '", "next_room_id":"' + str(traversal_path[i+1]) + '"}'
        # get the reverse in case come_back = True
        reverse_data = '{"direction":"' + reverse[direction] + '", "next_room_id":"' + str(traversal_path[i]) + '"}'
        temp_list.insert(0,reverse_data)
        # Move
        next_room = requests.post(url + '/api/adv/move/', headers=headers, data=data).json()
        # increment i
        i+=1
        # Cooldown
        cooldown_func(next_room)
    
    sold = False
    # iterate through items to sell each item
    for i in inventory:
        # if item has the word treasure sell it
        if 'treasure' in i:
            item_to_sell = '{"name":"'+i+'", "confirm":"yes"}'
            response_sell = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/sell/', 
                                        headers=headers, data=item_to_sell).json()
            print(f'Item {i} sold\n')
            sold = True
            cooldown_func(response_sell)
    # Come to where we started
    if come_back == True:
        for i in temp_list:
            next_room = requests.post(url + '/api/adv/move/', headers=headers, data=i).json()
            cooldown_func(next_room)
    # Get current room id
    curr_id = next_room['room_id']
    
    return sold
            
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
        next_room = requests.post(url + '/api/adv/move/', headers=headers, data=data).json()
        i +=1
        cooldown_func(next_room)
    
    data_name = '{"name":"[MALI-BOT]", "confirm":"aye"}'

    response_name = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/change_name/', headers=headers, data=data_name).json()
    print(response_name['messages'])
    

    if come_back == True:
        for i in temp_list:
            next_room = requests.post(url + '/api/adv/move/', headers=headers, data=i).json()
            cooldown_func(next_room)
            
    print("NAME CHANGED ============= Let's Mine!!!\n")
    curr_id = next_room['room_id']
    # return curr_id
    
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
        next_room = requests.post(url + '/api/adv/move/', headers=headers, data=data).json()
        i +=1
        cooldown_func(next_room)
    response_shrine = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/pray/', 
                                                headers=headers).json()
    print('=========Shrined!=================\n')
    cooldown_func(response_shrine)
    shrined[ind] = 1
    print(shrined)
    print(response_shrine)
    # curr_id = next_room['room_id']
    # return curr_id
    
    




def find_new_move_room(visited, current_room, curr_id, encumbrance, 
                       strength, inventory, gold, armor, shoes, name, abilities):
    sold = False
    if (strength - encumbrance) <= 2 | (encumbrance == strength) | ((gold == 900) & (encumbrance == 3)):
        print('=========Going to the shop===========\n')
        
        sold = go_to_shop(curr_id, inventory, shop=1, come_back=False)
        if sold == True:
            curr_id, encumbrance, strength, inventory, gold, armor, shoes, name = response_func()
            
    print(f'Encumbrance and stength: {encumbrance}, {strength}')
    if (gold >= 1000) & (name == '[Stephen-Sinclair-BOT]'):
        print('=========Going to the see pirate Ry===========\n')
        go_to_pirate(curr_id)
    
    if ('pray' in abilities) & (shrined != [1,1,1]):
        print('==============Going to Pray================')
        go_to_shrine(curr_id)
        
        
            
    room_exits = visited[curr_id]
    known_ids = path[curr_id]
    print(f'room_exits: {room_exits}\n')
    dirs = []
    print(f'known_ids: {known_ids}')
            
            
    for direction in room_exits:
        dirs.append(direction)
    random.shuffle(dirs)
    for direction in dirs:
        if room_exits[direction] == '?':
            next_room_id_pred = known_ids[direction]
            print(f'next_room_id_pred: {next_room_id_pred}')
            data = '{"direction":"' + direction + '", "next_room_id":"' + str(next_room_id_pred) + '"}'
            
            next_room = requests.post(url + '/api/adv/move/', 
                                      headers=headers, data=data).json()
            cooldown_func(next_room)
            
            if 'shrine' in next_room['description']:
                response_shrine = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/pray/', 
                                                headers=headers).json()
                print('Shrine\n')
                cooldown_func(response_shrine)
                
            next_room_id = next_room['room_id']
            
            if (len(next_room['items']) > 0):
                weights = []
                
                for i in next_room['items']:
                    data_items = '{"name":"'+ i +'"}'
                    response_examin = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/examine/', 
                                                    headers=headers, data=data_items).json()
                    print('Exmaning items\n')
                    cooldown_func(response_examin)
                    
                    
                    
                    if response_examin['itemtype'] == 'TREASURE':
                        if (encumbrance + response_examin['weight']) < strength:
                                name_item = i
                            
                                data_items = '{"name":"' + name_item + '"}'

                                response_items = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/take/', 
                                                                headers=headers, data=data_items).json()
                                print('Picked up item\n')
                                cooldown_func(response_items)
                                encumbrance += response_examin['weight']
                                inventory.append(name_item)
                    elif (armor == None) | (shoes == None):
                        
                        data_wear = '{"name":"'+ i +'"}'
                        response_wear = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/wear/', 
                                                        headers=headers, data=data_wear).json()
                        cooldown_func(response_wear)
                        print(f'Wore item: {i}\n')
                        next_room['items'].remove(i)
                        print('Getting status after wearing\n')
                        encumbrance, strength, inventory, gold, armor, shoes, name = response_func()
                            
                        
            
                # if (encumbrance == strength) | (strength - encumbrance) == 1:
                if next_room['title'] == 'Shop':
                    sold = 0
                    for i in inventory:
                        if 'treasure' in i:
                            item_to_sell = '{"name":"'+i+'", "confirm":"yes"}'
                            response_sell = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/sell/', 
                                                        headers=headers, data=item_to_sell).json()
                            print(f'Item {i} sold\n')
                            sold = 1
                            cooldown_func(response_items)
                    if sold == 1:
                        encumbrance, strength, inventory, gold, armor, shoes, name = response_func()
            return direction, next_room, next_room_id, encumbrance, strength, inventory, gold, armor, shoes, name, abilities
        
    return None, None, None, encumbrance, strength, inventory, gold, armor, shoes, name, abilities
    
def go_back(traversal_path, visited, curr_room):
    print("----------------GOING BACK-------------------------")
    while True:
        next_move = s.pop()
        print(str(next_move[0]))
        traversal_path.append(next_move[0])
        print(str(next_move[1]))
        data = '{"direction":"' + next_move[0] + '", "next_room_id":"' + str(next_move[1]) + '"}'
                
        next_room = requests.post(url + '/api/adv/move/', headers=headers, data=data).json()
        cooldown_func(next_room)
        
        print(f"{next_room['messages']}\n")
        
        next_room_id = next_room['room_id']

        if '?' in visited[next_room_id].values():
            return next_room['room_id']
        if s.size() == 0:
            return next_room['room_id']

s.push(curr_id)
n = 0
while moving:
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
    next_move, next_room, next_room_id, encumbrance, strength, inventory, gold, armor, shoes, name, abilities = find_new_move_room(visited, 
                                                                                   curr_room, 
                                                                                   curr_id, 
                                                                                   encumbrance, 
                                                                                   strength, 
                                                                                   inventory,
                                                                                   gold, 
                                                                                   armor, 
                                                                                   shoes,
                                                                                   name,
                                                                                   abilities
                                                                                   )
    
    if next_move == None:
        print(f"Reached a deadend:\n")
        curr_id = go_back(traversal_path, visited, curr_room)
        continue
    else:
        traversal_path.append(next_move)
        print(f"Going {next_move} towards {next_room_id}\n")
        visited[curr_id][next_move] = next_room_id
        # room_info[curr_id] = curr_room
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
    # print(f'room_info: {room_info}')

    f = open("visited.txt","w")
    f.write(str(visited))
    f.close()
    
    f = open("room_info.txt","w")
    f.write(str(room_info))
    f.close()

    # json = json.dumps(visited)
    # f = open("visited.json","w")
    # f.write(json)
    # f.close()

    # json = json.dumps(room_info)
    # f = open("room_info.json","w")
    # f.write(json)
    # f.close()