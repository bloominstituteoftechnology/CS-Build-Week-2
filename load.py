import pickle

def load():
    print('Checking if map saved...')

    try:
        with open('map.pickle', 'rb') as f:
            graph = pickle.load(f)
            print(f"Map contains {len(graph)} nodes.")
        print('Map loaded\n')
    except FileNotFoundError:
        graph = {}

    try:
        with open('500rooms.pickle', 'rb') as f:
            room_list = pickle.load(f)
        print('Map loaded\n')
    except FileNotFoundError:
        room_list = {}

    return graph, room_list


graph, room_list = load()

print(len(graph))
print(len(room_list))