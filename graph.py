
# from adv import move

# import random
# from ast import literal_eval

# # Load world
# world = World()

# # map_file = "maps/main_maze.txt"

# # Loads the map into a dictionary
# # room_graph=literal_eval(open(map_file, "r").read())
# # world.load_graph(room_graph)

# # Print an ASCII map
# # world.print_rooms()
# # world.print_grid()

# # player = Player(world.starting_room)

# # Fill this out with directions to walk
# # traversal_path = ['n', 'n']
# traversal_path = [] #append path here


# #back to room with exit
# previous_room = [None]
# opposites_direction = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}

# room_track = {}
# visited = {}
# #check each direction                                (14, 14)        {'n': 2, 's': 50, 'w': 6}
# print(room_graph[5][0])  #see room graph [room_id][0 is conneted room/ 1 is direction]
# def check_directions(room_id):
#     directions = []
#     if 'n' in room_graph[room_id][1].keys(): #get only key direction
#         directions.append('n')
#     if 'e' in room_graph[room_id][1].keys():  
#         directions.append('e')
#     if 's' in room_graph[room_id][1].keys():
#         directions.append('s')
#     if 'w' in room_graph[room_id][1].keys():
#         directions.append('w')
#     return directions

# while len(visited) < len(room_graph):
#     room_id = player.current_room.id
#     #check room_id in  room_track 
#     if room_id not in room_track:
#         #add to visited 
#         visited[room_id] = room_id
#         #add all directions using check_directions()
#         room_track[room_id] = check_directions(room_id)
    
#     #check if there are any more directions to travel. 
#     if len(room_track[room_id]) < 1:
#         previous_direction = previous_room.pop()
#         traversal_path.append(previous_direction)
#         #send player object in that direction
#         player.travel(previous_direction)
        
#     else:
#         #new direction to travel in, will be pulled from the master list of directions
#         next_direction = room_track[room_id].pop(0)
#         traversal_path.append(next_direction)
#         #keep track in opposite direction
#         previous_room.append(opposites_direction[next_direction])
#         player.travel(next_direction)


# # TRAVERSAL TEST
# visited_rooms = set()
# player.current_room = world.starting_room
# visited_rooms.add(player.current_room)

# for move in traversal_path:
#     player.travel(move)
#     visited_rooms.add(player.current_room)

# if len(visited_rooms) == len(room_graph):
#     print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
# else:
#     print("TESTS FAILED: INCOMPLETE TRAVERSAL")
#     print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



# #######
# # UNCOMMENT TO WALK AROUND
# #######
# # player.current_room.print_room_description(player)
# # while True:
# #     cmds = input("-> ").lower().split(" ")
# #     if cmds[0] in ["n", "s", "e", "w"]:
# #         player.travel(cmds[0], True)
# #     elif cmds[0] == "q":
# #         break
# #     else:
# #         print("I did not understand that command.")