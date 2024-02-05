"""
Ćwiczenie 19
Podany jest poniższy słownik:
fruits = {'apple': 2, 'banana': 3, 'cherry': 5, 'orange': 1}
Stwórz program, który wykona poniższe operacje:
wydrukuje słownik fruits
doda do słownika nowy klucz 'kiwi' z wartością 4
wydrukuje słownik fruits
usunie element ze słownika z kluczem 'orange'
wydrukuje słownik fruits
wydrukuje klucze słownika fruits
wydrukuje wartości słownika fruits
W odpowiedzi wynik wydrukuj do konsoli tak jak pokazano poniżej.
Oczekiwany wynik:
Dictionary: {'apple': 2, 'banana': 3, 'cherry': 5, 'orange': 1}
After adding: {'apple': 2, 'banana': 3, 'cherry': 5, 'orange': 1, 'kiwi': 4}
After deleting: {'apple': 2, 'banana': 3, 'cherry': 5, 'kiwi': 4}
Keys: dict_keys(['apple', 'banana', 'cherry', 'kiwi'])
Values: dict_values([2, 3, 5, 4])
"""
fruits = {'apple': 2, 'banana': 3, 'cherry': 5, 'orange': 1}

print(f"Dictionary: {fruits}")

fruits['kiwi'] = 4
print(f"After adding: {fruits}")
del fruits['orange']
print(f"After deleting: {fruits}")
print(f"Keys: {fruits.keys()}")
print(f"Values: {fruits.values()}")

