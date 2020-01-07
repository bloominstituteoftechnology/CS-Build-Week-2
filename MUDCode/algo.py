traversalPath = []
own_graph = {
    0: {'n': '?', 's': '?', 'e': '?', 'w': '?'}
}
backpath = []
​
# ATTEMPT 2
def get_opp(direction):
    if direction == 'n':
        return 's'
    if direction == 'e':
        return 'w'
    if direction == 's':
        return 'n'
    if direction == 'w':
        return 'e'
​
def log_path(direction, prev_room, prev_exits):
    # if room already in own graph, assign exit just used, leave everything else alone
    if player.currentRoom.id in own_graph:
        for x in player.currentRoom.getExits():
            if get_opp(direction) == x: 
                own_graph[player.currentRoom.id][x] = prev_room
​
    # otherwise, create room, assign exit just used, fill other exits with '?'
    else:
        own_graph[player.currentRoom.id] = {}
        for x in player.currentRoom.getExits():
            if get_opp(direction) == x: 
                own_graph[player.currentRoom.id][x] = prev_room
            else:
                own_graph[player.currentRoom.id][x] = '?'
​
    # assign exit just used to previous room
    for x in prev_exits:
        if x == direction:
            own_graph[prev_room][x] = player.currentRoom.id
​
​
def get_unexplored(unexplored):
    # if any exits in current room == '?', add to unexplored list
    for x in player.currentRoom.getExits():
        if own_graph[player.currentRoom.id][x] == '?':
            unexplored.append(x)
​
def travel(direction):
    player.travel(direction)
    traversalPath.append(direction)
​
def dft():
​
    while len(own_graph) < len(roomGraph):  
        prev_room = player.currentRoom.id
        prev_exits = player.currentRoom.getExits()
        # loop through current room exits, if exit == '?', then add to unexplored list
        unexplored = []
        get_unexplored(unexplored)
​
        # choose random direction from unexplored
        if len(unexplored) > 0:
            direction = random.choice(unexplored)
            travel(direction)
            backpath.append(get_opp(direction))  
        else: 
            # if dead-end reached
            while len(unexplored) == 0:
                direction = backpath.pop()
                travel(direction)
                get_unexplored(unexplored)
​
        #### after traveling, log
        log_path(direction, prev_room, prev_exits)
​
start = time.time()
dft()
end = time.time()
print("own_graph = ", own_graph)
print("traversalPath = ", traversalPath)
print("len(own_graph) = ", len(own_graph))
print("len(roomGraph) = ", len(roomGraph))
print("length of traversal path (number of steps): ", len(traversalPath))
print("Time: ", end - start)