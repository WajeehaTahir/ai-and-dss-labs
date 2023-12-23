class PriorityQueue:
    def __init__(self):
        self.queue = {}

    def push(self, value, priority):
        if priority in self.queue.keys():
            self.queue[priority].append(value)
        else:
            self.queue[priority] = [value]

    def pop(self):
        min_priority = min(self.queue.keys())
        node = self.queue[min_priority].pop(0)

        if not self.queue[min_priority]:
            del self.queue[min_priority]

        return node

    def display(self):
        print(self.queue)

    def length(self):
        return len(self.queue)

    def ifExists(self, value):
        return value in self.queue.keys()


def AStar(graph, heuristic, startNode, goal):
    queue = PriorityQueue()
    queue.push(startNode, 0)

    cameFrom = {startNode: ''}
    costSoFar = {startNode: 0}

    while queue.length():
        currentNode = queue.pop()
        neighbors = graph[currentNode]

        for key in neighbors.keys():
            newCost = costSoFar[currentNode] + graph[currentNode][key]

            if key not in costSoFar or newCost < costSoFar[key]:
                costSoFar[key] = newCost
                priority = newCost + heuristic[key]
                queue.push(key, priority)
                cameFrom[key] = currentNode

    return reconstructPath(cameFrom, startNode, goal), costSoFar[goal]


def reconstructPath(cameFrom, start, goal):
    current = goal
    path = []

    while current is not start:
        path.append(current)
        current = cameFrom[current]

    path.append(start)
    path.reverse()

    return path


graph = {
    'A': {'Z': 75, 'T': 118, 'S': 140},
    'B': {'G': 90, 'P': 101, 'U': 85, 'F': 211},
    'C': {'D': 120, 'R': 146, 'P': 138},
    'D': {'C': 120, 'M': 75},
    'E': {'H': 86},
    'F': {'B': 211, 'S': 99},
    'G': {'B': 90},
    'H': {'E': 86, 'U': 98},
    'I': {'N': 87, 'V': 92},
    'L': {'T': 111, 'M': 70},
    'M': {'L': 70,'D': 75},
    'N': {'I': 87},
    'O': {'Z': 71, 'S': 151},
    'P': {'R': 97, "C": 138, 'B': 101},
    'R': {'P': 97, "S": 80, 'C': 146},
    'S': {'O': 151, 'A': 140, 'F': 99, 'R': 80},
    'T': {'A': 118, 'L': 111},
    'U': {'B': 85, 'V': 142, 'H': 98},
    'V': {'I': 92, 'U': 142},
    'Z': {'O': 71, 'A': 75},
}

heuristic = {
    'A': 366,
    'B': 0,
    'C': 160,
    'D': 242,
    'E': 161,
    'F': 178,
    'G': 77,
    'H': 151,
    'I': 226,
    'L': 244,
    'M': 241,
    'N': 234,
    'O': 380,
    'P': 98,
    'R': 193,
    'S': 253,
    'T': 329,
    'U': 80,
    'V': 199,
    'Z': 374
}

path, cost = AStar(graph, heuristic, 'A', 'E')
print('Path: ', path)
print('Cost: ', cost)
