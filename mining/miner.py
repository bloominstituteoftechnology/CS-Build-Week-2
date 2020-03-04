import hashlib
import requests
import time
import sys
import random

from decouple import config
from uuid import uuid4
from timeit import default_timer as timer


def proof_of_work(last_proof, diff):
    """
    Multi-Ouroboros of Work Algorithm
    - Find a number p' such that the last six digits of hash(p) are equal
    to the first six digits of hash(p')
    - IE:  last_hash: ...AE9123456, new hash 123456888...
    - p is the previous proof, and p' is the new proof
    - Use the same method to generate SHA-256 hashes as the examples in class
    """

    start = timer()

    print("Searching for next proof")
    proof = 0
    last = f'{last_proof}'.encode()
    last_hash = hashlib.sha256(last).hexdigest()

    while valid_proof(last_hash, last_proof, proof, diff) is False:
        proof += 1

    print("Proof found: " + str(proof) + " in " + str(timer() - start))
    return proof


def valid_proof(last_hash, last_proof, proof, diff):
    """
    Validates the Proof:  Multi-ouroborus:  Do the last six characters of
    the hash of the last proof match the first six characters of the hash
    of the new proof?
    IE:  last_hash: ...AE9123456, new hash 123456E88...
    """

    guess = f'{last_proof}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()

    if guess_hash[:diff] == '0'*diff:
        return True
    else:
        return False


if __name__ == '__main__':
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "https://lambda-treasure-hunt.herokuapp.com/api/bc"
        headers = {"Authorization": config('API_KEY')}

    coins_mined = 0

    while True:
        r = requests.get(url=node + "/last_proof", headers=headers)
        last_data = r.json()
        new_proof = proof_of_work(last_data['proof'], last_data['difficulty'])
        print(f'New Proof {new_proof}')

        post_data = {"proof": new_proof}
        print(post_data)

        r = requests.post(url=node + "/mine", json=post_data, headers=headers)
        data = r.json()
        print(data)
        time.sleep(data["cooldown"])
