import requests

token = "397c72c0a6440aae0c75fd52cd42addaefb6ba87"

def init(token):
    URL = "https://lambda-treasure-hunt.herokuapp.com/api/adv/init/"

    HEADERS = {"Authorization": f"Token {token}"}
    # HEADERS = {"Authorization": "Token 397c72c0a6440aae0c75fd52cd42addaefb6ba87"}
    response = requests.get(url = URL, headers = HEADERS)
    print(response)
    data = response.json()
    print(data)

def move():
    URL = "https://lambda-treasure-hunt.herokuapp.com/api/adv/move/"
    HEADERS = {"Authorization": "Token 2b31b01022bf6e2fa8e79e93a7f2db494acdfdd6", "Content-Type": "application/json"}
    DATA = {"direction":"n"}
    response = requests.post(url = URL, headers = HEADERS, json = DATA)
    print(response)
    data = response.json()
    print(data)




#BOOOOM baby
# Init just needs to be run once to put your ass into the world
def fastMove():
    URL = "https://lambda-treasure-hunt.herokuapp.com/api/adv/move/"
    HEADERS = {"Authorization": "Token 2b31b01022bf6e2fa8e79e93a7f2db494acdfdd6", "Content-Type": "application/json"
    }
    DATA = {"direction":"n", "next_room_id": "10"}
    response = requests.post(url = URL, headers = HEADERS, json = DATA)
    print(response)
    data = response.json()
    print(data)

#init()
fastMove()

# data to be sent to api 
# data = {'api_dev_key':API_KEY, 
#         'api_option':'paste', 
#         'api_paste_code':source_code, 
#         'api_paste_format':'python'} 

    # return jsonify(response), 200

    # curl -X GET -H 'Authorization: Token ABC123' https://lambda-treasure-hunt.herokuapp.com/api/adv/init/

    # # Init
    # curl -X GET -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' https://lambda-treasure-hunt.herokuapp.com/api/adv/init/

    # # Movement
    # curl -X POST -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' -H "Content-Type: application/json" -d '{"direction":"n"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/move/

    # # Speedy movement
    # curl -X POST -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' -H "Content-Type: application/json" -d '{"direction":"s", "next_room_id": "0"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/move/

    # # Pick up Treasure:
    # curl -X POST -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' -H "Content-Type: application/json" -d '{"name":"treasure"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/take/

    # # Drop treasure
    # curl -X POST -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' -H "Content-Type: application/json" -d '{"name":"treasure"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/drop/

    # # Offer treasure to sell
    # curl -X POST -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' -H "Content-Type: application/json" -d '{"name":"treasure"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/sell/

    # # Confirm sale
    # curl -X POST -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' -H "Content-Type: application/json" -d '{"name":"treasure", "confirm":"yes"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/sell/

    # # Inventory check
    # curl -X POST -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' -H "Content-Type: application/json" https://lambda-treasure-hunt.herokuapp.com/api/adv/status/

    # # Examine item or player
    # curl -X POST -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' -H "Content-Type: application/json" -d '{"name":"[NAME OF ITEM OR PLAYER]"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/examine/

    # # Wear item
    # curl -X POST -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' -H "Content-Type: application/json" -d '{"name":"[NAME OF WEARABLE]"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/wear/

    # # Name changer
    # curl -X POST -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' -H "Content-Type: application/json" -d '{"name":"[NEW NAME]"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/change_name/

    # # Pray for powers
    # curl -X POST -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' -H "Content-Type: application/json" https://lambda-treasure-hunt.herokuapp.com/api/adv/pray/

    