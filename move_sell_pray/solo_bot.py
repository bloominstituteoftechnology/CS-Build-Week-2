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
    if 'cooldown' in response:
        cooldown = response["cooldown"]
        cooldown_rounded_up = math.ceil(cooldown)
    else:
        response = requests.get(url + '/api/adv/init/', headers=headers)
        response = response.json()
        print(response)
        cooldown = response["cooldown"]
        cooldown_rounded_up = math.ceil(cooldown)
    for i in range(0, cooldown_rounded_up):
        print(f'Remaining cooldown new move: {cooldown_rounded_up - i})', end="\r")
        time.sleep(1)

# curl -X POST -H 'Authorization: Token 6a879ef0d8d6851f96f1d1144cd3836007c07225' -H "Content-Type: application/json" https://lambda-treasure-hunt.herokuapp.com/api/adv/status/
token = 'Token 6a879ef0d8d6851f96f1d1144cd3836007c07225' #6a879ef0d8d6851f96f1d1144cd3836007c07225 474a89c17aebf1820255565c58db9f9b2e2893f1
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
response_status = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/status/', 
                                            headers=headers).json()
print(response_status)
def response_func(what='status'):
    response_status = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/status/', 
                                            headers=headers).json()
    cooldown_func(response_status)
    if response_status['encumbrance']:
        encumbrance = response_status['encumbrance']
    else:
        encumbrance = 0
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


Initial_name = 'User 20679'
shrined = [0,1,1]
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
        # next_room = requests.post(url + '/api/adv/fly/', headers=headers, data=data).json()
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
            data_items = '{"name":"'+ i +'"}'
            response_examin = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/examine/', 
                                            headers=headers, data=data_items).json()
            print('Exmaning items\n')
            print(response_examin)
            cooldown_func(response_examin)
            response_sell = {}
            # if "{}" in response_examin['attributes']:
            item_to_sell = '{"name":"'+i+'", "confirm":"yes"}'
            response_sell = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/sell/', 
                                            headers=headers, data=item_to_sell).json()
            print(f'Item {i} sold\n')
            # sold = True
            cooldown_func(response_sell)
    # Come to where we started
    if come_back == True:
        for i in temp_list:
            next_room = requests.post(url + '/api/adv/fly/', headers=headers, data=i).json()
            cooldown_func(next_room)
    # Get current room id
    curr_id = next_room['room_id']
    
    return sold, shop
            
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
        # next_room = requests.post(url + '/api/adv/fly/', headers=headers, data=data).json()
        next_room = requests.post(url + '/api/adv/move/', headers=headers, data=data).json()
        i +=1
        cooldown_func(next_room)
    
    data_name = '{"name":"[WillH]", "confirm":"aye"}'

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
        # next_room = requests.post(url + '/api/adv/fly/', headers=headers, data=data).json()
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
    curr_id = next_room['room_id']
    return curr_id
import itertools
def dash_fly(curr_id,destination):
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
                          headers=headers, data=dash_data).json()
            print(next_room)
            print(f"room: {next_room['room_id']}")
            cooldown_func(next_room)
        else:
            print('FLYING')
            fly_data = '{"direction":"' + direction + '", "next_room_id":"' + ids_str + '"}'
            next_room = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/fly/', 
                                headers=headers, data=fly_data).json()
            # print(f"room: {next_room['room_id']}")
            cooldown_func(next_room)
        
    return destination


def go_to_wishing_well_mine(curr_id, wishing_well=55, alternative=False):
    if alternative == False:
        new_room_id = dash_fly(curr_id, wishing_well)
    else:
        pass
    print('===================== Wishing Well ===================')
    # name_of_well = next_room['Wishing Well']
    data_items = '{"name":"Wishing Well"}'
    response_examin = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/examine/', 
                                                    headers=headers, data=data_items).json()
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
    mine_room = ls8.run()
    mine_room = int(mine_room.replace(" ",""))
    print('=================== Going to mine ===================')
    mine_room = dash_fly(new_room_id, mine_room)

    message = proof_of_work(headers)
    print(f'Mining message: {message}')
    mine_response = requests.get('https://lambda-treasure-hunt.herokuapp.com/api/bc/get_balance/', 
                                 headers=headers).json()
    cooldown_func(mine_response)
    print('================ Mined new coin ===============')
    print(mine_response)
           
    return mine_room
    
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

