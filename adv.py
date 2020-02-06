import random
import requests
import json
from api_key import API_KEY
import time

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
    print(data)
    return data


def move(payload):
    r_move = requests.post(f'{url}/adv/move', data=json.dumps(payload), headers=headers)
    data = r_move.json()
    if 'errors' in data and len(data['errors']) > 0:
        print(data)
        return False
    current_state = get_contents()
    # print('current_state', current_state)

    if str(data['coordinates']) not in current_state.keys():
        current_state[data['coordinates']] = data
        save_content(current_state)
        # print(data)
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
    print(f'Visited rooms: {len(contents)}')
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

def travel():
    current_room = init()
    if current_room:
        direction = current_room['exits'][0]
        while True:
            current_room = move({"direction": direction})
            if current_room:
                cooldown = current_room['cooldown']
                print('Room ID: ', current_room['room_id'])
                print('ITEMS: ', current_room['items'])
                print('Cooling down...', cooldown, ' seconds')
                
                # MAIN DIRECTION LOGIC
                direction = current_room['exits'][0]

                sleep_print(cooldown+2)
                item = current_room['items']
                if len(item) > 0:
                    print('We found item!!')
                    get_item({'name': item[0]})

                if current_room['room_id'] == 0:
                    print('sell something')
                    break
            else:
                print('Not room...')
                sleep_print(30)
            



move({'direction': "n"})
# change_name()
# status()
# get_item({'name': 'shiny treasure'})

get_contents()
# travel()









