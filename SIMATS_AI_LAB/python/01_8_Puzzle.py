from collections import deque

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
moves = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}

queue = deque([[start]])
visited = {start}

while queue:
    path = queue.popleft()
    state = path[-1]
    if state == goal:
        print("Solved in", len(path) - 1, "moves:")
        for s in path:
            print(s[:3])
            print(s[3:6])
            print(s[6:])
            print()
        break
    zero = state.index(0)
    for move in moves[zero]:
        new_state = list(state)
        new_state[zero], new_state[move] = new_state[move], new_state[zero]
        new_state = tuple(new_state)
        if new_state not in visited:
            visited.add(new_state)
            queue.append(path + [new_state])
