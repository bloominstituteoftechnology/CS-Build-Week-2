from utils import *

mappy = mapper()
mappy.accumulate = True  # set pick up items to false
mappy.import_text_map = True
mappy.create_starting_map()
# mappy.go_to_room(1)
mappy.get_treasure()
# mappy.get_info()

# mappy.explore_random(118)
