from collections import deque


def dfs(graph, node):
    stack = deque()
    visited = []

    visited.append(node)
    stack.append(node)

    while stack:
        s = stack.pop()
        print(s, end=" ")

        for i in reversed(graph[s]):
            if i not in visited:
                visited.append(i)
                stack.append(i)


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

dfs(graph, "A")
