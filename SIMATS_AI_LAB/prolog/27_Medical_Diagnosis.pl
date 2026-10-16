symptom(fever).
symptom(cough).
diagnose(flu) :- symptom(fever), symptom(cough).
diagnose(cold) :- symptom(sneezing), symptom(runny_nose).
