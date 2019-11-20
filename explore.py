from utils import *

mappy = mapper()
mappy.accumulate=True   #set pick up items to false
mappy.import_text_map=True
mappy.create_starting_map()

# mappy.explore_random(150)
mappy.get_treasure()
