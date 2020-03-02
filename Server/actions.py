import requests
from time import sleep

api_key = 'b252215e4fff6b9c3b59318b5aba49e66b9e5732'
url_base = 'https://lambda-treasure-hunt.herokuapp.com/api/adv'
headers = {'Content-Type': 'application/json', 
           'Authorization': 'Token ' + api_key}

# Used to test api key and check all the relevant stats before moving player
def get_init():
    response = requests.get(url_base + 'init', headers=headers)
    status_code = response.status_code

    if status_code is not 200:
        return ('Failed to Connect, Status Code: ', status_code)
    return response.json()

# Used to check your player's current status and inventory
def get_status():
    response = requests.post(url_base + 'status', headers=headers)
    status_code = response.status_code

    if status_code is not 200:
        return ('Failed to Connect, status Code: ', status_code)
    return response.json()

# Used to move player (direction -- n, s, e, w -- should be passed inside object)
def move(direction): 
    response = requests.post(url_base + 'move', headers=headers, json=direction)
    status_code = response.status_code

    if status_code is not 200:
        return ('Failed to Connect, status Code: ', status_code)
    return response.json()

# Used to examine players or items residing in the room you're currently in
def examine(room): 
    response = requests.post(url_base + 'examine', headers=headers, json=room)
    status_code = response.status_code

    if status_code is not 200:
        return ('Failed to Connect, status Code: ', status_code)
    return response.json()

# Used to pick up an item or treasure (this should be automated later along with traversing the graph)
def take_item(item):
    response = requests.post(url_base + 'take', headers=headers, json=item)
    status_code = response.status_code

    if status_code is not 200:
        return ('Failed to Connect, status Code: ', status_code)
    return response.json()

# Used to drop/discard an item
def drop_item(item):
    response = requests.post(url_base + 'drop', headers=headers, json=item)
    status_code = response.status_code

    if status_code is not 200:
        return ('Failed to Connect, status Code: ', status_code)
    return response.json()

# Used to sell items in your inventory to a shopkeepr
def sell_item(item):
    room = get_init()['title']
    # You can only sell items at a shop, hence this conditional
    if room != "Shop":
        return "You can't sell stuff anywhere but the shop."
    # Added a brief pause so commands hopefully won't clash later
    sleep(1)
    response = requests.post(url_base + 'sell', headers=headers, json=item)
    status_code = response.status_code 

    if status_code is not 200:
        return ('Failed to Connect, status Code: ', status_code)
    return response.json()

# Used to change your name (ReadMe says coins can't be mined without doing so... don't ask me why!)
def change_name(name): 
    response = requests.post(url_base + 'change_name', headers=headers, json={'name': name, 'confirm': 'yes'})
    status_code = response.status_code

    if status_code is not 200:
        return ('Failed to Connect, status Code: ', status_code)
    return response.json()

# Used to retrieve the last valid proof, which is then used to mine a new block
def get_last_proof():
    # [:-4] is necessary because every other API call goes to /adv (versus /bc)
    response = requests.get(url_base[:-4] + 'bc/last_proof', headers=headers)
    status_code = response.status_code

    if status_code is not 200:
        return ('Failed to Connect, status Code: ', status_code)
    return response.json()

# Used to submit a proposed proof (along with our unique token) to try mining a block
def mine(proof):
    print('Proof: ', proof)
    response = requests.post(url_base[:-4] + 'bc/mine', headers=headers, json=proof)
    status_code = response.status_code
    
    if status_code is not 200:
        return ('Failed to Connect, status Code: ', status_code)
    return response.json()

# Used to check your Lambda coin balance
def get_balance():
    response = requests.get(url_base[:-4] + 'bc/get_balance', headers=headers)
    status_code = response.status_code

    if status_code is not 200:
        return ('Failed to Connect, status Code: ', status_code)
    return response.json()