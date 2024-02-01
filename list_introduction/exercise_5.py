"""
Ćwiczenie 14
Utwórz dwie poniższe listy:
list_1 = [4, 5, 3, 3]
list_2 = [9, 7]
Używając odpowiedniej metody
rozszerz listę pierwszą o elementy drugiej list i wynik wydrukuj do konsoli.
Oczekiwany wynik:
[4, 5, 3, 3, 9, 7]
"""
list_1 = [4, 5, 3, 3]
list_2 = [9, 7]
list_1.extend(list_2)
print(list_1)

