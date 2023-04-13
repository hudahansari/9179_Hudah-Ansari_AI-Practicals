min_of_two(X,Y,X) :- X =< Y, !.
min_of_two(X,Y,Y) :- X > Y.
list_min_elem([X],X).
list_min_elem([X,Y|Rest],Min) :-
   list_min_elem([Y|Rest],MinRest),
   min_of_two(X,MinRest,Min).