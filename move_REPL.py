# Initialize
import requests
import sys
import time
import math
import pickle

def load():
    print('Checking if map saved...')

    try:
        with open('map.pickle', 'rb') as f:
            graph = pickle.load(f)
            print(f"Map contains {len(graph)} nodes.")
        print('Map loaded\n')
    except FileNotFoundError:
        graph = {}

    try:
        with open('500rooms.pickle', 'rb') as f:
            room_list = pickle.load(f)
        print('Map loaded\n')
    except FileNotFoundError:
        room_list = {}

    return graph, room_list

graph, room_list = load()

token = 'Token 6a879ef0d8d6851f96f1d1144cd3836007c07225'
url = 'https://lambda-treasure-hunt.herokuapp.com'
headers = {
    'Authorization': token,
}

response = requests.get(url + '/api/adv/init/', headers=headers)
response = response.json()

print(response)

cooldown = response["cooldown"] # is this right?
current_room = response["room_id"]

# Move 
headers = {
    'Authorization': token,
    'Content-Type': 'application/json',
}

moving = True
while moving:
    print("Enter the direction you'd like to move: ")
    direction = input()
    # print(direction)
    
    if direction == 'exit':
        moving = False
        break
    
    room = graph[current_room][direction]
    data = {"direction": f'{direction}', "next_room_id": f"{room}"}

    # data = '{"direction":"' + direction + '"}'

    response = requests.post(url + '/api/adv/move/', headers=headers, json=data)
    print(response.text)

    json_response = response.json()
    cooldown = json_response["cooldown"]
    current_room = json_response["room_id"]
    cooldown_rounded_up = math.ceil(cooldown)

    for i in range(0, cooldown_rounded_up):
        print(f'Remaining cooldown: {cooldown_rounded_up - i}...', end="\r")
        time.sleep(1)
#curl -X GET -H 'Authorization: Token 6a879ef0d8d6851f96f1d1144cd3836007c07225' https://lambda-treasure-hunt.herokuapp.com/api/adv/init/
#curl -X POST -H 'Authorization: Token 6a879ef0d8d6851f96f1d1144cd3836007c07225' -H "Content-Type: application/json" -d '{"name":"amazing treasure"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/take/
#curl -X POST -H 'Authorization: Token 6a879ef0d8d6851f96f1d1144cd3836007c07225' -H "Content-Type: application/json" https://lambda-treasure-hunt.herokuapp.com/api/adv/status/
#curl -X POST -H 'Authorization: Token 6a879ef0d8d6851f96f1d1144cd3836007c07225' -H "Content-Type: application/json" -d '{"name":"tiny treasure", "confirm":"yes"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/sell/
#curl -X POST -H 'Authorization: Token 6a879ef0d8d6851f96f1d1144cd3836007c07225' -H "Content-Type: application/json" -d '{"name":"tiny treasure"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/drop/
#curl -X POST -H 'Authorization: Token 6a879ef0d8d6851f96f1d1144cd3836007c07225' -H "Content-Type: application/json" -d '{"name":"Wishing Well"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/examine/
#curl -X GET -H 'Authorization: Token 6a879ef0d8d6851f96f1d1144cd3836007c07225' https://lambda-treasure-hunt.herokuapp.com/api/bc/last_proof/
#curl -X POST -H 'Authorization: Token 6a879ef0d8d6851f96f1d1144cd3836007c07225' -H "Content-Type: application/json" -d '{"proof":16663616}' https://lambda-treasure-hunt.herokuapp.com/api/bc/mine/
#curl -X GET -H 'Authorization: Token 6a879ef0d8d6851f96f1d1144cd3836007c07225' https://lambda-treasure-hunt.herokuapp.com/api/bc/get_balance/
#curl -X POST -H 'Authorization: Token 6a879ef0d8d6851f96f1d1144cd3836007c07225' -H "Content-Type: application/json" https://lambda-treasure-hunt.herokuapp.com/api/adv/pray/
#curl -X POST -H 'Authorization: Token 6a879ef0d8d6851f96f1d1144cd3836007c07225' -H "Content-Type: application/json" -d '{"name":"shiny treasure"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/examine/
#curl -X POST -H 'Authorization: Token 6a879ef0d8d6851f96f1d1144cd3836007c07225' -H "Content-Type: application/json" -d '{"name":"shiny treasure", "confirm":"yes"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/sell/
#curl -X POST -H 'Authorization: Token 6a879ef0d8d6851f96f1d1144cd3836007c07225' -H "Content-Type: application/json" -d '{"name":"donut"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/buy/
#curl -X POST -H 'Authorization: Token 6a879ef0d8d6851f96f1d1144cd3836007c07225' -H "Content-Type: application/json" -d '{"name":"great treasure"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/transmogrify/
#curl -X POST -H 'Authorization: Token 6a879ef0d8d6851f96f1d1144cd3836007c07225' -H "Content-Type: application/json" -d '{"name":"poor boots"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/wear/
#curl -X POST -H 'Authorization: Token 6a879ef0d8d6851f96f1d1144cd3836007c07225' -H "Content-Type: application/json" https://lambda-treasure-hunt.herokuapp.com/api/adv/warp/
#curl -X POST -H 'Authorization: Token 6a879ef0d8d6851f96f1d1144cd3836007c07225' -H "Content-Type: application/json" -d '{"direction":"e"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/move/

#curl -X POST -H 'Authorization: Token 6a879ef0d8d6851f96f1d1144cd3836007c07225' -H "Content-Type: application/json" -d '{"name":"small treasure"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/take/