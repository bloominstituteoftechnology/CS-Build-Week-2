import requests
import json
import time
from time import sleep
import random
import sys
my_token = sys.argv[1]


class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


def move(direction, wise_travel = None):
    if wise_travel == None:
        r = requests.post(
            "https://lambda-treasure-hunt.herokuapp.com/api/adv/move/",
            data = json.dumps({"direction": direction}),
            headers = {
                "Authorization": my_token,
                "Content-Type": "application/json"
            }
        )
    else:
        r = requests.post(
            "https://lambda-treasure-hunt.herokuapp.com/api/adv/move/",
            data = json.dumps({
                "direction": direction,
                "next_room_id": wise_travel
                }),
            headers = {
                "Authorization": my_token,
                "Content-Type": "application/json"
            }
        )
    return r.json()


def reverse_dict(dictionary):
    return {str(v): str(k) for k, v in dictionary.items()}


def bfs(start):
    print(f"\tStarting BFT at: {start}")
    q = Queue()
    q.enqueue([start])
    visited = set()
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        print(f"\tExits from current vertex: {v} {traversial_graph[v]}")
        if v not in visited:
            if '?' in list(traversial_graph[v].values()):
                print("\tFound one")
                return path
            print("\tNo unexplored paths here")
            visited.add(v)
            for neighbor in list(traversial_graph[v].values()):
                new_path = list(path)
                new_path.append(str(neighbor))
                q.enqueue(new_path)
    return None



"""
# Uncomment to start from scratch
r = requests.get(
    "https://lambda-treasure-hunt.herokuapp.com/api/adv/init/",
    headers = {"Authorization": my_token}
)
starting_room = dict(r.json())
sleep(starting_room['cooldown'])
# Create a dictionary of rooms and a dictionary of room info
traversial_graph = {
    str(starting_room['room_id']):
        dict.fromkeys(starting_room['exits'], '?')
}

room_infomation = {starting_room['room_id']: starting_room}
current = starting_room
"""

with open("room_map.json", "r") as f:
    traversial_graph = json.load(f)
    f.close()

with open('room_info.json', 'r') as f:
    room_infomation = json.load(f)
    f.close()


done = False
iter = 0
current = room_infomation[random.choice(list(traversial_graph.keys()))]
print(f"Starting at room :{current}")

while done == False:

    # Pick a random unexplored direction
    print(type(list(traversial_graph.keys())[0]))
    print(traversial_graph[str(current['room_id'])])
    if type(list(traversial_graph.keys())[0]) == str:
        possible_moves = [i for i in traversial_graph[str(current['room_id'])]\
                            if traversial_graph[str(current['room_id'])][i] == '?']
    else:
        possible_moves = [i for i in traversial_graph[current['room_id']]\
                            if traversial_graph[current['room_id']][i] == '?']
    print(f"Can move {possible_moves}")

    if len(possible_moves) > 0:
        move_choice = random.choice(possible_moves)
        print(f"Let's go {move_choice}")

        # Travel to that room Sleep for the cooldown and log the direction
        previous_room_id = str(current['room_id'])
        current = move(move_choice)
        print(current)
        print(f"We're in room {current['room_id']}")
        print(f"Waiting: {current['cooldown']}")
        sleep(current['cooldown'])
        print(f"Previous {traversial_graph[previous_room_id]}")
        traversial_graph[previous_room_id][move_choice] = str(current['room_id'])
        print(f"Updated {traversial_graph[previous_room_id]}")
        room_infomation[str(current['room_id'])] = current

        # If the room isn't in traversial_graph
        if str(current['room_id']) not in list(traversial_graph.keys()):
            # Add room to the traversial_graph
            traversial_graph[str(current['room_id'])] = dict.fromkeys(
                                                current['exits'], '?')

        if move_choice == 'n':
            traversial_graph[str(current['room_id'])]['s'] = previous_room_id
            print(f"South of {current['room_id']} is {previous_room_id}")
        elif move_choice == 's':
            traversial_graph[str(current['room_id'])]['n'] = previous_room_id
            print(f"North of {current['room_id']} is {previous_room_id}")
        elif move_choice == 'e':
            traversial_graph[str(current['room_id'])]['w'] = previous_room_id
            print(f"West of {current['room_id']} is {previous_room_id}")
        elif move_choice == 'w':
            traversial_graph[str(current['room_id'])]['e'] = previous_room_id
            print(f"East of {current['room_id']} is {previous_room_id}")

    else:
        # find the shortest path to a room with an unexplored path
        print("Looks like we know all the exits of this room")
        print("Lets find a room with unexplored exits")
        short_path = bfs(str(current['room_id']))
        print(f"Here is our path: {short_path}")
        if short_path == None:
            break

        directed_path = []
        for i in range(len(short_path) + 1):
            if i + 1 < len(short_path):
                direction = reverse_dict(
                    traversial_graph[str(short_path[i])])[short_path[i+1]]
                directed_path.append(direction)

        # Travel along that path and sleep for the cooldown
        print(f"Here is our path to an unexplored room {directed_path}")
        for i in range(len(directed_path)):
            previous_room_id = str(current['room_id'])
            current = move(directed_path[i], wise_travel = short_path[i])
            print(f"Waiting: {current['cooldown']}")
            sleep(current['cooldown'])

        # If the room isn't in traversial_graph
        if str(current['room_id']) not in list(traversial_graph.keys()):
            # Add room to the traversial_graph
            traversial_graph[str(current['room_id'])] = dict.fromkeys(
                                                current['exits'], '?')


    # Iteration
    values = []
    for adj_dict in list(traversial_graph.values()):
        for i in list(adj_dict.values()):
            values.append(i)

    if '?' in values or len(traversial_graph) != 500:
        done = False
    else:
        done = True
    iter += 1
    # Data save
    if iter % 1 == 0:
        exit_record = open("room_map.json", "w+")
        exit_record.write(json.dumps(traversial_graph))
        exit_record.close()
        info_data = open("room_info.json", "w+")
        info_data.write(json.dumps(room_infomation))
        info_data.close()
