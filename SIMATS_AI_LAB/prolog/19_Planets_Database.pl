planet(mercury, terrestrial, 0).
planet(earth, terrestrial, 1).
planet(jupiter, gas_giant, 79).
has_moons(P) :- planet(P, _, M), M > 0.
