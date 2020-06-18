import json
from path import my_dict as path
from graph import Graph
g = Graph()
import requests
import sys
import random
from util import Stack, Queue
import copy
import time
import math
import json
import zmq
from cpu import CPU
from mine import valid_proof, proof_of_work
import itertools



context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
while True:
    message = socket.recv()
    room = open("snitch_room.txt","r").readline()
    # print(f.readline())
    socket.send_string(room)