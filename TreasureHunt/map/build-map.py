import random
from structures import Queue, Stack
from treasure.models import MapRoom
from functions import move_player, init_player

# view_stack = []
# view_queue = []


class Graph:
    def __init__(self):
        self.rooms_count = 0
        self.rooms = {}

    def add_room(self, room):
        # add vertex to the graph with dictionary as value
        if room.room_id not in self.rooms:
            directions = {}
            for direct in room.exits:
                directions[direct] = '?'
            self.rooms[room.room_id] = directions
            self.rooms_count += 1

            map_room = MapRoom(room)
            map_room.neighbors = directions
            map_room.save()
        else:
            print(f"room: {room} already exists, did not add.")
            return False

    def connect_rooms(self, next_dir, curr_room, prev_room):
        for direction in self.rooms[prev_room]:
            if direction == next_dir:
                self.rooms[prev_room][direction] = curr_room
        for direction in self.rooms[curr_room]:
            if next_dir == 'n':
                self.rooms[curr_room]['s'] = prev_room
            if next_dir == 's':
                self.rooms[curr_room]['n'] = prev_room
            if next_dir == 'e':
                self.rooms[curr_room]['w'] = prev_room
            if next_dir == 'w':
                self.rooms[curr_room]['e'] = prev_room

        prev_map_room = MapRoom.objects.get(room_id=prev_room)
        prev_map_room.neighbors = self.rooms[prev_room]
        prev_map_room.save()
        curr_map_room = MapRoom.objects.get(room_id=curr_room)
        curr_map_room.neighbors = self.rooms[curr_room]
        curr_map_room.save()

    def dft_rand(self, init_room):
        stack = Stack()
        stack.push(init_room)
        # view_stack.append(player.current_room.id)
        # # print('initial view stack', view_stack)
        random_dir = None
        prev_room = None
        while len(self.rooms) <= 500:
            curr_room = stack.pop()
            # view_stack.pop()
            # # print('view stack after pop', view_stack)
            if curr_room.room_id not in self.rooms:
                self.add_room(curr_room)
                print(curr_room.room_id, 'added to self.rooms')
            if random_dir is None:
                dir_list = []
                for direction in self.rooms[curr_room.room_id]:
                    if self.rooms[curr_room.room_id][direction] == '?':
                        dir_list.append(direction)
                    random.shuffle(dir_list)
                    random_dir = dir_list.pop()
            if prev_room is not None:
                self.connect_rooms(
                    random_dir, curr_room.room_id, prev_room.room_id)
                print(curr_room.room_id, "connected to:", prev_room.room_id)
            if random_dir not in self.rooms[curr_room.room_id]:
                print('random_dir', random_dir,
                      'self.rooms[curr_room.id]:', self.rooms[curr_room.room_id])
                unex_list = []

                for key, value in self.rooms[curr_room.room_id].items():
                    if value == '?':
                        unex_list.append(key)
                print('unex_list', unex_list)
                if len(unex_list) == 0:
                    path = self.bfs(curr_room)
                    print('path:', path)
                    if path is None:
                        print('path is none')
                        return
                    new_room = path[-1][0]
                    print('path[-1][0]:', path[-1][0])
                    for move in path[1:]:
                        # changing room as we travel
                        curr_room = move_player(move)
                        # print('player.current_room bfs', player.current_room.room_id)
                    unex_list = []
                    for key, value in self.rooms[new_room].items():
                        if value == '?':
                            unex_list.append(key)
                    random.shuffle(unex_list)
                random_dir = unex_list.pop()

            prev_room = curr_room
            curr_room = move_player(random_dir)
            # print('player.current_room dft:', player.current_room.id)
            stack.push(curr_room)
            # view_stack.append(player.current_room.id)
            # # print('from outer cond of dft viewstack', view_stack)

    def bfs(self, first_room):
        queue = Queue()
        queue.enqueue([(first_room.room_id, "")])
        # view_queue.append([(first_room.id, "")])
        # print('initial view_queue', view_queue)
        visited_set = set()
        while queue.size() > 0 and len(self.rooms) < 500:
            new_path = queue.dequeue()
            # view_queue.pop(0)
            # print('view_queue after dequeue', view_queue)
            room = new_path[-1][0]
            # print('room', room, 'new_path', new_path, 'queue', queue)
            for direction, value in self.rooms[room].items():
                if value == '?':
                    # print('all of room props:', self.rooms[room])
                    return new_path
            if room not in visited_set:
                visited_set.add(room)
                for direction, neighbor in self.rooms[room].items():
                    if neighbor not in visited_set:
                        next_path = list(new_path)
                        next_path.append((neighbor, direction))
                        queue.enqueue(next_path)
                        # view_queue.append(next_path)
                        # print('viewqueue after append', view_queue)
                        # print('visited_set', visited_set)


user = init_player()
tg = Graph()
tg.dft_rand(user)
