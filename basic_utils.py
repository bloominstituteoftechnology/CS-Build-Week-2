class Queue():
    def __init__(self):
        self.queue = []

    def __repr__(self):
        return f'{self.queue}'

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        if vertex not in self.vertices.keys():
            self.vertices[vertex] = set()
        else:
            pass

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 and v2 in self.vertices.keys():
         # self.vertices[v2].add(v1)
            self.vertices[v1].add(v2)

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        ret_list = []
        if starting_vertex is None:
            return None
        my_q = Queue()
        visited = [starting_vertex]
        my_q.enqueue(starting_vertex)
        while len(my_q.queue) > 0:
            point = my_q.queue[0]
            joins = self.vertices[point]
            for j in joins:
                if j not in visited:
                    my_q.enqueue(j)
                    visited.append(j)
            # print(my_q.dequeue())
            ret = my_q.dequeue()
            ret_list.append(ret)
        return ret_list

    def dft(self, starting_vertex, chooser=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        ret_list = []
        if starting_vertex is None:
            return None
        my_s = Stack()
        visited = [starting_vertex]
        my_s.push(starting_vertex)
        while len(my_s.stack) > 0:
            point = my_s.stack[-1]
            joins = self.vertices[point]
            r = my_s.pop()  # new code
            ret_list.append(r)  # new code
            # print(r)  ##changed to r from pop
            if chooser is None:
                pass
            elif chooser == 'random':
                joins = random.sample(joins, len(joins))
            elif chooser == 'shortest':
                joins = find_longest_clique(point, self, visited)
            for j in joins:
                if j not in visited:
                    my_s.push(j)
                    visited.append(j)
        return ret_list

    def dft_recursive(self, starting_vertex, visited=[]):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        print(starting_vertex)
        visited.append(starting_vertex)
        joins = self.vertices[starting_vertex]
        if joins is None:
            return None
        for j in joins:
            if j in visited:
                pass
            else:
                self.dft_recursive(j, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        print('Starting BFS')
        q = Queue()
        visited = set()
        q.enqueue([starting_vertex])
        print(f'Starting vertex: {starting_vertex}')
        print(f'End Room: {destination_vertex}')

        while destination_vertex not in q.queue[0]:
            # while q.queue[0][-1] != destination_vertex:
            # print(q)
            current_point = q.queue[0][-1]
            # print(f'current point: {current_point}')
            joins = self.vertices[current_point].values()
            # print(joins)
            for j in joins:
                # print(f'J: {j}')
                if j != '?' and j not in visited:
                    visited.add(j)
                    _ = [x for x in q.queue[0]]
                    _.append(j)
                    q.enqueue(_)
            q.dequeue()

        return q.queue[0]

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex])

        while destination_vertex not in s.stack[-1]:
            current_point = s.stack[-1][-1]

            joins = self.vertices[current_point]
            if joins is None:
                s.pop()
            else:
                temp_list = []
                for j in joins:
                    _ = [x for x in s.stack[-1]]
                    _.append(j)
                    temp_list.append(_)
                for tl in temp_list:
                    s.push(tl)
            # s.pop()

        return s.stack[-1]
