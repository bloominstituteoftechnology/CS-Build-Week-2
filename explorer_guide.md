# Explorer guide

either run from command line with 

```
python explore.py
```

or load up python from command line and import * from utils

basic_utils.py is just all the old graphs, stack, queue and search funtions from our assignments

## to initialize from python

```python
mappy = mapper()
mappy.create_starting_map()
```

## set your custom variables
```python
mappy.accumulate = True       # auto pick up items
mappy.save_map_to_text = True #overwrite current map.txt with fresh map.txt
mappy.import_text_map = True #load current map.txt as starting map #MUST BE DONE BEFORE create_starting_map
                             #if you don't want fresh map
```
## show your latest map
```python
mappy.my_map.vertices
```

## randomly explore

```python
mappy.explore_random(50)   #exploring 50 unkown rooms (not including backtracking)
```

## take action in current room given lastest info from server

```python
mappy.room_check()   #given how you have set certain variables like pray or accumulate will automate actions 
                    # given certain cues from the server json responses
```

## examples of working commands
```python
mappy.get_info('init')                  # initialize and get current room details
mappy.get_info('move','n')              # move north
mappy.get_info('backtrack','e','254')   # back track specifying room and direction

mappy.action('take','tiny treasure')    # pick up some treasure  
mappy.action('drop','tiny treasure')    # drop some treasure in your inventory
mappy.action('sell','tiny treasure')    # sell some treasure in your inventory
mappy.action('sell_confirm','tiny treasure')    # confirm sell some treasure in your inventory 
mappy.action('examine','tiny treasure')    # examine tiny treasure in your inventory
mappy.action('status')                  # get status update
mappy.action('pray')                    # pray in shrine room

```