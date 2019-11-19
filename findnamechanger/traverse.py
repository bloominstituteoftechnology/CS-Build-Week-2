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
goBackCache = []

def start():
    global currentRoom
    currentRoom = None
    global cooldown
    cooldown = 0
    global visitedIds
    visitedIds = set()
    global count 
    count = 0
    global roomsInfo
    roomsInfo = []
    global goBackCache
    goBackCache = []

    try:
        with open('roominfo.json', 'r') as jsonFile:
            prevData = json.load(jsonFile)
            for el in prevData:
                visitedIds.add(el['room_id'])
                roomsInfo.append(el)

        with open('goBackCache.json', 'r') as jsonFile:
            prevData = json.load(jsonFile)
            for el in prevData:
                goBackCache.append(el)
                    
        count = 0

        print("moves:", count, " len(visited):", len(visitedIds), " len(roomsInfo):", len(roomsInfo))



    except:
        return

def traverse():

    global goBackCache


    while len(visitedIds) < 500:

        print(currentRoom['room_id'])
        if currentRoom['room_id'] == 467:
            changeName()
            break

        if currentRoom['room_id'] == 461:
            pray()
            break
            

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

def changeName():
    print("NAMECHANGER")
    res = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/change_name/',
                        headers={'Authorization': str(os.getenv('authToken'))},
                        json={'name': 'BestTeam: Sorin the Mentor, Thorben the Hero, Wasiu the Great, Damola the Warrior, Shola the Wizard, Inaki the other Hero', 'confirm': 'aye'}
                        )

def pray():
    print("SHRINE")
    res = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/pray/',
                        headers={'Authorization': str(os.getenv('authToken'))},
                        json={"confirm": "yes"}
                        )

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
    time.sleep(cooldown)

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
        
        global visitedIds
        global count
        count += 1
        
        if res['room_id'] not in visitedIds:
            global roomsInfo 
            roomsInfo.append(res)
            visitedIds.add(res['room_id'])
            print("moves:", count, " len(visited):", len(visitedIds), " len(roomsInfo):", len(roomsInfo))   
            
    upateFile()

def upateFile():
    global roomsInfo
    f = open("./roominfo.json", "w+")
    f.write(json.dumps(roomsInfo))
    f.close()

    global goBackCache
    f = open("./goBackCache.json", "w+")
    f.write(json.dumps(goBackCache))
    f.close()



start()
init()
traverse()

