# Explorer guide


## to initialize

```python
mappy = mapper()
mappy.create_starting_map()
```

## randomly explore

```python
mappy.explore_random(50)
```

## take action in current room given lastest info from server

```python
mappy.room_check()
```

## examples of workign commands
```python
mappy.action('take','tiny treasure')    #pick up some treasure  
mappy.action('status')                  # get status update
mappy.get_info('backtrack','e','254')   # back track specifying room and direction
```