list_member(X,[X|_]).
list_member(X,[_|TAIL]) :- list_member(X,TAIL).

conc([],L,L).
conc([X|M],N,[X|Q]):-conc(M,N,Q). 

list_rev([],[]).
list_rev([Head|Tail],Reversed) :-
   list_rev(Tail, RevTail),conc(RevTail, [Head],Reversed).

list_length([],0).
list_length([_|TAIL],N) :- list_length(TAIL,N1), N is N1 + 1.