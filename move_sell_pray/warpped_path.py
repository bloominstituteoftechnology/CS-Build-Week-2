import time
import datetime
def cooldown_func(response):
    cooldown = response
    # cooldown_rounded_up = math.ceil(cooldown)
    then = datetime.datetime.now()
    print(then)
    while (then + cooldown + .1) > datetime.datetime.now():
            print(f'Remaining cooldown new move: {(then + cooldown) - datetime.datetime.now()}', end="\r")
            time.sleep(1)
    # for i in range(0, cooldown_rounded_up):
    #     print(f'Remaining cooldown new move: {cooldown_rounded_up - i})', end="\r")
    #     time.sleep(1)
    
cooldown_func(5)