from decouple import config
import requests
import time
import sys
import re


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


def move_wise(direction, room_id):
    pass


def take_item(item):
    try:
        item = requests.post(
            f'{config('API_URL')}/api/adv/take/',
            headers={
                'Authorization': f'Token {config('API_KEY')}',
                'Content-Type': 'application/json'
            },
            data={
                'name': f'{item}'
            }
        )
        return item
    # if cooldown applies, add exception and while loop
    except requests.exceptions.RequestExceptions as exception:
        print(exception)
        sys.exit(1)


def drop_item(item):
    try:
        item = requests.post(
            f'{config('API_URL')}/api/adv/drop/',
            headers={
                'Authorization': f'Token {config('API_KEY')}',
                'Content-Type': 'application/json'
            },
            data={
                'name': f'{item}'
            }
        )
        return item
    # if cooldown applies, add exception and while loop
    except requests.exceptions.RequestExceptions as exception:
        print(exception)
        sys.exit(1)


def sell_treasure():
    while True:
        try:
            sale = requests.post(
                f'{config('API_URL')}/api/adv/sell/',
                headers={
                    'Authorization': f'Token {config('API_KEY')}',
                    'Content-Type': 'application/json'
                },
                data={
                    'name': 'treasure'
                }
            )
            message = sale['messages']
            cooldown = sale['cooldown']
            time.sleep(cooldown)
            # returns a message and requires confirmation to sell
            edited_message = re.sub('\([^)]*\)',
                                    '(choose YES or NO.)', message)
            print(edited_message)
            prompt = input().lower().strip()
            if promt == 'yes' or if prompt == 'y':
                # make call to confirm
                return confirm_treasure()
            elif prompt == 'no' or if prompt == 'n':
                # print confirmation message and return
                # need to decide how to handle return within algorithm
                print("Sale declined.")
                return
        # if cooldown applies, add exception and while loop
        except requests.exceptions.RequestException as exception:
            print(exception)
            sys.exit(1)


def confirm_treasure():
    try:
        confirm = requests.post(
            f'{config('API_URL')}/api/adv/sell/',
            headers={
                'Authorization': f'Token {config('API_KEY')}',
                'Content-Type': 'application/json'
            },
            data={
                'name': 'treasure',
                'confirm': 'yes'
            }
        )
        cooldown = confirm['cooldown']
        time.sleep(cooldown)
        return confirm
    except requests.exceptions.RequestException as exception:
        print(exception)
        sys.exit(1)


def check_status():
    try:
        status = requests.post(
            f'{config('API_URL')}/api/adv/status/',
            headers={
                'Authorization': f'Token {config('API_KEY')}',
                'Content-Type': 'application/json'
            }
        )
        cooldown = status['cooldown']
        time.sleep(cooldown)
        return status
    # if cooldown applies, add exception and while loop
    except requests.exceptions.RequestException as exception:
        print(exception)
        sys.exit(1)
