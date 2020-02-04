import requests
import os
# from dotenv import load_dotenv
# load_dotenv()
from util import Graph, add_explored
from threading import Timer

headers = {
'Authorization': 'Token d3f3a0266824458c28f1e36c817636085dcc3106',
'Content-Type': 'application/json',
}

world_graph = Graph()

explored_rooms = set()

last_room = 0

world_graph.add_vertex(0,  "A brightly lit room",  "You are standing in the center of a brightly lit room. You notice a shop to the west and exits to the north, south and east.",  "(60,60)",  0,  "NORMAL",  [],  ['?','?','?','?'], ["You have walked south."])

# while len(explored_rooms) < 500:
    
#     direction = response[""]

#     data = {"direction":direction}

#     response = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/move/', headers=headers, data=data)

#     exits = response["exits"]

#     if response["room_id"] not in explored_rooms:
#         world_graph.add_vertex(response["room_id"],response["title"],response["description"],response["coordinates"],response["elevation"],response["terrain"],response["items"],exits,response["messages"])

#     cooldown = response["cooldown"]

#     r = Timer(cooldown + 1, add_explored, (explored_rooms,response["room_id"]))

#     last_room = response["room_id"]

# Once done looping, add everything to database

print(world_graph.vertices[0]["exits"])
