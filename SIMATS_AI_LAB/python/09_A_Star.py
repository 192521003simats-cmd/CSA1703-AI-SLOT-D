import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 3), ('G', 5)],
    'C': [('G', 2)],
    'D': [('G', 1)],
    'G': []
}

heuristic = {'A': 5, 'B': 3, 'C': 2, 'D': 1, 'G': 0}
queue = [(heuristic['A'], 0, 'A', ['A'])]

while queue:
    f, cost, current, path = heapq.heappop(queue)
    if current == 'G':
        print('Path:', path)
        print('Cost:', cost)
        break
    for neighbor, weight in graph[current]:
        new_cost = cost + weight
        total_f = new_cost + heuristic[neighbor]
        heapq.heappush(queue, (total_f, new_cost, neighbor, path + [neighbor]))
