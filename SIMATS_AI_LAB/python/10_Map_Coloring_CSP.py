neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW']
}

colors = ['Red', 'Green', 'Blue']
solution = {}

def is_safe(node, color):
    for n in neighbors[node]:
        if n in solution and solution[n] == color:
            return False
    return True

def solve(nodes):
    if not nodes:
        return True
    node = nodes[0]
    for color in colors:
        if is_safe(node, color):
            solution[node] = color
            if solve(nodes[1:]):
                return True
            solution.pop(node)
    return False

solve(list(neighbors.keys()))
print('Color Assignment:', solution)
