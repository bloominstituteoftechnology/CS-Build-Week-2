from decouple import config
from basic_utils import *
from miner import *
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
        self.fly = False
        self.dash = False
        self.important_rooms = {} # May not need this anymore (all special rooms are id'd)

    def get_info(self, what='init', direction=None, backtrack=None):
        """multi purpose move & init function - this is used
        for the most common actions"""

        if what == 'init':
            response = requests.get(f'{my_url}{what}/', headers=self.header)

        elif what == 'move':
            if self.fly and self.info['elevation']>0:
                response = requests.post(
                            f'{my_url}fly/', headers=self.header, json={"direction": direction})
            else:
                response = requests.post(
                    f'{my_url}move/', headers=self.header, json={"direction": direction})

        elif what == 'fly':
            response = requests.post(
                f'{my_url}fly/', headers=self.header, json={"direction": direction})

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

        if what == 'change_name':
            response = requests.post(
                f'{my_url}{what}/', headers=self.header, json={"name": name, "confirm": "aye"})
        
        if what == 'balance':
            response = requests.get(
                'https://lambda-treasure-hunt.herokuapp.com/api/bc/get_balance/', headers=self.header)

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

        if self.info['title'] == "shop":
            self.info = self.action('sell', item)
            self.info = self.action('confirm_sell')

    def create_starting_map(self):
        """"initiates your starting map which is stored under the vertices of a graph class"""
        info_dict = self.get_info()
        # print(info_dict)  # this can be deactivated - just helpful at first
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
            # May not need this anymore since all important rooms are id'd
            with open('rooms.txt', 'r') as file:
                string_dict = json.loads(file.read())
                for key in string_dict:
                    self.important_rooms[key] = string_dict[key]
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
        # May not need this anymore since all important rooms are id'd        
        self.important_rooms.update({info['title']: info['room_id']})
        if self.save_map_to_text:
            with open('rooms.txt', 'w') as file:
                file.write(json.dumps(self.important_rooms))

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
        counter is the number of times you want it to explore unknown rooms"""
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
        """Breadth First Traversal to particular room in shortest route"""
        print('moving')
        path = self.my_map.bfs(self.player.currentRoom, destination)
        for m in path:
            room = self.player.currentRoom
            exits = self.my_map.vertices[room]
            for direction in exits:
                if self.my_map.vertices[room][direction] == m:
                    self.get_info(what='move', direction=direction)
                    print(
                        f"Current Room -> Title: {self.info['title']} ID: {self.info['room_id']} Items: {self.info['items']}")
                else:
                    continue

    def dash_to_room(self, destination):
        "same as go to room but with dash"
        #print('dashing')
        path = self.my_map.bfs(self.player.currentRoom, destination)
        #print('bfs',path)
        my_dirs = self.get_dirs(path)
        i = 0
        while i < len(path)-1:
            if i < len(path)-2 and my_dirs[i]==my_dirs[i+1]:
                print('dashing')
                dash_path = self.get_dash_path(path[i:],my_dirs[i:])
                self.make_dash(my_dirs[i],dash_path[1:])
                print(f"Current Room -> Title: {self.info['title']} ID: {self.info['room_id']} Items: {self.info['items']}")
                i += len(dash_path[1:])
            else:
                print('normal walking')
                room = self.player.currentRoom
                exits = self.my_map.vertices[room]
                for direction in exits:
                    if self.my_map.vertices[room][direction] == path[i+1]:
                        #print('walk triggered',path[i+1],direction)
                        self.get_info(what='backtrack', direction=direction,backtrack=str(path[i+1]))
                        print(
                            f"Current Room -> Title: {self.info['title']} ID: {self.info['room_id']} Items: {self.info['items']}")
                           
                    else:
                        continue
                i+=1


    def get_dash_path(self,traversal,dirs):
        "check if the path in go to room contains a dashable stretch"
        print('dash path check',traversal,dirs)
        dash_list = []
        j = 0
        while (j<len(dirs)-1) and dirs[j]==dirs[j+1]:
            dash_list.append(traversal[j])
            j += 1
        dash_list.append(traversal[j])
        dash_list.append(traversal[j+1])
        #print('dash_list',dash_list)
        return dash_list

    def make_dash(self,direction,traversal):
        "make a dash given direction and traversal"
        string_rooms = ','.join([str(x) for x in traversal])
        params = {"direction":direction, "num_rooms":str(len(traversal)), 
                            "next_room_ids": string_rooms}
        print('dash_list_json',params,f'{my_url}dash/')
        response = requests.post(
                    f'{my_url}dash/', headers=self.header, json=params)

        if response.status_code == 200:
            self.info = json.loads(response.content)
            if self.player is not None:
                self.player.currentRoom = self.info['room_id']

            if 'cooldown' in self.info.keys():  
                time.sleep(self.info['cooldown'])

            self.room_check()
            return self.info
        else:
            print('cooldown triggered - waiting 20 seconds. code =',response.status_code,response.content)
            time.sleep(20)
            self.get_info(what=what, direction=direction, backtrack=backtrack)

    def pirate(self):
        # Goes directly to pirate ry
        self.go_to_room(467)
        time.sleep(self.wait)

    def wishing_well(self):
        # Goes directly to pirate ry
        self.go_to_room(55)
        time.sleep(self.wait)

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
            #! This request is being used to get information about our player from the lambda server.
            #! This would probably be better off initializing our local player attributes at the top, but
            #! I tried this first.
            url = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/status/'
            token = config('AUTH_KEY')
            headers = {'Authorization': f'Token {token}'}
            r = requests.post(url, headers=headers)
            ret_data = r.json()
            print('\n')
            print(f"***********Current Character Attributes***************")
            print(ret_data)
            print("*******************************************************")

            #!------------------------This name is specific to each person, be sure to change this to yours.
            if ret_data['name'] == 'player420' and ret_data['gold'] >= 1000:
                # Go to name changer (pirate ry)
                print('Time to Buy a Name')
                # * Made this false here so that we don't somehow pick up a ton of treasure on the way, and
                # * get over-encumbered.
                self.accumulate = False
                self.pirate()  # pirate ry's room
                time.sleep(self.wait)
                # Buy name
                #! -------------------------- Change the name here to be what you want!!
                self.action('change_name', name='SirSnuffaluffagus')
                time.sleep(self.wait)

                #! This print isn't accurate. It doesn't update when you actually change your name.
                #! Next time you see it, it should have changed though.
                print(f"Got a name! Time to get a COIN. New Name: {ret_data['name']}")
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

    def get_coins(self):
      # Want this to do 3 things:
      # Function to go to the wishing well and examine
      # Function to go to where the wishing well says
      # Function to mine coin at specified location
      # Could include if clause to go transmog coins

      coins = 0
      # variable for proof?
      while coins < 1000:
        # Go to wishing well
        print('Going to the Wishing Well.')
        self.wishing_well()
        # Examine well
        self.action('examine')
        # Go to where it says
        self.go_to_room('hinted location/room')
        # Mine Coin
        print('Getting proof...')
        response = request.post(f'https://lambda-treasure-hunt.herokuapp.com/api/bc/last_proof/', headers=self.headers)
        new_proof = proof_of_work(data.get('proof'), data.get('difficulty'))
        time.sleep(self.wait)
        # Need to send new_proof in the mine request json
        response = request.post(f'https://lambda-treasure-hunt.herokuapp.com/api/bc/mine/', headers=self.headers, json={"proof":''})
        print('You got a coin!')
        coins += 1
        time.sleep(self.wait)

    def hint_to_ld8(self):
        "converts hint in well to room number"
        self.action('examine','well')
        z = self.info['description']  #read the last info to get the hint
        z = z.split('\n')[2:]
        print(z)
        with open('hinter.ls8','w') as f:
            for zz in z:
                f.write("%s\n" % zz)
        #quicker way to parse message
        #z = [int(zz,2) for zz in z]
 

    def get_proof(self):
        """gets last proof then obtains proof of work
        then posts new proof to server"""
        print('Getting proof...')
        response = requests.get(f'https://lambda-treasure-hunt.herokuapp.com/api/bc/last_proof/', headers=self.header)
        self.last_proof = json.loads(response.content)
        print(self.last_proof)
        my_proof = proof_of_work(self.last_proof['proof'],self.last_proof['difficulty'])
        self.get_mine(my_proof)
        time.sleep(self.mine_response['cooldown'])
    
    def get_mine(self,new_proof):
        """posts your new proof to the server - note high cooldown penalties for posting wrong proof"""
        params = {"proof" : new_proof}
        response = requests.post(f'https://lambda-treasure-hunt.herokuapp.com/api/bc/mine/', headers=self.header,json = params)
        self.mine_response = json.loads(response.content)
        print(self.mine_response)

    def sell_all_items(self):
        """sells all items if you are in the shop"""
        self.action('status')
        inv = self.info['inventory']
        for i in inv:
            self.action('sell',i)
            self.action('confirm_sell',i)

    


