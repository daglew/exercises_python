"""
Ćwiczenie 12
Mamy podaną zmienną tekstową:
number_string = '123,785,45,5'
Używając odpowiedniej metody wyodrębnij dane liczbowe ze zmiennej number_string,
tak aby rezultatem była lista wartości tekstowych zawierających same cyfry.
Wynik wydrukuj do konsoli używając funkcji print().
Oczekiwany wynik:
['123', '785', '45', '5']

"""

number_string = '123,785,45,5'

print(number_string.split(","))

