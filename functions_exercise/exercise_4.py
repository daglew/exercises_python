"""
Ćwiczenie 4
Podane są poniższe zmienne:
number = 5
string = 'Hello, world!'
values = [5, 2, 8, 1, 9, 3]
Wykonaj poszczególne kroki:
sprawdź, czy zmienna number
jest typu int - jeśli tak, wydrukuj do konsoli 'The number is of type int.'
sprawdź, czy zmienna number jest typu float - jeśli tak, wydrukuj do konsoli
'The number is of type float.'
sprawdź, czy zmienna string jest typu str - jeśli tak, wydrukuj do konsoli
'The string is of type str.'
sprawdź, czy zmienna values jest typu tuple - jeśli tak, wydrukuj do konsoli
'The object is of type tuple.'
sprawdź, czy zmienna values jest typu list - jeśli tak, wydrukuj do konsoli
'The object is of type list.'
Oczekiwany wynik:
The number is of type int.
The string is of type str.
The object is of type list.
"""
number = 5
string = 'Hello, world!'
values = [5, 2, 8, 1, 9, 3]

if isinstance(number, int):
    print("The number is of type int.")

if isinstance(number, float):
    print("The number is of type float.")

if isinstance(string, str):
    print("The string is of type str.")

if isinstance(values, tuple):
    print("The object is of type tuple.")

if isinstance(values, list):
    print("The object is of type list.")









