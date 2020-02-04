import requests
import json
import time
from time import sleep
import random
import sys
import pprint
pp = pprint.PrettyPrinter(indent=4)

from special_rooms import *

#my_token = sys.argv[1]
my_token = "Token 9a118462c7930cbb7786d91ceeedf67f3d76c643"
base_url = "https://lambda-treasure-hunt.herokuapp.com/api/adv/"

r = requests.get("https://raw.githubusercontent.com/build-week-pt2/CS-Build-Week-2/matt/room_info.json")
room_information = dict(r.json())
r = requests.get("https://raw.githubusercontent.com/build-week-pt2/CS-Build-Week-2/matt/room_map.json")
traversial_graph = dict(r.json())


class Player:


    def __init__(self):
        self.token = my_token
        r = requests.get(
            base_url + "init/",
            headers = {"Authorization": self.token}
        )
        response = dict(r.json())
        self.current_room_id = response['room_id']
        pp.pprint(response)



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
        self.current_room_id = response['room_id']
        pp.pprint(response)
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
        response = dict(r.json())
        pp.pprint(response)
        return response


    def drop(self, item):
        r = requests.post(
            "https://lambda-treasure-hunt.herokuapp.com/api/adv/drop/",
            data = json.dumps({"name": item}),
            headers = {
                "Authorization": self.token,
                "Content-Type": "application/json"
            }
        )
        response = dict(r.json())
        pp.pprint(response)
        return response


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
        response = dict(r.json())
        pp.pprint(response)
        return response


    def status(self):
        r = requests.post(
            "https://lambda-treasure-hunt.herokuapp.com/api/adv/status/",
            headers = {
                "Authorization": self.token,
                "Content-Type": "application/json"
            }
        )
        response = dict(r.json())
        pp.pprint(response)
        return response


    def examine(self, name):
        r = requests.post(
            "https://lambda-treasure-hunt.herokuapp.com/api/adv/examine/",
            data = json.dumps({"name": [name]}),
            headers = {
                "Authorization": self.token,
                "Content-Type": "application/json"
            }
        )
        response = dict(r.json())
        pp.pprint(response)
        return response


    def wear(self, item):
        r = requests.post(
            "https://lambda-treasure-hunt.herokuapp.com/api/adv/wear/",
            data = json.dumps({"name": [item]}),
            headers = {
                "Authorization": self.token,
                "Content-Type": "application/json"
            }
        )
        response = dict(r.json())
        pp.pprint(response)
        return response


    def undress(self, item):
        r = requests.post(
            "https://lambda-treasure-hunt.herokuapp.com/api/adv/undress/",
            data = json.dumps({"name": [item]}),
            headers = {
                "Authorization": self.token,
                "Content-Type": "application/json"
            }
        )
        response = dict(r.json())
        pp.pprint(response)
        return response


    def change_name(self, new_name):
        r = requests.post(
            "https://lambda-treasure-hunt.herokuapp.com/api/adv/change_name/",
            data = json.dumps({"name": [new_name]}),
            headers = {
                "Authorization": self.token,
                "Content-Type": "application/json"
            }
        )
        response = dict(r.json())
        pp.pprint(response)
        return response


    def pray(self):
        r = requests.post(
            "https://lambda-treasure-hunt.herokuapp.com/api/adv/pray/",
            headers = {
                "Authorization": self.token,
                "Content-Type": "application/json"
            }
        )
        response = dict(r.json())
        pp.pprint(response)
        return response

    #def treasure_hunt(self, threshhold):
        # while gold under threshhold
        while self.status['gold'] < threshhold
            #while encumbrance < strength
            while self.status['encumbrance'] < self.status['strength']
                # pick a random direction
                # wise travel
                # if item treasure
                # pick it up
            #go to shop and sell treasure

    def destination_travel(self, destination):
        destination_map = map_to_destination(self.current_room_id, destination)

        while room_information[str(self.current_room_id)]["title"] != destination:
            direction = destination_map[str(self.current_room_id)]
            wise_travel_id = traversial_graph[str(self.current_room_id)][direction]
            self.move(direction, wise_travel_id)
