class Lifo:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack):
            return self.stack.pop()

    def getLength(self):
        return len(self.stack)

    def ifExists(self, value):
        return value in self.stack


def dfs(graph, start):
    stack = Lifo()
    stack.push(start)
    visited_nodes = []

    while stack.getLength():
        node = stack.pop()

        if node not in visited_nodes:
            visited_nodes.append(node)

            for neighbor in graph[node]:
                if not stack.ifExists(neighbor):
                    stack.push(neighbor)

    print(visited_nodes)


graph1 = {
    6: [4],
    4: [3, 5],
    3: [2, 4],
    5: [1, 2, 4],
    2: [1, 3, 5],
    1: [2, 5]
}
dfs(graph1, 6)

graph2 = {
    'C': ['D'],
    'D': ['A', 'B', 'C'],
    'A': ['B', 'D', 'E'],
    'B': ['A', 'D', 'E'],
    'E': ['A', 'B']
}
dfs(graph2, 'E')