def go_to_transmogrifier(curr_id, destination=495):
    
    print('=================== Going to the transmogrifier ===================')
    destination = dash_fly(curr_id, destination)
    encumbrance, strength, inventory, gold, armor, shoes, name, abilities, has_mined = response_func()
    n = 0
    
    for i in inventory:
        # if item has the word treasure sell it
        data_items = '{"name":"'+ i +'"}'
        response_examin = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/examine/', 
                                        headers=headers, data=data_items).json()
        print('Exmaning items\n')
        print(response_examin)
        cooldown_func(response_examin)
        print(response_examin['attributes'])
        if "{}" not in response_examin['attributes']:
            print(f'item: {i}')
            while True:
                print(inventory)
                cmds = input("-> ").lower().split(" ")
                if cmds[0] in ["examine", "wear", "undress","choose",'transmogrify']:
                    # player.travel(cmds[0], True)
                    t = ""
                    if len(cmds[:]) > 1:
                        t = cmds[1] + " " + cmds[2]
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

    return destination

def warp():
    response = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/warp/', headers=headers).json()
    cooldown_func(response)
    curr_id = response['room_id']
    print(response)
    return curr_id
    
def force_go(curr_id, destination):
    
    
    destination = dash_fly(curr_id, destination)
    encumbrance, strength, inventory, gold, armor, shoes, name, abilities, has_mined = response_func()
    
    
 
    while True:
        print(inventory)
        cmds = input("-> ").lower().split(" ")
        if cmds[0] in ["examine", "wear", "undress","choose",'transmogrify', 'take', 'pray', 'buy']:
            if cmds[0] == 'pray':
                 pray_response = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/'+cmds[0]+'/', 
                                    headers=headers).json()
                 print(pray_response)
            if cmds[0] == 'buy':
                t = cmds[1]
                if len(cmds[:]) > 2:
                    t = cmds[1] + " " + cmds[2]
                elif len(cmds[:]) > 3:
                    t = cmds[1] + " " + cmds[2] + " " + cmds[3]
                # {"name":"donut", "confirm":"yes"}
                data = '{"name":"' + str(t) +'", "confirm":"yes"}'
                take_examin = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/'+cmds[0]+'/', 
                                        headers=headers, data=data).json()
                cooldown_func(take_examin)
            else:
                t = cmds[1]
                if len(cmds[:]) > 2:
                    t = cmds[1] + " " + cmds[2]
                elif len(cmds[:]) > 3:
                    t = cmds[1] + " " + cmds[2] + " " + cmds[3]

                data = '{"name":"' + str(t) +'"}'
                
                take_examin = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/'+cmds[0]+'/', 
                                        headers=headers, data=data).json()
                cooldown_func(take_examin)
                print(take_examin)
        elif cmds[0].isnumeric():
            curr_room = destination
            destination = int(cmds[0])
            destination = force_go(curr_room, destination)
        
        elif cmds[0] == 'title':
            t = ""
            if len(cmds[1:]) > 1:
                t = cmds[1] + " " + cmds[2]
            elif len(cmds[1:]) > 2:
                t = cmds[1] + " " + cmds[2] + " " + cmds[3]
            elif len(cmds[1:]) > 3:
                t = cmds[1] + " " + cmds[2] + " " + cmds[3]+ " " + cmds[4]

            data = '{"title":"' + str(t) +'"}'
            
            take_examin = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/'+cmds[0]+'/', 
                                    headers=headers, data=data).json()
            cooldown_func(take_examin)
            print(take_examin)
            
        elif cmds[0] == "q":
            break

    return destination
    

def go_to_wishing_well_snitch(curr_id, wishing_well=55, alternative=False):
    new_room_id = dash_fly(curr_id, wishing_well)

    print('===================== Wishing Well ===================')
    # name_of_well = next_room['Wishing Well']
    data_items = '{"name":"Wishing Well"}'
    response_examin = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/examine/', 
                                                    headers=headers, data=data_items).json()
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
    print('=================== Going to to get snitch ===================')
    snitch_room = dash_fly(new_room_id, snitch_room)
    
    data = '{"name":"golden snitch"}'
                    
    take_snitch = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/take/', 
                                            headers=headers, data=data).json()


    cooldown_func(take_snitch)
    print('================ snitch grabbed ===============')
    print(take_snitch)
           
    return snitch_room

curr_id = response['room_id']
if curr_id > 500:
    wrapped = True
else:
    wrapped = False
    
