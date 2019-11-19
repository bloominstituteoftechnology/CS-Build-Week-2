from decouple import config
from basic_utils import *
import requests
import json
import time
import random
import os

auth_key = config('AUTH_KEY')  #MAKE SURE YPU HAVE .ENV SET UP 
my_url = config('LAMBDA_URL')  # AND PYTHON DECOUPLE INSTALLED

def keystoint(x):
    "function to change json dictionary keys to ints - used for map load"
    return {int(k): v for k, v in x.items()}

class Player:
    def __init__(self, name, startingRoom):
        self.name = name
        self.currentRoom = startingRoom

class mapper:
  def __init__(self,auth =auth_key,save = True, load_map= True):
    self.auth = auth  #the auth token
    self.header = {'Authorization':f'Token {self.auth}'}   #the header for post and get
    self.wait = 18  # the current sleep length - this is no longer required as wait always points to cooldown
    self.info = {}   #the last status json from post or get
    self.accumulate = False #whether player picks up items or not - it is very easy to get overencumbered
    self.pray = False #can't pray without a name unfortunately
    self.save_map_to_text = save  #save latest map to a text file
    self.import_text_map = load_map #import map so far - setting to false starts from scratch
    self.player = None

  def get_info(self,what='init',direction=None,backtrack=None):
    """multi purpose move & init function - this is used
    for the most common actions"""
  
    if what=='init':
      response = requests.get(f'{my_url}{what}/',headers=self.header) 

    elif what=='move':
      response = requests.post(f'{my_url}move/',headers=self.header,json = {"direction":direction})

    elif what=='backtrack':
      response = requests.post(f'{my_url}move/',headers=self.header,json = {"direction":direction,"next_room_id": backtrack})   

    if response.status_code==200:
      self.info = json.loads(response.content)
      if self.player is not None:
        self.player.currentRoom = self.info['room_id']

      if 'cooldown' in self.info.keys():  #there are a lot of TRAPS which require extra cooldown
          time.sleep(self.info['cooldown'])

      self.room_check()
      return self.info
    else:
      print('cooldown triggered - waiting 20 seconds')
      time.sleep(20)
      self.get_info(what=what,direction=direction,backtrack=backtrack)

  def action(self,what='take',treasure=None):
    """another multi purpose request function
    this one focuses on less common actions"""

    if what in ['take','drop','sell','examine']:
      response = requests.post(f'{my_url}{what}/',headers=self.header,json = {"name":treasure})

    if what in ['status','pray']:
      response = requests.post(f'{my_url}{what}/',headers=self.header)

    if what == 'confirm_sell':
      response = requests.post(f'{my_url}{what}/',headers=self.header,json = {"name":treasure, "confirm" : "yes"})

    if response.status_code==200:
      self.info = json.loads(response.content)
      if 'cooldown' in self.info.keys():
          time.sleep(self.info['cooldown'])
      return self.info
    else:
      print('error',what,treasure,response.status_code)

  def room_check(self):
    """checks for items in teh room or special rooms"""
    #print('room check triggered.  info: ',self.info)
    if self.info['items']!=[] and self.accumulate:
      for item in self.info['items']:

        self.info = self.action('take',item)
        print(self.info)

    if self.info['title'] == "Linh's Shrine" and self.pray:  #there may be other shrines
      self.info = self.action('pray')
    
  def create_starting_map(self):
    """"initiates your starting map which is stored under the vertices of a graph class"""
    info_dict = self.get_info()
    print(info_dict)   #this can be deactivated - just helpful at first
    self.my_map = Graph()
    self.player = Player("scooby_doo",info_dict['room_id'])
    exits = info_dict['exits']
    exit_dict = {}
    for e in exits:
      exit_dict[e] = '?'
    if self.import_text_map:
        print("load map triggered")
        with open('map.txt','r') as file:
            string_dict = json.loads(file.read())
            for key in string_dict:
                self.my_map.vertices[int(key)] = string_dict[key]
    else:
        print("fresh map triggered")
        self.my_map.vertices[self.player.currentRoom] = exit_dict
        
    return self.my_map,self.player

  def pop_map_on_move(self,move):
    """fills in the map while moving in the direction specified"""
    reverse_dir ={'n':'s','s':'n','w':'e','e':'w'}
    old_room = self.player.currentRoom
    info = self.get_info('move',move)
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
        with open('map.txt','w') as file:
            file.write(json.dumps(self.my_map.vertices))

  def count_unmapped(self):
    """counts all the unmapped rooms"""
    counter = 0
    for val1 in self.my_map.vertices.values():
      for val2 in val1.values():
        if val2=='?':
          counter += 1
    return counter
  
  def get_dirs(self,traversal):
    """gets the direction of travel given a room traversal list"""
    point = traversal[0]
    dir_list = []
    for t in traversal[1:]:
      for key in self.my_map.vertices[point]:
        if self.my_map.vertices[point][key]==t:
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

  def explore_random(self,counter=5):
    """explores the map choosing random ? and backtracks using bfs
    counter is the number of times you want it to explore unkown rooms"""
    unmapped_number = self.count_unmapped()
    moves = []
    c=0
    while unmapped_number > 0 and c <= counter:
      print(self.my_map.vertices)
      
      room = self.player.currentRoom
      unvisited_exits = [x for x in self.my_map.vertices[room] if self.my_map.vertices[room][x]=='?']
      if unvisited_exits !=[]:
        print('exit checker',unvisited_exits)
        move = random.choice(unvisited_exits)
        moves.append(move)
        self.pop_map_on_move(move)
        unmapped_number = self.count_unmapped()
        time.sleep(self.wait)
      else:   
        print('back track on') #leave this line in to show you when you are backtracking
        backtrack = self.bfs_for_q()
        backtrack_dirs = self.get_dirs(backtrack)
        print('backtrack details',backtrack,backtrack_dirs) #this line shows details of backtrack
        for i in range(len(backtrack_dirs)):
          b_info = self.get_info('backtrack',backtrack_dirs[i],str(backtrack[i+1]))
          self.player.currentRoom = b_info['room_id']
      c+=1

    def go_to_room(self,destination):
      """depth first traversal to particular room in shortest route
      NOT OPERATIONAL YET"""
      s = Stack()
      s.push([self.player.currentRoom])
      
      while destination not in s.stack[-1]:
        current_point = s.stack[-1][-1]
        
        joins = self.my_map.vertices[current_point]
        if joins is None:
          s.pop()
        else:
          temp_list = []
          for j in joins:
            _ = [x for x in s.stack[-1]]
            _.append(j)
            temp_list.append(_)
          for tl in temp_list:
            s.push(tl)

      return s.stack[-1]

