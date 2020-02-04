import pandas as pd
import json
import requests
from .utils import *

df = pd.read_json("https://raw.githubusercontent.com/build-week-pt2/CS-Build-Week-2/matt/room_info.json").T

shop = df['title'] == 'Shop'
Glasowyn_Grave = df['title'] == "Glasowyn's Grave"
Arron_Athenaeum = df['title'] == "Arron's Athenaeum"
Fully_Shrine = df['title'] == "Fully Shrine"
Sandofsky_Sanctum = df['title'] == "Sandofsky's Sanctum"
brightly_lit_room = df['title'] == "A brightly lit room"
Wishing_Well = df['title'] == "Wishing Well"
Linh_Shrine = df['title'] == "Linh's Shrine"
The_Transmogriphier = df['title'] == "The Transmogriphier"
Peak_Mt_Holloway = df['title'] == "The Peak of Mt. Holloway"
Pirate_Ry = df['title'] == "Pirate Ry's"

special_rooms = df[shop | Glasowyn_Grave | Arron_Athenaeum | Fully_Shrine | Sandofsky_Sanctum | brightly_lit_room | Wishing_Well | Linh_Shrine | The_Transmogriphier | Peak_Mt_Holloway | Pirate_Ry]


r = requests.get("https://raw.githubusercontent.com/build-week-pt2/CS-Build-Week-2/matt/room_map.json")
traversial_graph = dict(r.json())

def path_dict(start_id, end_id):
    short_path = bfs(str(start_id), str(end_id))
    directed_path = []
    for i in range(len(short_path) + 1):
        if i + 1 < len(short_path):
            direction = reverse_dict(
                traversial_graph[str(short_path[i])])[short_path[i+1]]
            directed_path.append(direction)
    return dict(zip(short_path, directed_path))

special_rooms['room_id'].to_list()

paths = {}
starting_room = 254
for i in range(len(special_rooms)):
  paths[special_rooms['title'].to_list()[i]] = path_dict(starting_room, special_rooms['room_id'].tolist()[i])

"""
#uncomment to export
special_rooms = open("special_rooms.json", "w+")
special_rooms.write(json.dumps(paths))
special_rooms.close()
"""
