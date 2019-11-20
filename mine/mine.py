import requests
import time
import os
import json
import random
from dotenv import load_dotenv
load_dotenv()


lastProof = 0
difficulty = 0

def init():
    res = requests.get('https://lambda-treasure-hunt.herokuapp.com/api/bc/last_proof/',
                       headers={'Authorization': str(os.getenv("authToken"))})

    if res:
        res = res.json()
        lastProof = res['proof']
        difficulty = res['difficulty']

        time.sleep(res['cooldown'])

def mine():
    rndNumber = random.randrange(2, 1001)
    proposedProof = hash(lastProof, rndNumber)

    while proof(proposedProof) is not True:
        rndNumber += random.randrange(2, 1001)
        proposedProof = hash(lastProof, rndNumber)

    res = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/bc/mine/',
                        headers={'Authorization': str(os.getenv('authToken'))},
                        json={'proof': proposedProof}
                        )
    print(res)
    if res:
        res = res.json()

        time.sleep(res['cooldown'])



def proof(proposedProof):
    str(proposedProof)
    check = proposedProof[:difficulty]

    if int(check) is 0:
        return True
    else:
        return False


init()
while True:
    mine()
    init()