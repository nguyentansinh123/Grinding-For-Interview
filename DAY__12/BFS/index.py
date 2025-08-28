from collections import deque


def bfs(graph, node):
    visited = []
    queue = []

    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for i in graph[s]:
            if i not in visited:
                visited.append(i)
                queue.append(i)


graph = {
    "A": ["B", "G"],
    "B": ["C", "D", "E"],
    "C": [],
    "D": [],
    "E": ["F"],
    "F": [],
    "G": ["H"],
    "H": ["I"],
    "I": [],
}

bfs(graph, "A")
