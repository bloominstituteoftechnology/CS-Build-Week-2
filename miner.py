import hashlib
import requests

import sys
from timeit import default_timer as timer
import random


def proof_of_work(last_proof, difficulty):
    start = timer()

    print("Searching for next proof")
    proof = 0
    total_tries = 0
    prev_proof = f'{last_proof}'.encode()
    last_hash = hashlib.sha256(prev_proof).hexdigest()
    while valid_proof(last_hash, proof, difficulty) is False:
        proof = random.randint(0, 10000)
        total_tries += 1

    print("Proof found: " + str(proof) + " in " + str(timer() - start))
    return proof


def valid_proof(last_hash, proof, difficulty):
    guess = f'{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()

    if difficulty is not None:
        leading_zeros = "0" * difficulty
    else:
        leading_zeros = "0" * 6

    return guess_hash[0:difficulty] == leading_zeros