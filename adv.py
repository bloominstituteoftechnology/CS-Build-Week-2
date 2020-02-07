import random
import requests
import json
from api_key import API_KEY
import time
from random import randint, choice

url = 'https://lambda-treasure-hunt.herokuapp.com/api'

headers = {
    'Authorization': API_KEY
}

def init():
    r = requests.get(f'{url}/adv/init/', headers=headers)
    data = r.json()
    if 'errors' in data and len(data['errors']) > 0:
        print(data)
        return False
    with open('current_state.txt', 'w') as f:
        f.write(json.dumps(data, indent=4))
    print(data)
    return data


def move(payload):
    r_move = requests.post(f'{url}/adv/move', data=json.dumps(payload), headers=headers)
    data = r_move.json()
    # print(type(data))
    # print(data)
    if 'errors' in data and len(data['errors']) > 0:
        print(data)
        return False
    with open('current_state.txt', 'w') as f:
        f.write(json.dumps(data, indent=4))
    current_state = get_contents()
    # print(f'current_state, {current_state}\n')

    if str(data['coordinates']) not in current_state.keys():
        current_state[data['coordinates']] = data
        save_content(current_state)
    print(data)
    return data

def sleep_print(seconds):
    while seconds > 0:
        print('Wait', seconds, ' seconds!')
        time.sleep(1)
        seconds = seconds - 1

def save_content(data):
    with open('map.txt', 'w') as f:
        f.write(json.dumps(data, indent=4))

def get_contents():
    map_file = open('map.txt', 'rb').read()
    contents = json.loads(map_file)
    # print(f'Visited rooms: {len(contents)}')
    return contents

def get_item(item):
    r = requests.post(f'{url}/adv/take', data=json.dumps(item), headers=headers)
    data = r.json()
    print(data)
    return data

def drop_item(item):
    r = requests.post(f'{url}/adv/drop', data=json.dumps(item), headers=headers)
    data = r.json()
    print(data)
    return data

def change_name():
    name = {"name":"[ANN]"}
    r = requests.post(f'{url}/adv/change_name', data=json.dumps(name), headers=headers)
    data = r.json()
    print(data)
    return data

def status():
    r = requests.post(f'{url}/adv/status', headers=headers)
    data = r.json()
    print(data)
    return data

def wear(item):
    r = requests.post(f'{url}/adv/wear', data=json.dumps(item), headers=headers)
    data = r.json()
    print(data)
    return data



traversal_path = []
previous_room = [None]
opposites_direction = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}

room_track = {}
visited = {}

def travel():
    current_room = init()
    sleep_print(1)
    def check_directions(room_id):
        direction = []
        if 'e' in current_room['exits']:
            direction.append('e')
        if 'n' in current_room['exits']:
            direction.append('n')
        if 'w' in current_room['exits']:
            direction.append('w')
        if 's' in current_room['exits']:
            direction.append('s')
        return direction

    while len(visited) < len(get_contents()):
        # print('traversal_path', traversal_path)
        # print(f'\n{current_room}\n')
        cooldown = current_room['cooldown']
        print('----cooldown---', cooldown)
        room_id = current_room['room_id']
        print(f'\ncontenst----: {len(get_contents())}\n')
        sleep_print(cooldown)
        if room_id not in room_track:
            visited[room_id] = room_id
            print('visited room ', len(visited))
            room_track[room_id] = check_directions(room_id)
    
        if len(room_track[room_id]) < 1:
            print('room track-----if ', len(room_track))
            previous_direction = previous_room.pop()
            traversal_path.append(previous_direction)
            current_room = move({"direction": previous_direction})
            print('move pre')
            # print('coor', current_room['coordinates'])
            sleep_print(cooldown)
        else:
            print('room track-----else', len(room_track))
            print('room_track[room_id]:  ', len(room_track[room_id]))
            print('exits if', current_room['exits'][0])
            print(room_track[room_id])
            # if len(room_track[room_id]) > 0:
            next_direction = room_track[room_id].pop(0)
            previous_room.append(opposites_direction[next_direction])
            traversal_path.append(next_direction)
            current_room = move({"direction": next_direction})
            print('next_direction',next_direction)
            sleep_print(cooldown+1)
            # else:
            #     print('do some thing')
            #     direction = current_room['exits']
            #     current_room = move({"direction": direction})

            
def travel_2():
    while True:
        current_room = move({"direction":'e'})
        if len(current_room['errors']) > 0:
            current_room = move({"direction":'w'})
            





# init()

move({'direction': "n"})
# sleep_print(30)

# change_name()
# status()
# get_item({'name': 'tiny treasure'})
# sleep_print(8)
# print(f'visited :{len(get_contents())} rooms')
# travel()
# travel_2()

# wear({"name":"[tiny treasure]"})









