from collections import deque

queue = deque([(0, 0, [])])
visited = set()

while queue:
    x, y, path = queue.popleft()
    if (x, y) in visited:
        continue
    visited.add((x, y))
    path = path + [(x, y)]

    if x == 2 or y == 2:
        print("Steps:", path)
        break

    queue.append((4, y, path))
    queue.append((x, 3, path))
    queue.append((0, y, path))
    queue.append((x, 0, path))
    queue.append((max(0, x - (3 - y)), min(3, y + x), path))
    queue.append((min(4, x + y), max(0, y - (4 - x)), path))
