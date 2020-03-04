import requests
import hashlib
import json
from time import time
from uuid import uuid4
def proof_of_work(headers):
    """
    Simple Proof of Work Algorithm
    Stringify the block and look for a proof.
    Loop through possibilities, checking each one against `valid_proof`
    in an effort to find a number that is a valid proof
    :return: A valid proof for the provided block
    """
    response = requests.get('https://lambda-treasure-hunt.herokuapp.com/api/bc/last_proof/', headers=headers).json()
    last_proof = response['proof']
    difficulty = response['difficulty']
    print('---'*10)
    print(f"Mining coin for proof {last_proof} at difficulty {difficulty}...")
    # block_string = json.dumps(block, sort_keys=True)
    proof = 0

    while valid_proof(last_proof, proof, difficulty) is False:
        proof += 1
    
    # return proof
    data = '{"proof":' + str(proof) + '}'
    response = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/bc/mine/', headers=headers, data=data).json()
    return response

def valid_proof(last_proof, proof, difficulty):
    """
    Validates the Proof:  Does hash(block_string, proof) contain 6
    leading zeroes?  Return true if the proof is valid
    :param block_string: <string> The stringified block to use to
    check in combination with `proof`
    :param proof: <int?> The value that when combined with the
    stringified previous block results in a hash that has the
    correct number of leading zeroes.
    :return: True if the resulting hash is a valid proof, False otherwise
    """
    guess = str(last_proof) + str(proof)
    guess_encoded = guess.encode()
    guess_hash = hashlib.sha256(guess_encoded).hexdigest()
    
    if guess_hash[:difficulty] == '0' * difficulty:
        return True
    return False