import json
with open("room_map.json") as f:
    traversial_graph = json.load(f)
    f.close()

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

def reverse_dict(dictionary):
    return {str(v): str(k) for k, v in dictionary.items()}

def bfs(start_id, end_id):
    q = Queue()
    q.enqueue([start_id])
    visited = set()
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        if v not in visited:
            if v == end_id:
                return path
            visited.add(v)
            for neighbor in list(traversial_graph[v].values()):
                new_path = list(path)
                new_path.append(str(neighbor))
                q.enqueue(new_path)
    return None
