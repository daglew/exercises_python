"""
Ćwiczenie 13
Podana jest lista miast:
cities = ['Warsaw', 'London', 'Berlin', 'New York']
Używając funkcji map() oraz wyrażenia lambda uzyskaj listę
zawierającą trzy pierwsze litery każdego miasta. Otrzymaną
listę wydrukuj do konsoli.
Oczekiwany wynik:
['War', 'Lon', 'Ber', 'New']
"""


cities = ['Warsaw', 'London', 'Berlin', 'New York']
list_cities = list(map(lambda city: city[:3], cities))
print(list_cities)