force = 986 # <---------------- CHANGE to room
def find_new_move_room(visited, current_room, curr_id, encumbrance, 
                       strength, inventory, gold, armor, shoes, name, 
                       abilities, has_mined, wrapped):
    # sold = False
    # Go to shop
    # mine_room = force_got_to(curr_id, 111)  # <--------------------------FORCE MINE---------------------------------
    # new_id = go_to_wishing_well_mine(curr_id) # <-------------------------- FROCE WISH AND MINE -------------------------
    # force go to:
    if force != False:
        if (force > 500) & (wrapped == False):
            curr_id = warp()
            wrapped = False
        elif (force < 500) & (wrapped == True):
            curr_id = warp()
            wrapped = False
            
        print(f'============= Forced to go to {force} =============')
        curr_id = force_go(curr_id, force)
    
     # Share and Enjoy
    
    encumbrance, strength, inventory, gold, armor, shoes, name, abilities, has_mined = response_func()
    
    
    print(f'Encumbrance and stength: {encumbrance}, {strength}')
    if ((strength - encumbrance) <= 2 | (encumbrance == strength)) & (name == Initial_name):
        print('=========Going to the shop===========\n')
        
        sold, curr_id = go_to_shop(curr_id, inventory, shop=1, come_back=False)
    
    # Change Name
    elif (gold >= 1000) & (name == Initial_name):
        print('=========Going to the see pirate Ry===========\n')
        curr_id = go_to_pirate(curr_id)
    # Pray
    elif ('pray' in abilities) & (len(abilities) != 5):
        print('==============Going to Pray================')
        curr_id = go_to_shrine(curr_id)

    elif (has_mined == True) & (name != Initial_name):
        print('=============== lets wish and mine =============')
        curr_id = go_to_wishing_well_mine(curr_id)
    
    # Wear stuff
    elif ((armor == '') | (shoes == '')) & (has_mined == True):
        curr_id = go_to_transmogrifier(curr_id)
        
    elif (wrapped == True) & (has_mined == True):
        curr_id = warp()
        wrapped = False
        
    elif (wrapped == True) & (has_mined == False):
        print('========================= Getting that snitch ==================')
        while True:
            curr_id = go_to_wishing_well_snitch(curr_id, wishing_well=555)
        
        
    
        
        
    if curr_id not in visited:
        for direction in ['n','s','w','e']:
            print(direction)
            visited[curr_id] = {}
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
            if 'fly' in abilities:
                next_room = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/fly/', 
                                        headers=headers, data=data).json()
            else:
                next_room = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/move/', 
                                        headers=headers, data=data).json()
            cooldown_func(next_room)
                
            next_room_id = next_room['room_id']
            
            if (len(next_room['items']) > 0):
                weights = []
                
                for i in next_room['items']:
                    data_items = '{"name":"'+ i +'"}'
                    response_examin = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/examine/', 
                                                    headers=headers, data=data_items).json()
                    print('Exmaning items\n')
                    print(response_examin)
                    cooldown_func(response_examin)
                    
                    
                    if (encumbrance + response_examin['weight']) < strength:
                        name_item = i
                        
                        data_items = '{"name":"' + name_item + '"}'

                        response_items = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/take/', 
                                                            headers=headers, data=data_items).json()
                        print('Picked up item\n')
                        cooldown_func(response_items)
                        encumbrance += response_examin['weight']
                        inventory.append(name_item)
                
            return direction, next_room, next_room_id, encumbrance, strength, inventory, gold, armor, shoes, name, abilities, wrapped
        
    return None, None, None, encumbrance, strength, inventory, gold, armor, shoes, name, abilities, wrapped
    
def go_back(traversal_path, visited, curr_room):
    print("----------------GOING BACK-------------------------")
    while True:
        next_move = s.pop()
        if next_move != None:
            print(str(next_move[0]))
            traversal_path.append(next_move[0])
            print(str(next_move[1]))
            data = '{"direction":"' + next_move[0] + '", "next_room_id":"' + str(next_move[1]) + '"}'
                    
            next_room = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/fly/', headers=headers, data=data).json()
            # next_room = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/move/', headers=headers, data=data).json()
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
    next_move, next_room, next_room_id, encumbrance, strength, inventory, gold, armor, shoes, name, abilities, wrapped = find_new_move_room(visited, 
                                                                                   curr_room, 
                                                                                   curr_id, 
                                                                                   encumbrance, 
                                                                                   strength, 
                                                                                   inventory,
                                                                                   gold, 
                                                                                   armor, 
                                                                                   shoes,
                                                                                   name,
                                                                                   abilities,
                                                                                   has_mined,
                                                                                   wrapped
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