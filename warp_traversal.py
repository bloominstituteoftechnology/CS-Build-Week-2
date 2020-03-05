# Initialize
import requests
import sys
import time
import math
import random
import pickle

token = 'Token 6a879ef0d8d6851f96f1d1144cd3836007c07225'
url = 'https://lambda-treasure-hunt.herokuapp.com'
headers = {
    'Authorization': token,
}

response = requests.get(url + '/api/adv/init/', headers=headers).json()

print(response)

cooldown = response["cooldown"] # is this right?
exits = response['exits']

time.sleep(cooldown)

headers['Content-Type'] = 'application/json'

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

def load():
    print('Checking if map saved...')

    try:
        with open('warp_map.pickle', 'rb') as f:
            graph = pickle.load(f)
            print(f"Map contains {len(graph)} nodes.")
        print('Map loaded\n')
    except FileNotFoundError:
        graph = {}

    try:
        with open('warp_rooms.pickle', 'rb') as f:
            room_list = pickle.load(f)
        print('Map loaded\n')
    except FileNotFoundError:
        room_list = {}

    return graph, room_list

def backtrack_path(graph, current_room):
    '''
    Use BFS to find the closest room with unexplored exits
    Return a path from the current room to the target room
    Path is a list of directions
    '''
    
    # Create an empty queue
    q = Queue()
 
    # Add a PATH TO the starting vertex_id to the queue
    q.enqueue( [(current_room, None)] )
    #Create an empty set
    visited = set()
    # While the queue is not empty
    while q.size() > 0:
        #Dequeue the first path
        path = q.dequeue()
        # grab the last vertex from the path
        v = path[-1][0]
        # check if it's the target
        if '?' in graph[v].values():
            # if so, return the path
            path = [i[1] for i in path[1:]]
            print()
            print(f"Path: {path}")
            return path
        if v not in visited:
            visited.add(v)
            for key, val in graph[v].items():
                # make a copy of the path before adding
                path_copy = path.copy()
                # print(f"Path copy: {path_copy}")
                path_copy.append((val, key))
                q.enqueue(path_copy)

def unexplored_exits(graph, current_room_id):
    return [k for k, v in graph[current_room_id].items() if v=='?']

def wait(cooldown):
    cooldown = math.ceil(cooldown)
    
    for i in range(0, cooldown):
        print(f'Remaining cooldown: {cooldown - i}...', end="\r")
        time.sleep(1)

def print_direction(direction):
    print('---' * 10)
    print(f"You move to the {direction}")
    print('---'*10)

def travel(direction, room=None):
    if room is not None:
        data = {"direction": f'{direction}', "next_room_id": f"{room}"}
        # data = '{"direction":"' + direction + '"}'
    else:
        data = {"direction": f'{direction}'}

    response = requests.post(url + '/api/adv/move/', headers=headers, json=data).json()
    cooldown = response["cooldown"]
    
    print_direction(direction)
    print(response)

    wait(cooldown)
    return(response)

# Use load() to read in pickled files
graph, room_list = load()

visited = set()
traversal_path = []
opposite = {'s': 'n', 'n': 's', 'w': 'e', 'e': 'w'}

source = None 
old_room = None
no_back = True

# moving = True
# while len(visited) < 10:
while len(graph) < 500:
    # Mark current room as visited
    current_room = response['room_id']
    exits = response['exits']
    visited.add(current_room)

    if current_room not in graph:
        graph[current_room] = {}
        for e in exits:
            graph[current_room][e] = '?'
    
    print(f"Your map has {len(graph)} rooms")

    if current_room not in room_list:
        room_list[current_room] = response

    if len(visited) == 500:
        break

    if len(visited) % 25 == 0:
        with open('warp_map.pickle', 'wb') as f:
            pickle.dump(graph, f)
        with open('warp_rooms.pickle', 'wb') as f:
            pickle.dump(room_list, f)
    
    unexplored_exits_list = unexplored_exits(graph, current_room)

    # randomly select an exit and travel in that direction
    if len(unexplored_exits_list)>0:
        # Pick a random unexplored direction and travel that way
        direction = random.choice(unexplored_exits_list)
        previous_room = current_room
        if graph[current_room][direction] != '?':
            room = graph[current_room][direction]
            response = travel(direction, room)
        else:
            response = travel(direction)
        current_room = response['room_id']
        exits = response['exits']

        if current_room not in graph:
            graph[current_room] = {}
            for e in exits:
                graph[current_room][e] = '?'
        
        graph[previous_room][direction] = current_room
        graph[current_room][opposite[direction]] = previous_room

        traversal_path.append(direction) 

    else:
        print()
        print("Backtracking...")
        backtrack_path_list = backtrack_path(graph, current_room)
        print(f"Backtrack list: {backtrack_path_list}")
        for d in backtrack_path_list:
            current_room = response['room_id']
            if graph[current_room][d] != '?':
                room = graph[current_room][d]
                response = travel(d, room)
            else:
                response = travel(d)
            # travel(d)
            traversal_path.append(d)
        # no_back = False

print(graph)
print('Map complete!\n')
with open('warp_map.pickle', 'wb') as f:
    pickle.dump(graph, f)
with open('warp_rooms.pickle', 'wb') as f:
    pickle.dump(room_list, f)
print(traversal_path)