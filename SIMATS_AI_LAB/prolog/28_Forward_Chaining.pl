:- dynamic fact/1.
fact(has_fur).
fact(eats_meat).
rule(mammal) :- fact(has_fur), \+ fact(mammal), assertz(fact(mammal)).
rule(carnivore) :- fact(mammal), fact(eats_meat), \+ fact(carnivore), assertz(fact(carnivore)).
forward :- rule(_), !, forward.
forward :- write('Forward Chaining Complete').
