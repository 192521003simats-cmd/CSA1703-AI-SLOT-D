bird(sparrow).
bird(eagle).
bird(penguin).
flightless(penguin).
can_fly(X) :- bird(X), \+ flightless(X).
