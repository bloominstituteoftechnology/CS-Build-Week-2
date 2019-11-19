from connection import connections
import requests
import time
import os
import json
from dotenv import load_dotenv
load_dotenv()


currentRoom = None
cooldown = 0
visitedIds = set()
count = 0
roomsInfo = []


def traverse():

    goBackCache = []

    while len(visitedIds) < 500:

        connection = connections[str(currentRoom['room_id'])][1]

        if 'n' in currentRoom['exits'] and connection['n'] not in visitedIds:
            goBackCache.append('s')
            move('n')

        elif 'e' in currentRoom['exits'] and connection['e'] not in visitedIds:
            goBackCache.append('w')
            move('e')

        elif 's' in currentRoom['exits'] and connection['s'] not in visitedIds:
            goBackCache.append('n')
            move('s')

        elif 'w' in currentRoom['exits'] and connection['w'] not in visitedIds:
            goBackCache.append('e')
            move('w')

        elif len(visitedIds) < 500:
            while len(goBackCache) > 0:

                direction = goBackCache.pop()
                move(direction)
                connection = connections[str(currentRoom["room_id"])][1]

                if 'n' in currentRoom['exits'] and connection['n'] not in visitedIds or 'e' in currentRoom['exits'] and connection['e'] not in visitedIds or 's' in currentRoom['exits'] and connection['s'] not in visitedIds or 'w' in currentRoom['exits'] and connection['w'] not in visitedIds:
                    break
        else:
            break


def move(dir):

    time.sleep(cooldown)

    try:
        res = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/move/',
                        headers={'Authorization': str(os.getenv('authToken'))},
                        json={'direction': dir, 'next_room_id': str(connections[str(currentRoom["room_id"])][1][dir])}
                        )
        res.raise_for_status()
    except Exception as err:
        print(err)

    handleRes(res)


def init():
    res = requests.get('https://lambda-treasure-hunt.herokuapp.com/api/adv/status/api/adv/init/',
                       headers={'Authorization': str(os.getenv("authToken"))})
    handleRes(res)


def handleRes(res):

    if res:    
        res = res.json()

        global cooldown
        cooldown = res['cooldown']
        del res['cooldown']
        del res['players']
        global currentRoom
        currentRoom = res
        global roomsInfo
        roomsInfo.append(res)
        global visitedIds
        if res['room_id'] not in visitedIds:
            global count
            count += 1
            print(count)
            visitedIds.add(res['room_id'])

        upateFile()

def upateFile():
    global roomsInfo
    f = open("roominfo.json", "w+")
    f.write(json.dumps(roomsInfo))


init()
traverse()
