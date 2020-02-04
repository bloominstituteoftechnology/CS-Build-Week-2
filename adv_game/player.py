import requests
import json
import time
from time import sleep
import random
import sys
import pprint
pp = pprint.PrettyPrinter(indent=4)

#my_token = sys.argv[1]
my_token = "Token 9a118462c7930cbb7786d91ceeedf67f3d76c643"

class Player:


    def __init__(self):
        self.token = my_token
        r = requests.get(
            "https://lambda-treasure-hunt.herokuapp.com/api/adv/init/",
            headers = {"Authorization": self.token}
        )
        pp.pprint(dict(r.json()))


    def move(self, direction, wise_travel = None):
        if wise_travel == None:
            r = requests.post(
                "https://lambda-treasure-hunt.herokuapp.com/api/adv/move/",
                data = json.dumps({"direction": direction}),
                headers = {
                    "Authorization": self.token,
                    "Content-Type": "application/json"
                }
            )
        else:
            r = requests.post(
                "https://lambda-treasure-hunt.herokuapp.com/api/adv/move/",
                data = json.dumps({
                    "direction": direction,
                    "next_room_id": wise_travel
                    }),
                headers = {
                    "Authorization": self.token,
                    "Content-Type": "application/json"
                }
            )
        response = dict(r.json())
        print(f"Waiting {response['cooldown']} seconds for cooldown.")
        sleep(response['cooldown'])
        return response


    def pickup(self, item):
        r = requests.post(
            "https://lambda-treasure-hunt.herokuapp.com/api/adv/take/",
            data = json.dumps({"name": item}),
            headers = {
                "Authorization": self.token,
                "Content-Type": "application/json"
            }
        )
        return r.json()


    def drop(self, item):
        r = requests.post(
            "https://lambda-treasure-hunt.herokuapp.com/api/adv/drop/",
            data = json.dumps({"name": item}),
            headers = {
                "Authorization": self.token,
                "Content-Type": "application/json"
            }
        )
        return r.json()


    def sell(self, item, confirm = True):
        if confirm == True:
            r = requests.post(
                "https://lambda-treasure-hunt.herokuapp.com/api/adv/sell/",
                data = json.dumps({
                    "name": item,
                    "confirm": "yes"
                }),
                headers = {
                    "Authorization": self.token,
                    "Content-Type": "application/json"
                }
            )
        else:
            r = requests.post(
                "https://lambda-treasure-hunt.herokuapp.com/api/adv/sell/",
                data = json.dumps({"name": item}),
                headers = {
                    "Authorization": self.token,
                    "Content-Type": "application/json"
                }
            )
        return r.json()


    def status(self):
        r = requests.post(
            "https://lambda-treasure-hunt.herokuapp.com/api/adv/status/",
            headers = {
                "Authorization": self.token,
                "Content-Type": "application/json"
            }
        )
        return r.json()


    def examine(self, name):
        r = requests.post(
            "https://lambda-treasure-hunt.herokuapp.com/api/adv/examine/",
            data = json.dumps({"name": [name]}),
            headers = {
                "Authorization": self.token,
                "Content-Type": "application/json"
            }
        )
        return r.json()


    def wear(self, item):
        r = requests.post(
            "https://lambda-treasure-hunt.herokuapp.com/api/adv/wear/",
            data = json.dumps({"name": [item]}),
            headers = {
                "Authorization": self.token,
                "Content-Type": "application/json"
            }
        )
        return r.json()


    def undress(self, item):
        r = requests.post(
            "https://lambda-treasure-hunt.herokuapp.com/api/adv/undress/",
            data = json.dumps({"name": [item]}),
            headers = {
                "Authorization": self.token,
                "Content-Type": "application/json"
            }
        )
        return r.json()


    def change_name(self, new_name):
        r = requests.post(
            "https://lambda-treasure-hunt.herokuapp.com/api/adv/change_name/",
            data = json.dumps({"name": [new_name]}),
            headers = {
                "Authorization": self.token,
                "Content-Type": "application/json"
            }
        )
        return r.json()


    def pray(self):
        r = requests.post(
            "https://lambda-treasure-hunt.herokuapp.com/api/adv/pray/",
            headers = {
                "Authorization": self.token,
                "Content-Type": "application/json"
            }
        )
        return r.json()
