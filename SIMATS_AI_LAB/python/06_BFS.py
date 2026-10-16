from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

visited = []
queue = deque(['A'])

while queue:
    node = queue.popleft()
    if node not in visited:
        visited.append(node)
        for neighbor in graph[node]:
            queue.append(neighbor)

print('BFS Traversal:', visited)
