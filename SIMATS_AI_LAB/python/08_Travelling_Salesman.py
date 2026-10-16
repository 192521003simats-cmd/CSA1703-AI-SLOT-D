from itertools import permutations

cost_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

cities = [1, 2, 3]
min_cost = 9999
best_route = []

for p in permutations(cities):
    route = [0] + list(p) + [0]
    cost = 0
    for i in range(len(route) - 1):
        cost += cost_matrix[route[i]][route[i + 1]]
    if cost < min_cost:
        min_cost = cost
        best_route = route

print('Optimal Route:', best_route)
print('Minimum Cost:', min_cost)
