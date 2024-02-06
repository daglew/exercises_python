"""
Ćwiczenie 23
Podany jest poniższy słownik:
people = {'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40}
Napisz program, który wykorzystując odpowiednią metodę umożliwia dodanie
nowego wpisu do słownika, jeśli klucz nie istnieje, lub zwraca
wartości związaną z kluczem, jeśli klucz już istnieje w słowniku
i dodaj w ten sposób parę o kluczu 'Emma' i wartości 20 do słownika people.
W odpowiedzi wydrukuj otrzymaną wartość po dodaniu wpisu oraz
słownik people do konsoli tak jak pokazano poniżej.
Oczekiwany wynik:
20
{'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40, 'Emma': 20}
"""
people = {'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40}
new_people = people.setdefault('Emma', 20)
print(new_people)
print(people)




