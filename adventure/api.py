from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from decouple import config
from django.contrib.auth.models import User
from .models import *
from rest_framework.decorators import api_view
import json
import math
from random import random
from threading import Timer

@csrf_exempt
@api_view(["GET"])
def initialize(request):
    user = request.user
    player = user.player
    player_id = player.id
    uuid = player.uuid
    room = player.room()
    nextRooms = [{'n': room.n_to}, {'e': room.e_to},
                 {'s': room.s_to}, {'w': room.w_to}]
    players = room.playerNames(player_id)


    return JsonResponse({'uuid': uuid, 'name': player.user.username, 'title': room.title, 'roomId': room.id, 'description': room.description, 'nextRooms': nextRooms, 'players': players}, safe=True)

@csrf_exempt
@api_view(["POST"])
def move(request):
    dirs = {"n": "north", "s": "south", "e": "east", "w": "west"}
    reverse_dirs = {"n": "south", "s": "north", "e": "west", "w": "east"}
    player = request.user.player
    player_id = player.id
    player_uuid = player.uuid
    data = json.loads(request.body)
    direction = data['direction']
    room = player.room()
    
@csrf_exempt
@api_view(["POST"])
def graph(request):
    data = json.loads(request.body)
    print(request)