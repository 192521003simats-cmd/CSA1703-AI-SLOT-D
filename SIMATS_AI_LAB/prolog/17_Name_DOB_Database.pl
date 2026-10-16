person(alice, '15-May-2001').
person(bob, '22-Aug-2000').
person(charlie, '10-Jan-2002').
get_dob(Name, DOB) :- person(Name, DOB).
