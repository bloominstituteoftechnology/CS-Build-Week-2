from utils import *

mappy = mapper()
mappy.accumulate=True   #set pick up items to false
mappy.import_text_map=True
mappy.create_starting_map()
# mappy.go_to_room('10')
# print(mappy.player.currentRoom)
mappy.explore_random(150)