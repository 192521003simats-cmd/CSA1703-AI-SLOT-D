edge(a, b).
edge(a, c).
edge(b, goal).
h(a, 4).
h(b, 1).
h(c, 3).
h(goal, 0).
best_fs(Goal, Goal, [Goal]).
best_fs(Curr, Goal, [Curr|Path]) :- edge(Curr, Next), best_fs(Next, Goal, Path).
