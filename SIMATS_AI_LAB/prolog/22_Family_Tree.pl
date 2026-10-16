parent(john, bob).
parent(bob, mike).
male(john).
male(bob).
father(F, C) :- male(F), parent(F, C).
grandfather(G, C) :- father(G, P), parent(P, C).
