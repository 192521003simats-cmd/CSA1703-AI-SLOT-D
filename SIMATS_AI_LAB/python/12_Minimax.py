def minimax(depth, index, is_max, scores):
    if depth == 3:
        return scores[index]

    if is_max:
        left = minimax(depth + 1, index * 2, False, scores)
        right = minimax(depth + 1, index * 2 + 1, False, scores)
        return max(left, right)
    else:
        left = minimax(depth + 1, index * 2, True, scores)
        right = minimax(depth + 1, index * 2 + 1, True, scores)
        return min(left, right)

scores = [3, 5, 2, 9, 12, 5, 23, 23]
result = minimax(0, 0, True, scores)
print('Optimal Value:', result)
