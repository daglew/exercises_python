"""
Ćwiczenie 3
Podana jest poniższa lista:
values = [-5, 2, 8, -1, 9, -3]
Wykorzystując funkcje wbudowane w język Python posortuj
tę listę według wartości bezwzględnej. Wynik wydrukuj
do konsoli tak jak pokazano poniżej.
Oczekiwany wynik:
[-1, 2, -3, -5, 8, 9]
"""
values = [-5, 2, 8, -1, 9, -3]

ready_list = sorted(values, key=abs)
print(ready_list)

