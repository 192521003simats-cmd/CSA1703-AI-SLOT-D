match_prefix([], _).
match_prefix([H|T1], [H|T2]) :- match_prefix(T1, T2).
match_sub(Pat, List) :- append(_, Rest, List), append(Pat, _, Rest).
