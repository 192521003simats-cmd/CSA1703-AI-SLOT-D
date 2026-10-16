diet(diabetes, 'Low sugar, high fiber').
diet(hypertension, 'Low salt, DASH diet').
diet(anemia, 'Iron-rich spinach and dates').
suggest(Disease, Diet) :- diet(Disease, Diet).
