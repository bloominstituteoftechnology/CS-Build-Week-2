import requests
import schedule
import time
import os
import json
import random
import hashlib
from dotenv import load_dotenv
load_dotenv()


lastProof = 0
difficulty = 0 
leadingZeros = "0"

def init():
    res = requests.get('https://lambda-treasure-hunt.herokuapp.com/api/bc/last_proof/',
                       headers={'Authorization': str(os.getenv("authToken"))})

    if res:
        global lastProof
        global difficulty
        global leadingZeros
        res = res.json()
        lastProof = res['proof']
        difficulty = res['difficulty']
        leadingZeros = "0" * difficulty
        print(lastProof)
        print(difficulty)
        print(leadingZeros)

        time.sleep(res['cooldown'])

def mine():
    global lastProof
    global difficulty
    global leadingZeros

    guess = 1
    encoded = f'{lastProof}{guess}'.encode()
    hashed = hashlib.sha256(encoded).hexdigest()


    while hashed[:difficulty] != leadingZeros:
        guess += 1
        encoded = f'{lastProof}{guess}'.encode()
        hashed = hashlib.sha256(encoded).hexdigest()

    print(hashed)

    res = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/bc/mine/',
                        headers={'Authorization': str(os.getenv('authToken'))},
                        json={'proof': guess}
                        )
    print(res)
    if res:
        res = res.json()
        print(res)

        time.sleep(res['cooldown'])


while True:
    init()
    mine()