import hashlib

import sys
from uuid import uuid4

import requests
import os
from dotenv import load_dotenv
load_dotenv()

from timeit import default_timer as timer
import random

AUTH_TOKEN = os.getenv("AUTH_TOKEN")

print(AUTH_TOKEN)


# def proof_of_work(last_proof):
#     """
#     Multi-Ouroboros of Work Algorithm
#     - Find a number p' such that the last six digits of hash(p) are equal
#     to the first six digits of hash(p')
#     - IE:  last_hash: ...AE9123456, new hash 123456888...
#     - p is the previous proof, and p' is the new proof
#     - Use the same method to generate SHA-256 hashes as the examples in class
#     - Note:  We are adding the hash of the last proof to a number/nonce for the new proof
#     """
#     start = timer()

#     print("Searching for next proof")
#     proof = 0
#     #  TODO: Your code here

#     last_encoded = f'{last_proof}'.encode()
#     last_hash = hashlib.sha256(last_encoded).hexdigest()
#     while valid_proof(last_hash, proof) is False:
#         proof = random.randint(1,99999999999)

#     print("Proof found for: " + last_hash[-6:] + " " + str(proof) + " in " + str(timer() - start))
#     return proof

# def valid_proof(last_hash, proof):
#     """
#     Validates the Proof:  Multi-ouroborus:  Do the last six characters of
#     the hash of the last proof match the first six characters of the proof?

#     IE:  last_hash: ...AE9123456, new hash 123456888...
#     """

#     # TODO: Your code here!
#     guess_encoded = f'{proof}'.encode()
#     guess_hash = hashlib.sha256(guess_encoded).hexdigest()
#     return guess_hash[:6] == last_hash[-6:]


# if __name__ == '__main__':
#     # What node are we interacting with?
#     if len(sys.argv) > 1:
#         node = sys.argv[1]
#     else:
#         node = "https://lambda-treasure-hunt.herokuapp.com/api"

#     coins_mined = 0

#     # Load or create ID
#     f = open("my_id.txt", "r")
#     id = f.read()
#     print("ID is", id)
#     f.close()
#     AUTH_TOKEN = os.getenv("AUTH_TOKEN")
#     headers = {
#     'Authorization': 'Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607',
#     }

#     if id == 'NONAME\n':
#         print("ERROR: You must change your name in `my_id.txt`!")
#         exit()
#     # Run forever until interrupted
#     while True:
#         # Get the last proof from the server
#         r = requests.get(url=node + "/bc/last_proof", headers=headers)
#         data = r.json()
#         new_proof = proof_of_work(data.get('proof'))

#         post_data = {"proof": new_proof,
#                      "id": id}

#         r = requests.post(url=node + "/bc/mine", json=post_data, headers=headers)