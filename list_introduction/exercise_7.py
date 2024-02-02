"""
Ćwiczenie 16
Podana jest poniższa lista:
fruits = ['apple', 'banana', 'cherry', 'orange', 'kiwi']
Stwórz program, wykorzystuje różne metody list i wykona poszczególne operacje:
doda element 'melon' na koniec listy
wydrukuje listę
usunie element 'orange' z listy
wydrukuje listę
odwróci kolejność elementów w liście
wydrukuje listę
posortuje listę
wydrukuje listę
Wynik wydrukuj tak jak pokazano poniżej.
Oczekiwany wynik:
After appending: ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon']
After removing: ['apple', 'banana', 'cherry', 'kiwi', 'melon']
After reversing: ['melon', 'kiwi', 'cherry', 'banana', 'apple']
After sorting: ['apple', 'banana', 'cherry', 'kiwi', 'melon']
"""
fruits = ['apple', 'banana', 'cherry', 'orange', 'kiwi']
melon = ("melon")
fruits.append(melon)
print(f"After appending: {fruits}")
fruits.remove('orange')
print(f"After removing: {fruits}")
fruits.reverse()
print(f"After reversing: {fruits}")
fruits.sort()
print(f"After sorting: {fruits}")


