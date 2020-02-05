import requests
import os
import json
# from dotenv import load_dotenv
# load_dotenv()
from util import Graph, add_explored
from threading import Timer
import time

headers = {
'Authorization': 'Token d3f3a0266824458c28f1e36c817636085dcc3106',
'Content-Type': 'application/json'
}

node_headers = {
'Content-Type': 'application/json'
}

world_graph = Graph()

explored_rooms = set()

last_room_id = 0
world_graph.add_vertex(0,  "A brightly lit room",  "You are standing in the center of a brightly lit room. You notice a shop to the west and exits to the north, south and east.",  "(60,60)",  0,  "NORMAL",  [],  {'n':'?','e':'?','s':'?','w':'?'}, ["You have walked south."])
{explored_rooms.add(0)}
exits = {'n':'?','e':'?','s':'?','w':'?'}
direction = 's'

dir_reverse = {"n":"s","s":"n","e":"w","w":"e"}

while len(explored_rooms) < 500:

    contains_unexplored = False
    for i in exits:
        if exits[i] == '?':
            contains_unexplored = True
            direction = i
    if contains_unexplored is True:
        payloads = {"direction": direction}
        response = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/move/', data=json.dumps(payloads), headers=headers).json()
        print(response)
        exits = {}
        for d in response["exits"]:
            exits[d] = '?'
    
        exits[dir_reverse[direction]] = last_room_id
        
    
        if response["room_id"] not in explored_rooms:
            world_graph.add_vertex(response["room_id"],response["title"],response["description"],response["coordinates"],response["elevation"],response["terrain"],response ["items"],exits,response["messages"])
        
        world_graph.add_edge(last_room_id, direction, response["room_id"])
    
        cooldown = response["cooldown"]
        time.sleep(cooldown + 1)
        explored_rooms.add(response["room_id"])
        # r = Timer(cooldown + 1, add_explored, (explored_rooms,response["room_id"]))
        # r.start()
        last_room_id = response["room_id"]
    else:
        path = world_graph.unexplored_search(last_room_id)
        modified_path = []
        for index,i in enumerate(path):
            if index < len(path) - 1:
                current = i
                after = path[index+1]
                
                for q in world_graph.vertices[current]["exits"]:
                    if world_graph.vertices[current]["exits"][q] == after:
                        modified_path.append(q)
        
        while len(modified_path) > 0:
            bfsdir = modified_path.pop(0)
            print('about to move in this direction: ', bfsdir, " to: ", world_graph.vertices[last_room_id]["exits"][bfsdir])
            if world_graph.vertices[last_room_id]["exits"][bfsdir] != '?':
                payloads = {"direction": bfsdir, "next_room_id": str(world_graph.vertices[last_room_id]["exits"][bfsdir])}
                print('wise explorer activated, payload: ', payloads)
            else:
                payloads = {"direction": bfsdir}

            response = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/move/', data=json.dumps(payloads), headers=headers).json()
            print(response)
            cooldown = response["cooldown"]
            time.sleep(cooldown + 1)
            explored_rooms.add(response["room_id"])
            # r = Timer(cooldown + 1, add_explored, (explored_rooms,response["room_id"]))
            # r.start()
            last_room_id = response["room_id"]
        exits = world_graph.vertices[response["room_id"]]["exits"]

for i in world_graph.vertices:    
    post_room = requests.post('https://bw2rooms.herokuapp.com/api/room/addRoom', data=json.dumps(world_graph.vertices[i]),headers=node_headers).json()
    print(post_room)

# # Once done looping, add everything to database
