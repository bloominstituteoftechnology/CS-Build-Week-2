# Explorer guide


## to initialize

```mappy = mapper()
mappy.create_starting_map()```

## randomly explore

```mappy.explore_random(50)```

## take action in current room given lastest info from server

```mappy.room_check()```

## examples of workign commands
```mappy.action('take','tiny treasure')```  
```mappy.action('status')```
```mappy.get_info('backtrack','e','254')```