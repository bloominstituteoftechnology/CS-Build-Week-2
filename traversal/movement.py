import hashlib
import requests
import time
import sys
import json
from decouple import config
from visited_rooms import visited_rooms


# Import visited_rooms for wise movement
# Traversal that uses DFS, to find path
# Store is at room id 1
mine = 72
store = 1
# Name Changer is at 467
name_change = 467
# Well is at 55
well = 55
# Shrines is at 461, 374
shrine1 = 461
shrine2 = 374
# Mine location (decoded coordinates as room id)
# Add power abilites (STRETCH)

node = "https://lambda-treasure-hunt.herokuapp.com/api"
headers = {"Authorization": config('API_KEY')}
player_data = requests.post(url=node + "/adv/status", headers=headers)
player = player_data.json()


def wise_map(visited_rooms):
    # Get the current room information
    r = requests.get(url=node + "/adv/init", headers=headers)
    curr = r.json()
    print(curr)
    # Pass in the direction being moved
    # Grab the room_id of room going into
    # Run moving function


def sell(player):
    if len(player['inventory']) > 0:
        data = {"name": "treasure"}
        r = requests.post(url=node + "/adv/sell",
                          json=data, headers=headers)
        # Handle non-json response
        print("data", data)
        try:
            print("cooldown", r.json()["cooldown"])
            time.sleep(r.json()["cooldown"])
            data = {"name": "treasure", "confirm": "yes"}
            r = requests.post(url=node + "/adv/sell",
                              json=data, headers=headers)
            try:
                print("cooldown", r.json()["cooldown"])
                time.sleep(r.json()["cooldown"])
                data = {"name": "treasure", "confirm": "yes"}
                r = requests.post(url=node + "/adv/sell",
                                  json=data, headers=headers)
            except ValueError:
                print("Error:  Non-json response")
                print("next_room_id Response returned:")
                print(r)
        except ValueError:
            print("Error:  Non-json response")
            print("next_room_id Response returned:")
            print(r)
            sell(player)
    else:
        print('No more to sell!')


def moving_function(traversal_path, rooms_id_list=None):
    print(traversal_path, rooms_id_list)
    for i in range(len(traversal_path)):
        # data = {"direction": i, "next_room_id": str(room_id)}
        data = {"direction": traversal_path[i],
                "next_room_id": str(rooms_id_list[i])}
        r = requests.post(url=node + "/adv/move",
                          json=data, headers=headers)
        # Handle non-json response
        print("data", data)
        try:
            print("cooldown", r.json()["cooldown"])
            time.sleep(r.json()["cooldown"])
        except ValueError:
            print("Error:  Non-json response")
            print("next_room_id Response returned:")
            print(r)


r = requests.get(url=node + "/adv/init", headers=headers)
time.sleep(r.json()["cooldown"])
starting_room = r.json()


def room_search(visited_rooms, starting_room, target):
    queue = []
    visited = set()
    start = starting_room['room_id']
    print("start", start)
    queue.append(start)
    rooms_id_list = [[]]
    paths = [[]]
    while len(queue) > 0:
        path = paths.pop(0)
        rooms_id = rooms_id_list.pop(0)
        last_room = queue.pop(0)
        print(f'Path {path}')

        if last_room == target:
            print(path)
            print("last_room", last_room)
            return moving_function(path, rooms_id)

        else:
            if last_room not in visited:
                visited.add(last_room)
                for d in visited_rooms[str(last_room)]:
                    if visited_rooms[str(last_room)][d] not in visited:
                        new_path = path.copy()
                        new_path.append(d)
                        new_rooms_id = rooms_id.copy()
                        new_rooms_id.append(visited_rooms[str(last_room)][d])
                        rooms_id_list.append(new_rooms_id)
                        print(f'new Path {new_path}')
                        paths.append(new_path)
                        queue.append(visited_rooms[str(last_room)][d])
            else:
                pass


# wise_map(visited_rooms)
# sell(player)
# moving_function(traversal_path, rooms_id_list=None)
room_search(visited_rooms, starting_room, mine)
