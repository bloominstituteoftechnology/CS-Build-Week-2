from utils import *

mappy = mapper()
mappy.accumulate=False   #set pick up items to false

mappy.create_starting_map()
time.sleep(5)

mappy.explore_random(50)