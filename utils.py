from decouple import config
from basic_utils import *
import requests
import json
import time
import random

auth_key = config('AUTH_KEY')
my_url = config('LAMBDA_URL')

class Player:
    def __init__(self, name, startingRoom):
        self.name = name
        self.currentRoom = startingRoom

class mapper:
  def __init__(self,auth ='827d98231059f187c4203da53476090d1c83a2b9'):
    self.auth = auth  #the auth token
    self.header = {'Authorization':f'Token {self.auth}'}   #the header for post and get
    self.wait = 18  # the current sleep length
    self.info = {}   #the last status json from post or get
    self.accumulate = False #whether player picks up items or not - it ise very easy to get overencumbered

  def get_info(self,what='init',direction=None,backtrack=None):
    """multi purpose move & init function"""
    #info = !curl -X GET -H 'Authorization: Token 827d98231059f187c4203da53476090d1c83a2b9' https://lambda-treasure-hunt.herokuapp.com/api/adv/init/
    if what=='init':
      response = requests.get(f'{my_url}{what}/',headers=self.header) 

    elif what=='move':
      response = requests.post(f'{my_url}move/',headers=self.header,json = {"direction":direction})

    elif what=='backtrack':
      response = requests.post(f'{my_url}move/',headers=self.header,json = {"direction":direction,"next_room_id": backtrack})   

    if response.status_code==200:
      self.info = json.loads(response.content)
      if self.info['terrain'] == 'TRAP':
          time.sleep(30)
      self.room_check()
      return self.info
    else:
      print('cooldown triggered - waiting 20 seconds')
      time.sleep(20)
      self.get_info(what=what,direction=direction,backtrack=backtrack)

  def action(self,what='take',treasure=None):
    """another multi purpose request function"""

    if what in ['take','drop','sell','examine']:
      response = requests.post(f'{my_url}{what}/',headers=self.header,json = {"name":treasure})

    if what in ['status','pray']:
      response = requests.post(f'{my_url}{what}/',headers=self.header)

    if what == 'confirm_sell':
      response = requests.post(f'{my_url}{what}/',headers=self.header,json = {"name":treasure, "confirm" : "yes"})

    if response.status_code==200:
      self.info = json.loads(response.content)
      return self.info
    else:
      print('error',what,treasure,response.status_code)

  def room_check(self):
    print('room check triggered.  info: ',self.info)
    if self.info['items']!=[] and self.accumulate:
      for item in self.info['items']:
        time.sleep(self.wait)
        self.info = self.action('take',item)
        print(self.info)
        time.sleep(self.info['cooldown'])

    if self.info['title'] == 'Shrine':
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
    self.my_map.vertices[self.player.currentRoom] = exit_dict
    return self.my_map,self.player

  def pop_map_on_move(self,move):
    """fills in the map while moving in the direction specified"""
    reverse_dir ={'n':'s','s':'n','w':'e','e':'w'}
    old_room = self.player.currentRoom
    info = self.get_info('move',move)
    self.player.currentRoom = info['room_id']
    print(info)  #another debugger
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
        print('back track on') 
        backtrack = self.bfs_for_q()
        #print('backtrack is', backtrack)
        backtrack_dirs = self.get_dirs(backtrack)
        print('backtrack details',backtrack,backtrack_dirs)
        for i in range(len(backtrack_dirs)):
          b_info = self.get_info('backtrack',backtrack_dirs[i],str(backtrack[i+1]))
          self.player.currentRoom = b_info['room_id']
          time.sleep(self.wait)
      c+=1

    def go_to_room(self,destination):
      """depth first traversal to particular room in shortest route"""
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

