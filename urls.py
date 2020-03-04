import requests
import os
from time import sleep

base = 'https://lambda-treasure-hunt.herokuapp.com/api/'

endpoint = {
    'init': 'adv/init', # GET

    'wear': 'adv/wear', # POST
    # data: {name: name_of_wearable str}

    'undress': 'adv/undress', # POST
    # data: {name: name_of_wearable str}
    
    'carry': 'adv/carry', # POST
    # data: {name: name_of_item str}
    
    'receive': 'adv/receive', # POST
    # data: {name: name_of_item str}
    
    'warp': 'adv/warp', # POST
    
    'recall': 'adv/recall', # POST
    
    'take': 'adv/take', # POST
    # data: {name: name_of_treasure str}
    
    'drop': 'adv/drop', # POST
    # data: {name: name_of_treasure str}
    
    'move': 'adv/move', # POST 
    # data : {direction: str}
    # optional data for "wise explorer" {direction: str, next_room_id: numerical str}
    
    'sell': 'adv/sell', # POST
    # data: {name: name_of_treasure str, confirm: "yes" or "no"}
    
    'change': 'adv/transmogrify', # POST
    # data: {name: name_of_item}
    
    'status': 'adv/status', # POST
    
    'examine': 'adv/examine', # POST
    # data: {name: name of item in room or inventory, or name of player in room}
    
    'name': 'adv/change_name', # POST
    # data: {name: new_name str}
    
    'pray': 'adv/pray', # POST
    
    'fly': 'adv/fly', # POST
    # data: {direction: str}
    
    'dash': 'adv/dash', # POST
    # data: {direction: str, num_rooms: numerical str, next_room_ids: str:
    # "10,19,20,63,72"}
    
    'mine': 'bc/mine', # POST
    # data: {proof: new_proof}
    
    'lp': 'bc/last_proof', # POST
    
    'bal': 'bc/get_balance' # GET
}

##token = os.environ.get('TOKEN')
token = "f976aafe27b40a76a602b84c15df748b3c6d7403"
headers = {'Authorization': "Token " + token}

cooldown = 1

def makeGetRequest(endpoint):
    req = requests.get(F"{base}{endpoint}/", headers=headers)
    json = req.json()
    print(F"Here is the response json: {json}")
    if json["cooldown"] != 0:
        cooldown = float(json["cooldown"])
    print(F"Cooldown in seconds: {cooldown}")
    if len(json['errors']):
        for err in json['errors']:
            print('\nERROR: ', err, end='\n\n')
    sleep(cooldown)
    return json

# makeGetRequest(endpoint["init"])

def makePostRequest(endpoint, data):
    req = requests.post(F"{base}{endpoint}/", json=data, headers=headers)
    json = req.json()
    if json["cooldown"] != 0:
        cooldown = float(json["cooldown"])
    print(F"Cooldown: {cooldown}")
    if len(json["errors"]):
        for err in json["errors"]:
            print("ERROR: ", err, end="\n\n")
    sleep(cooldown)
    return json

makePostRequest(endpoint["move"], {"direction": "n"})

"""
def post(endpoint, data):
    '''
    accepts (endpoint, data)
    Makes a post request to the given endpoint with
    Authorization header and token 
    returns a jsonified response with cooldown
    '''
    req = requests.post(f'{base}{endpoint}/', json=data, headers=headers)
    json = req.json()
    if json['cooldown'] != 0:
        sleep_time = float(json['cooldown'])
    print(f'{endpoint} ----> {sleep_time} second cooldown')
    if len(json['errors']):
        for err in json['errors']:
            print('\nERROR --->', err, end='\n\n')
    sleep(sleep_time)
    return json

"""
