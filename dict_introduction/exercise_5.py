"""
Ćwiczenie 22
Podany jest poniższy słownik:
people = {'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40}
Napisz program, który wykorzystując odpowiednią metodę usuwa
wpis ze słownika o kluczu 'Bob' i zwraca wartość usuniętego wpisu.
W odpowiedzi wydrukuj otrzymaną wartość oraz pozostały
słownik people tak jak pokazano poniżej.
Oczekiwany wynik:
30
{'Alice': 25, 'Charlie': 35, 'David': 40}
"""
people = {'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40}
people.pop('Bob')
print(people)


