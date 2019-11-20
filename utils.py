from decouple import config
from basic_utils import *
import requests
import json
import time
import random
import os

auth_key = config('AUTH_KEY')  # MAKE SURE YPU HAVE .ENV SET UP
my_url = config('LAMBDA_URL')  # AND PYTHON DECOUPLE INSTALLED
my_name = config('NAME')  # when to change name


def keystoint(x):
    "function to change json dictionary keys to ints - used for map load"
    return {int(k): v for k, v in x.items()}


class Player:
    def __init__(self, name, startingRoom):
        self.name = name
        self.currentRoom = startingRoom
        self.player_cooldown = 1,
        self.player_encumbrance = 0,
        self.player_strength = 0,
        self.player_speed = 0,
        self.player_gold = 0,
        self.player_inventory = [],
        self.player_status = [],
        self.player_errors = [],
        self.player_messages = []
        self.player_mine = ''


class mapper:
    def __init__(self, auth=auth_key, save=True, load_map=True):
        self.auth = auth  # the auth token
        # the header for post and get
        self.header = {'Authorization': f'Token {self.auth}'}
        self.wait = 18  # the current sleep length - this is no longer required as wait always points to cooldown
        self.info = {}  # the last status json from post or get
        # whether player picks up items or not - it is very easy to get overencumbered
        self.accumulate = False
        self.pray = False  # can't pray without a name unfortunately
        self.save_map_to_text = save  # save latest map to a text file
        # import map so far - setting to false starts from scratch
        self.import_text_map = load_map
        self.player = None

    def get_info(self, what='init', direction=None, backtrack=None):
        """multi purpose move & init function - this is used
        for the most common actions"""

        if what == 'init':
            response = requests.get(f'{my_url}{what}/', headers=self.header)

        elif what == 'move':
            response = requests.post(
                f'{my_url}move/', headers=self.header, json={"direction": direction})

        elif what == 'backtrack':
            response = requests.post(f'{my_url}move/', headers=self.header,
                                     json={"direction": direction, "next_room_id": backtrack})

        if response.status_code == 200:
            self.info = json.loads(response.content)
            if self.player is not None:
                self.player.currentRoom = self.info['room_id']

            if 'cooldown' in self.info.keys():  # there are a lot of TRAPS which require extra cooldown
                time.sleep(self.info['cooldown'])

            self.room_check()
            return self.info
        else:
            print('cooldown triggered - waiting 20 seconds')
            time.sleep(20)
            self.get_info(what=what, direction=direction, backtrack=backtrack)

    def action(self, what='take', treasure=None, name=None):
        """another multi purpose request function
        this one focuses on less common actions"""

        if what in ['take', 'drop', 'sell', 'examine']:
            response = requests.post(
                f'{my_url}{what}/', headers=self.header, json={"name": treasure})
            print(f"Action: {what}")

        if what in ['status', 'pray']:
            response = requests.post(f'{my_url}{what}/', headers=self.header)

        if what == 'confirm_sell':
            response = requests.post(
                f'{my_url}{what}/', headers=self.header, json={"name": treasure, "confirm": "yes"})

        # Change Name +++++++
        if what == 'change_name':
            response = requests.post(
                f'{my_url}{what}/', headers=self.header, json={"name": name, "confirm": "aye"})

        if response.status_code == 200:
            self.info = json.loads(response.content)
            if 'cooldown' in self.info.keys():
                time.sleep(self.info['cooldown'])
            return self.info
        else:
            print('error', what, treasure, response.status_code)

    def room_check(self):
        """checks for items in teh room or special rooms"""
        # print('room check triggered.  info: ',self.info)
        if self.info['items'] != [] and self.accumulate:
            for item in self.info['items']:
                # Examines the item
                self.info = self.action('examine', item)
                print(self.info)
                self.info = self.action('take', item)
                print(self.info)

        if self.info['title'] == "Linh's Shrine" and self.pray:  # there may be other shrines
            self.info = self.action('pray')

            # Would this sell? ++++++
        if self.info['title'] == "shop":
            self.info = self.action('sell', item)
            self.info = self.action('confirm_sell')

        # Could this do the name change? +++++++
        # if self.info['title'] == "Pirate Ry's":
        #   self.info = self.action('change_name', name)
        #   self.info = self.action('confirm_name')

    def create_starting_map(self):
        """"initiates your starting map which is stored under the vertices of a graph class"""
        info_dict = self.get_info()
        print(info_dict)  # this can be deactivated - just helpful at first
        self.my_map = Graph()
        self.player = Player("MicahJones", info_dict['room_id'])
        exits = info_dict['exits']
        exit_dict = {}
        for e in exits:
            exit_dict[e] = '?'
        if self.import_text_map:
            print("load map triggered")
            with open('map.txt', 'r') as file:
                string_dict = json.loads(file.read())
                for key in string_dict:
                    self.my_map.vertices[int(key)] = string_dict[key]
        else:
            print("fresh map triggered")
            self.my_map.vertices[self.player.currentRoom] = exit_dict

        return self.my_map, self.player

    def pop_map_on_move(self, move):
        """fills in the map while moving in the direction specified"""
        reverse_dir = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}
        old_room = self.player.currentRoom
        info = self.get_info('move', move)
        self.player.currentRoom = info['room_id']
        print(info)  # leave this line in to get movement updates
        new_room = info['room_id']
        if new_room not in self.my_map.vertices:
            exit_dict = {}
            for exits in info['exits']:
                for e in exits:
                    exit_dict[e] = '?'
            self.my_map.vertices[new_room] = exit_dict
        self.my_map.vertices[old_room][move] = new_room
        reverse_move = reverse_dir[move]
        self.my_map.vertices[new_room][reverse_move] = old_room
        if self.save_map_to_text:
            with open('map.txt', 'w') as file:
                file.write(json.dumps(self.my_map.vertices))

    def count_unmapped(self):
        """counts all the unmapped rooms"""
        counter = 0
        for val1 in self.my_map.vertices.values():
            for val2 in val1.values():
                if val2 == '?':
                    counter += 1
        return counter

    def get_dirs(self, traversal):
        """gets the direction of travel given a room traversal list"""
        point = traversal[0]
        dir_list = []
        for t in traversal[1:]:
            for key in self.my_map.vertices[point]:
                if self.my_map.vertices[point][key] == t:
                    dir_list.append(key)
            point = t
        return dir_list

    def bfs_for_q(self):
        """breadth first search for last ?"""
        room = self.player.currentRoom
        q = Queue()
        q.enqueue([room])

        while '?' not in self.my_map.vertices[room].values():

            joins = self.my_map.vertices[room]
            for j in joins.values():
                if j in q.queue[0]:
                    pass
                else:
                    _ = [x for x in q.queue[0]]
                    _.append(j)
                    q.enqueue(_)
            q.dequeue()
            room = q.queue[0][-1]

        return q.queue[0]

    def explore_random(self, counter=5):
        """explores the map choosing random ? and backtracks using bfs
        counter is the number of times you want it to explore unkown rooms"""
        unmapped_number = self.count_unmapped()
        moves = []
        c = 0
        while unmapped_number > 0 and c <= counter:
            print(self.my_map.vertices)

            room = self.player.currentRoom
            unvisited_exits = [x for x in self.my_map.vertices[room]
                               if self.my_map.vertices[room][x] == '?']
            if unvisited_exits != []:
                print('exit checker', unvisited_exits)
                move = random.choice(unvisited_exits)
                moves.append(move)
                self.pop_map_on_move(move)
                unmapped_number = self.count_unmapped()
                time.sleep(self.wait)
            else:
                # leave this line in to show you when you are backtracking
                print('back track on')
                backtrack = self.bfs_for_q()
                backtrack_dirs = self.get_dirs(backtrack)
                # this line shows details of backtrack
                print('backtrack details', backtrack, backtrack_dirs)
                for i in range(len(backtrack_dirs)):
                    b_info = self.get_info(
                        'backtrack', backtrack_dirs[i], str(backtrack[i+1]))
                    self.player.currentRoom = b_info['room_id']
            c += 1

    def go_to_room(self, destination):
        """depth first traversal to particular room in shortest route
        NOT OPERATIONAL YET"""
        # self.accumulate = False
        print('moving')
        path = self.my_map.bfs(self.player.currentRoom, destination)
        # print(f'Path: {path}')
        for m in path:
            room = self.player.currentRoom
            # print(f'Room: {type(room)}')
            exits = self.my_map.vertices[room]
            # print(f'Room: {room}')
            for direction in exits:
                if self.my_map.vertices[room][direction] == m:
                    # print(f'direction: {direction}')
                    self.get_info(what='move', direction=direction)
                    print(
                        f"Current Room -> Title: {self.info['title']} ID: {self.info['room_id']} Items: {self.info['items']}")
                else:
                    # print(f'go_to_room FAILED: Invalid Direction[{direction}], Room[{room}]')
                    continue
        # self.accumulate = True

    def pirate(self):
        # Goes directly to pirate ry
        # self.go_to_room(self.important_rooms['pirate ry'])
        # time.sleep(self.wait)
        pass

    def wishing_well(self):
        # Goes directly to pirate ry
        # self.go_to_room(self.important_rooms['wishing well'])
        # time.sleep(self.wait)
        pass

    def vendor(self):
        # Goes directly to the shop
        self.go_to_room(1)
        time.sleep(self.wait)

    # Method to get treasure
    # BFS Randomly to travel the maze, looting
    # Once you get enough treasure, go sell
    # Once you reach 1000 gold, buy a name
    # Change name to something unique, that doesnt contain player
    # Keep looting and selling until stopped.
    def get_treasure(self):
        while True:
            # get a name

            #! This request is being used to get information about our player from the lambda server.
            #! This would probably be better off initializing our local player attributes at the top, but
            #! I tried this first.
            url = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/status/'
            token = config('AUTH_KEY')
            headers = {'Authorization': f'Token {token}'}
            r = requests.post(url, headers=headers)
            ret_data = r.json()

            print(f"***********Current Character Attributes***************")
            print(ret_data)
            print("*******************************************************")

            #!------------------------This name is specific to each person, be sure to change this to yours.
            if ret_data['name'] == 'player446' and ret_data['gold'] >= 1000:
                # Go to name changer (pirate ry)
                print('Time to Buy a Name')
                # * Made this false here so that we don't somehow pick up a ton of treasure on the way, and
                # * get over-encumbered.
                self.accumulate = False
                self.go_to_room(467)  # pirate ry's room
                time.sleep(self.wait)
                # Buy name
                #! -------------------------- Change the name here to be what you want!!
                self.action('change_name', name='Micah')
                time.sleep(self.wait)

                #! This print isn't accurate. It doesn't update when you actually change your name.
                #! Next time you see it, it should have changed though.
                print(
                    f"Got a name! Time to get a COIN. New Name: {ret_data['name']}")
                time.sleep(self.wait)
                # self.action('status') #Check new name
            elif ret_data['encumbrance'] <= ret_data['strength'] - 2:
                # If encumbered is str-2 (at base = 8)
                # Travel the room bfs style at random
                # Loot as you go with room_check
                print('Looting..')
                # * accumlate is true here since that's the whole point of this block
                self.accumulate = True

                # self.explore_random(500)
                self.go_to_room(random.randint(0, 499))
                print('Current Inventory: ', ret_data['inventory'])
                time.sleep(self.wait)
            # Could potentially add a section to manage miner
            else:
                # else go directly to the shop
                # loop through inventory and sell
                # Go back to looting
                print('Need to offload my loot.')
                # * Setting accumulate to false so we don't get overburdening on the way to shop.
                self.accumulate = False
                self.vendor()
                print('At the shop, time to sell.')
                for item in ret_data['inventory']:
                    print(f"Selling {item}...")
                    self.action('sell', item)
                    time.sleep(self.wait)
                    self.action('confirm_sell', item)
                    time.sleep(self.wait)
                    # This doesn't actually update after each sell for some reason.
                    print(f"You're current gold: {ret_data['gold']}")
                print('Back to Looting')


"""
need a function to go to name changer and buy a name.
funciton to go to wishing well and interact
function to go to where wishing well says and mine a coin

SHOP is in room id 1
Name changer is in 467
Well is 55

"""
