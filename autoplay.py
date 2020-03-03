# Initialize
import requests
import sys
import time
import math
import random
import pickle
import hashlib
from cpu import CPU

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
        with open('map.pickle', 'rb') as f:
            graph = pickle.load(f)
            print(f"Map contains {len(graph)} nodes.")
        print('Map loaded\n')
    except FileNotFoundError:
        graph = {}

    try:
        with open('500rooms.pickle', 'rb') as f:
            room_list = pickle.load(f)
        print('Map loaded\n')
    except FileNotFoundError:
        room_list = {}

    return graph, room_list


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

def travel_path(path):
    for room, step in path:
        travel(step, room)

def generate_path(destination, current_room, flipped_graph):
    # Create an empty queue
    q = Queue()
    # Add a PATH TO the starting vertex_id to the queue
    q.enqueue( [[current_room, None]] )
    #Create an empty set
    checked = set()
    # While the queue is not empty
    while q.size() > 0:
        #Dequeue the first path
        path = q.dequeue()
        # grab the last vertex from the path
        v = path[-1]
        # check if it's the target
        if v[0] == destination:
            # if so, return the path
            return [x for x in path[1:]]
        if v[0] not in checked:
            checked.add(v[0])
            for key, val in flipped_graph[v[0]].items():
                # make a copy of the path before adding
                path_copy = path.copy()
                path_copy.append([key, val])
                q.enqueue(path_copy)


def proof_of_work():
    """
    Simple Proof of Work Algorithm
    Stringify the block and look for a proof.
    Loop through possibilities, checking each one against `valid_proof`
    in an effort to find a number that is a valid proof
    :return: A valid proof for the provided block
    """
    response = requests.get('https://lambda-treasure-hunt.herokuapp.com/api/bc/last_proof/', headers=headers).json()
    last_proof = response['proof']
    difficulty = response['difficulty']
    print('---'*10)
    print(f"Mining coin for proof {last_proof} at difficulty {difficulty}...")
    # block_string = json.dumps(block, sort_keys=True)
    proof = 0

    while valid_proof(last_proof, proof, difficulty) is False:
        proof += 1
    
    # return proof
    data = '{"proof":' + str(proof) + '}'
    response = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/bc/mine/', headers=headers, data=data)
    return response.text

def valid_proof(last_proof, proof, difficulty):
    """
    Validates the Proof:  Does hash(block_string, proof) contain 6
    leading zeroes?  Return true if the proof is valid
    :param block_string: <string> The stringified block to use to
    check in combination with `proof`
    :param proof: <int?> The value that when combined with the
    stringified previous block results in a hash that has the
    correct number of leading zeroes.
    :return: True if the resulting hash is a valid proof, False otherwise
    """
    guess = str(last_proof) + str(proof)
    guess_encoded = guess.encode()
    guess_hash = hashlib.sha256(guess_encoded).hexdigest()
    
    if guess_hash[:difficulty] == '0' * difficulty:
        return True
    return False

def wish():
    data = '{"name":"Wishing Well"}'
    response = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/examine/', headers=headers, data=data).json()
    
    code = response['description'].split('\n')
    filename = 'wishing_well.txt'
    with open(filename, 'w') as f:
        for line in code[2:]:
            f.write(line)
            f.write('\n')

    ls8 = CPU()
    ls8.load(filename)
    next_room = ls8.run()

    print(f'\nMine found: {next_room}')
    return next_room

def status():
    return requests.get('https://lambda-treasure-hunt.herokuapp.com/api/adv/init/', headers=headers).json()


def keep_on_mining():
    while True:
        current_status = requests.get('https://lambda-treasure-hunt.herokuapp.com/api/adv/init/', headers=headers).json()
        location = current_status['room_id']

        if location != 55:
            path = generate_path(55, current_room, graph_reverse)
            travel_path(path)
            
        mine_room = wish()
        path = generate_path(mine_room, location, graph_reverse)
        travel_path(path)

        message = proof_of_work()
        print(message)

# Use load() to read in pickled files
graph, room_list = load()

graph_reverse = {}
for i in graph:
    graph_reverse[i] = {y: x for x, y in graph[i].items()}

# Init and display starting room
token = 'Token 6a879ef0d8d6851f96f1d1144cd3836007c07225'
url = 'https://lambda-treasure-hunt.herokuapp.com'
headers = {
    'Authorization': token,
}

response = requests.get(url + '/api/adv/init/', headers=headers).json()

print(response)

cooldown = response["cooldown"] # is this right?
exits = response['exits']
current_room = response['room_id']

wait(cooldown)

headers['Content-Type'] = 'application/json'

# Travel to a particular room
# path = generate_path(221, current_room, graph_reverse)
# travel_path(path)


# message = proof_of_work()
# print(message)
# path = generate_path(55, current_room, graph_reverse)
# travel_path(path)
keep_on_mining()