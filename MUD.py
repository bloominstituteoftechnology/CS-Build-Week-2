import requests

def init():
    URL = "https://lambda-treasure-hunt.herokuapp.com/api/adv/init/"

    HEADERS = {"Authorization": "Token 2b31b01022bf6e2fa8e79e93a7f2db494acdfdd6"}
    response = requests.get(url = URL, headers = HEADERS)
    print(response)
    data = response.json()
    print(data)

def move():
    URL = "https://lambda-treasure-hunt.herokuapp.com/api/adv/move/"
    HEADERS = {"Authorization": "Token 2b31b01022bf6e2fa8e79e93a7f2db494acdfdd6", "Content-Type": "application/json"
    }
    DATA = {"direction":"s"}
    response = requests.post(url = URL, headers = HEADERS, json = DATA)
    print(response)
    data = response.json()
    print(data)

#init()
#move()

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

def pickUpTreasure():
    URL = "https://lambda-treasure-hunt.herokuapp.com/api/adv/take/"
    HEADERS = {"Authorization": "Token 2b31b01022bf6e2fa8e79e93a7f2db494acdfdd6", "Content-Type": "application/json"
    }
    DATA = {"name":"treasure"}
    response = requests.post(url = URL, headers = HEADERS, json = DATA)
    print(response)
    data = response.json()
    print(data)

def dropTreasure():
    URL = "https://lambda-treasure-hunt.herokuapp.com/api/adv/drop/"
    HEADERS = {"Authorization": "Token 2b31b01022bf6e2fa8e79e93a7f2db494acdfdd6", "Content-Type": "application/json"
    }
    DATA = {"name":"treasure"}
    response = requests.post(url = URL, headers = HEADERS, json = DATA)
    print(response)
    data = response.json()
    print(data)

def offerTreasureForSale():
    URL = "https://lambda-treasure-hunt.herokuapp.com/api/adv/sell/"
    HEADERS = {"Authorization": "Token 2b31b01022bf6e2fa8e79e93a7f2db494acdfdd6", "Content-Type": "application/json"
    }
    DATA = {"name":"treasure"}
    response = requests.post(url = URL, headers = HEADERS, json = DATA)
    print(response)
    data = response.json()
    print(data)

def sellTreasure():
    URL = "https://lambda-treasure-hunt.herokuapp.com/api/adv/sell/"
    HEADERS = {"Authorization": "Token 2b31b01022bf6e2fa8e79e93a7f2db494acdfdd6", "Content-Type": "application/json"
    }
    DATA = {"name":"treasure", "confirm":"yes"}
    response = requests.post(url = URL, headers = HEADERS, json = DATA)
    print(response)
    data = response.json()
    print(data)

def checkInventory():
    URL = "https://lambda-treasure-hunt.herokuapp.com/api/adv/status/"
    HEADERS = {"Authorization": "Token 2b31b01022bf6e2fa8e79e93a7f2db494acdfdd6", "Content-Type": "application/json"
    }
    response = requests.post(url = URL, headers = HEADERS)
    print(response)
    data = response.json()
    print(data)

def examine():
    URL = "https://lambda-treasure-hunt.herokuapp.com/api/adv/examine/"
    HEADERS = {"Authorization": "Token 2b31b01022bf6e2fa8e79e93a7f2db494acdfdd6", "Content-Type": "application/json"
    }
    DATA = {"name":"[NAME OF ITEM OR PLAYER]"}
    response = requests.post(url = URL, headers = HEADERS, json = DATA)
    print(response)
    data = response.json()
    print(data)

def changeName():
    URL = "https://lambda-treasure-hunt.herokuapp.com/api/adv/change_name/"
    HEADERS = {"Authorization": "Token 2b31b01022bf6e2fa8e79e93a7f2db494acdfdd6", "Content-Type": "application/json"
    }
    DATA = {"name":"[NEW NAME]"}
    response = requests.post(url = URL, headers = HEADERS, json = DATA)
    print(response)
    data = response.json()
    print(data)

def pray():
    URL = "https://lambda-treasure-hunt.herokuapp.com/api/adv/pray/"
    HEADERS = {"Authorization": "Token 2b31b01022bf6e2fa8e79e93a7f2db494acdfdd6", "Content-Type": "application/json"
    }
    response = requests.post(url = URL, headers = HEADERS)
    print(response)
    data = response.json()
    print(data)

def fly():
    URL = "https://lambda-treasure-hunt.herokuapp.com/api/adv/fly/"
    HEADERS = {"Authorization": "Token 2b31b01022bf6e2fa8e79e93a7f2db494acdfdd6", "Content-Type": "application/json"
    }
    DATA = {"direction":"n"}
    response = requests.post(url = URL, headers = HEADERS, json = DATA)
    print(response)
    data = response.json()
    print(data)

def dash():
    URL = "https://lambda-treasure-hunt.herokuapp.com/api/adv/dash/"
    HEADERS = {"Authorization": "Token 2b31b01022bf6e2fa8e79e93a7f2db494acdfdd6", "Content-Type": "application/json"
    }
    DATA = {"direction":"n", "num_rooms":"5", "next_room_ids":"10,19,20,63,72"}
    response = requests.post(url = URL, headers = HEADERS, json = DATA)
    print(response)
    data = response.json()
    print(data)

def giveToGhost():
    # Holds 1 item ONLY - heaviest item
    URL = "https://lambda-treasure-hunt.herokuapp.com/api/adv/carry/"
    HEADERS = {"Authorization": "Token 2b31b01022bf6e2fa8e79e93a7f2db494acdfdd6", "Content-Type": "application/json"
    }
    DATA = {"name":"[ITEM_NAME]"}
    response = requests.post(url = URL, headers = HEADERS, json = DATA)
    print(response)
    data = response.json()
    print(data)

def takeFromGhost():
    URL = "https://lambda-treasure-hunt.herokuapp.com/api/adv/receive/"
    HEADERS = {"Authorization": "Token 2b31b01022bf6e2fa8e79e93a7f2db494acdfdd6", "Content-Type": "application/json"
    }
    response = requests.post(url = URL, headers = HEADERS)
    print(response)
    data = response.json()
    print(data)


    # return jsonify(response), 200

    # curl -X GET -H 'Authorization: Token 2b31b01022bf6e2fa8e79e93a7f2db494acdfdd6' https://lambda-treasure-hunt.herokuapp.com/api/adv/init/

    # # Init
    # curl -X GET -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' https://lambda-treasure-hunt.herokuapp.com/api/adv/init/

    # # Movement
    # curl -X POST -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' 
    # -H "Content-Type: application/json" -d '{"direction":"n"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/move/

    # # Speedy movement
    # curl -X POST -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' -H "Content-Type: application/json" 
    # -d '{"direction":"s", "next_room_id": "0"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/move/

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

    # Flight
    # curl -X POST -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' -H "Content-Type: application/json" -d '{"direction":"n"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/fly/

    # Dash
    # curl -X POST -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' -H "Content-Type: application/json" -d '{"direction":"n", "num_rooms":"5", "next_room_ids":"10,19,20,63,72"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/dash/

    # Ghost Carry
    # curl -X POST -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' -H "Content-Type: application/json" -d '{"name":"[ITEM_NAME]"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/carry/

    # Ghost Receive
    # curl -X POST -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' -H "Content-Type: application/json" https://lambda-treasure-hunt.herokuapp.com/api/adv/receive/