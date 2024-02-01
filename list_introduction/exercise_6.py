"""
Ćwiczenie 15
Podane są następujące elementy:
'Apple', 'Microsoft', 'Samsung', 'Netflix', 'Uber'.
Z podanych elementów utwórz listę.
Używając odpowiedniej metody dodaj jeszcze dwa elementy na koniec listy:
'Amazon', 'Google'
Wydrukuj otrzymaną listę do konsoli.
Oczekiwany wynik:
['Apple', 'Microsoft', 'Samsung', 'Netflix', 'Uber', 'Amazon', 'Google']
"""

lista_1 = ['Apple', 'Microsoft', 'Samsung', 'Netflix', 'Uber']
print(lista_1)
lista_2 = ('Amazon', 'Google')
lista_1.extend(lista_2)
print(lista_1)


