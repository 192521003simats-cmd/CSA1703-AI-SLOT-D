move(state(middle, middle, on_box, has_not), grasp, state(middle, middle, on_box, has)).
move(state(P, P, on_floor, H), climb, state(P, P, on_box, H)).
move(state(P1, P1, on_floor, H), push(P1, P2), state(P2, P2, on_floor, H)).
move(state(P1, B, on_floor, H), walk(P1, P2), state(P2, B, on_floor, H)).
canget(state(_, _, _, has), []).
canget(S1, [A|R]) :- move(S1, A, S2), canget(S2, R).
