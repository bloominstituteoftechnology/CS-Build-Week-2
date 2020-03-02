from decouple import config
import requests
import time
import sys


def init_player():
    try:
        player = requests.get(
            f'{config('API_URL')}/api/adv/init/',
            headers={
                'Authorization': f'Token {config('API_KEY')}',
                'Content-Type': 'application/json'
            }
        )
        cooldown = player['cooldown']
        time.sleep(cooldown)
        return player
    except requests.exceptions.RequestExceptions as exception:
        # cooldown -> will have to check response object to test
        if exception.response.status_code == 400:
            time.sleep(cooldown)
        else:
            print(exception)
            sys.exit(1)


def move_player(direction):
    while True:
        try:
            room = requests.post(
                f'{config('API_URL')}/api/adv/move/',
                headers={
                    'Authorization': f'Token {config('API_KEY')}',
                    'Content-Type': 'application/json'
                },
                data={
                    'direction': f'{direction}'
                }
            )
            cooldown = room['cooldown']
            time.sleep(cooldown)
            return room
        except requests.exceptions.RequestExceptions as exception:
            # cooldown -> will have to check response object to test
            if exception.response.status_code == 400:
                time.sleep(cooldown)
            else:
                print(exception)
                sys.exit(1)
