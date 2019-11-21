import hashlib
import requests

import sys
from timeit import default_timer as timer
import random


def proof_of_work(last_proof, difficulty):
    start = timer()

    print("Searching for next proof")
    proof = 80000000
    total_tries = 0
    prev_proof = f'{last_proof}'.encode()
    last_hash = hashlib.sha256(prev_proof).hexdigest()
    #while valid_proof(last_hash, proof, difficulty) is False:
    while valid_proof(last_proof, proof, difficulty) is False and total_tries < 6000000:
        #proof = random.randint(0, 10000)
        #proof+=1
        proof = random.randint(0, 100000000)
        total_tries += 1
        if total_tries % 1000000 == 0:
            print(total_tries/1000000,'million tries')

    
    if total_tries < 10000000:
        print("Proof found: " + str(proof) + " in " + str(timer() - start))
        return proof
    else:
        print('re-run')
        return 'rerun'


def valid_proof(last_hash, proof, difficulty):
    guess = f'{proof}'
    guess = (str(last_hash)+str(guess)).encode()  #there was no ref to last hash in valid proof
    guess_hash = hashlib.sha256(guess).hexdigest()
    #guess_hash = hash(guess)#.hexdigest()

    if difficulty is not None:
        leading_zeros = "0" * difficulty
    else:
        leading_zeros = "0" * 6

    #return guess_hash[0:difficulty] == leading_zeros
    return str(guess_hash)[0:difficulty] == leading_zeros