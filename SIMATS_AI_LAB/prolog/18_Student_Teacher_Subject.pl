teaches(dr_smith, ai).
studies(john, ai).
studies(mary, ai).
teacher_of(T, S) :- teaches(T, Sub), studies(S, Sub).
