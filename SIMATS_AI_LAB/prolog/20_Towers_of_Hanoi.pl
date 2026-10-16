move(1, A, B, _) :- format('Move disk from ~w to ~w~n', [A, B]).
move(N, A, B, C) :- N > 1, M is N - 1, move(M, A, C, B), move(1, A, B, _), move(M, C, B, A).
