has_fur(tom).
eats_meat(tom).
mammal(X) :- has_fur(X).
carnivore(X) :- mammal(X), eats_meat(X).
