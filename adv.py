import random
import requests
import json
from api_key import API_KEY

url = 'https://lambda-treasure-hunt.herokuapp.com/api'

headers = {
    'Authorization': API_KEY
}

def init():
    r = requests.get(f'{url}/adv/init/', headers=headers)
    print(r.json())


def move():
    payload = {"direction":"s"}
    r_move = requests.post(f'{url}/adv/move', data=json.dumps(payload), headers=headers)
    save = r_move.json()
    data = {
        'room_id':  save['room_id'],
        'coordinates':  save['coordinates'],
        'exits':  save['exits'],
    }
    current_state = get_contents()
    current_state[save['room_id']] = data

    save_content(current_state)
    print(save)

def save_content(data):
    with open('map.txt', 'w') as f:
        f.write(json.dumps(data, indent=4))


def get_contents():
    map_file = open('map.txt', 'rb').read()
    contents = json.loads(map_file)
    return contents



# init()
move()









