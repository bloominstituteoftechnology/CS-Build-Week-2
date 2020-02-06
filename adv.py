import random
import requests
import json
from api_key import API_KEY
import time
from random import randint

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
    # print(data)
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
        print('Cooling. Ready in ', seconds, ' seconds!')
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

ccurrent_room = init()

def travel():
    # current_room = init()
    # cooldown = current_room['cooldown']
    while True:
        if current_room:
            direction = 'w'
            cooldown = current_room['cooldown']
            exists = current_room['exits']
            print('Room ID: ', current_room['room_id'])
            print('ITEMS: ', current_room['items'])
            print('coor', current_room['coordinates'])
   

            print('EXITS', exists)
            print('DIRECTION', direction)

            item = current_room['items']
            if len(item) > 0:
                print('We found item!!')
                get_item({'name': item[0]})

            if current_room['room_id'] == 0:
                print('sell something')
                break

            sleep_print(cooldown+1)
            current_room = move({"direction": direction})
        else:
            print(direction)
            sleep_print(15)

            

# init()

# move({'direction': "w"})
# change_name()
# status()
# get_item({'name': 'shiny treasure'})

# print(len(get_contents()))
travel()










