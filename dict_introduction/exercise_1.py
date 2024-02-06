"""
Ćwiczenie 17
Utwórz słownik, który będzie mapował pierwsze pięć
liczb naturalnych na ich kwadraty (rozpocznij od 1).
W odpowiedzi utworzony słownik wydrukuj do konsoli.
Oczekiwany wynik:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""
natural_numbers = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(natural_numbers)

"""
Ćwiczenie 18
Podany jest poniższy słownik:
countries_capitals = {
    'Polska': 'Warszawa',
    'Niemcy': 'Berlin',
    'Czechy': 'Praga',
}
Dodaj kolejny element do słownika: 'Włochy': 'Rzym'
Następnie utwórz listę i przypisz do niej posortowane 
od A do Z nazwy stolic. Wynik sortowania wydrukuj do konsoli.
Oczekiwany wynik:
['Berlin', 'Praga', 'Rzym', 'Warszawa']
"""

countries_capitals = {
    'Polska': 'Warszawa',
    'Niemcy': 'Berlin',
    'Czechy': 'Praga',
}

countries_capitals['Włochy'] = 'Rzym'
enlarged_countries_capitals = sorted(list(countries_capitals.values()))
print(enlarged_countries_capitals)



