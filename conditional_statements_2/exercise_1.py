"""
Ćwiczenie 11
Podana jest zmienna tekstowa:
fact = 'Python is easy and enjoyable'
Stwórz zbiór wszystkich znaków ze zmiennej fact. Następnie wykorzystaj
instrukcję warunkową, która sprawdzi czy długość otrzymanego zbioru
jest mniejsza niż 20 i wydrukuje informację:
There are less than 20 unique characters.
W przeciwnej sytuacji wydrukuje:
The number of unique characters is greater than or equal to 20.
Oczekiwany wynik:
There are less than 20 unique characters.
"""
fact = 'Python is easy and enjoyable'
character_set = set(fact)
len_character_set = len(character_set)

if len_character_set < 20:
    print(f"There are less than 20 unique characters.")
else:
    print(f"The number of unique characters is greater than or equal to 20.")





