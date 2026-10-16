def alphabeta(depth, index, is_max, scores, alpha, beta):
    if depth == 3:
        return scores[index]

    if is_max:
        best = -999
        for i in range(2):
            val = alphabeta(depth + 1, index * 2 + i, False, scores, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = 999
        for i in range(2):
            val = alphabeta(depth + 1, index * 2 + i, True, scores, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

scores = [3, 5, 6, 9, 1, 2, 0, -1]
result = alphabeta(0, 0, True, scores, -999, 999)
print('Optimal Value with Pruning:', result)
