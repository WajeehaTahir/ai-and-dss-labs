class Queue:
    def __init__(self):
        self.list = []

    def push(self, value):
        self.list.append(value)

    def pop(self):
        if len(self.list):
            return self.list.pop(0)

    def display(self):
        print(self.list)

    def length(self):
        return len(self.list)

    def ifExists(self, value):
        return value in self.list

def bfs(graph):
    visited_nodes = Queue()
    queue = Queue()
    queue.push(list(graph.keys())[0])

    while queue.length():
        node = queue.pop()

        if not visited_nodes.ifExists(node):
            visited_nodes.push(node)

            for neighbor in graph[node]:
                if not queue.ifExists(neighbor):
                    queue.push(neighbor)

    visited_nodes.display()


graph1 = {
    'C': ['D'],
    'D': ['A', 'B'],
    'A': ['B', 'D', 'E'],
    'B': ['A', 'D', 'E'],
    'E': ['A', 'B']
}
bfs(graph1)

graph2 = {
    6: [4],
    4: [3, 5],
    3: [2, 4],
    5: [1, 2, 4],
    2: [1, 3, 5],
    1: [2, 5]
}
bfs(graph2)
