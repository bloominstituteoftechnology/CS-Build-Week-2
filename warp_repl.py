# Initialize
import requests
import sys
import time
import math
import pickle

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
    
    data = {"direction": f'{direction}'}

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