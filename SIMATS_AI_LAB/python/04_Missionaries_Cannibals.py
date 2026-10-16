from collections import deque

def is_valid(m, c):
    if m < 0 or m > 3 or c < 0 or c > 3:
        return False
    if m > 0 and c > m:
        return False
    if (3 - m) > 0 and (3 - c) > (3 - m):
        return False
    return True

queue = deque([(3, 3, 1, [(3, 3, 1)])])
visited = set()

while queue:
    m, c, b, path = queue.popleft()
    if (m, c, b) == (0, 0, 0):
        print("Path:", path)
        break
    visited.add((m, c, b))

    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    for dm, dc in moves:
        if b == 1:
            nm, nc, nb = m - dm, c - dc, 0
        else:
            nm, nc, nb = m + dm, c + dc, 1
        if is_valid(nm, nc) and (nm, nc, nb) not in visited:
            queue.append((nm, nc, nb, path + [(nm, nc, nb)]))
