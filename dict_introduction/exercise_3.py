"""
Ćwiczenie 20
Podany jest poniższy słownik:
fruits = {'apple': 2, 'banana': 3}
Stwórz program, który wykona poniższe operacje:
wydrukuje słownik fruits
zaktualizuje wartość dla istniejącego klucza 'apple' na 4
wydrukuje słownik fruits
doda nową parę klucz-wartość 'kiwi': 1
wydrukuje słownik fruits
połączy dwa słowniki fruits oraz {'orange': 3, 'peach': 2}
wydrukuje słownik po połączeniu
W odpowiedzi wynik wydrukuj do konsoli tak jak pokazano poniżej.
Oczekiwany wynik:
Dictionary before update: {'apple': 2, 'banana': 3}
Dictionary after update: {'apple': 4, 'banana': 3}
Dictionary after adding: {'apple': 4, 'banana': 3, 'kiwi': 1}
Dictionary after merging: {'apple': 4, 'banana': 3, 'kiwi': 1, 'orange': 3, 'peach': 2}
"""
fruits = {'apple': 2, 'banana': 3}
print(f"Dictionary before update: {fruits}")

fruits.update({'apple': 4})
print(f"Dictionary after update: {fruits}")

fruits['kiwi'] = 1
print(f"Dictionary after adding: {fruits}")

fruits.update({'orange': 3, 'peach': 2})
print(f"Dictionary after merging: {fruits}")

