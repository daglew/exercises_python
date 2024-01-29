"""
Ćwiczenie 6
Podane są dwie poniższe krotki (obiekty typu tuple):
tuple1 = (1, 2, 3)
tuple2 = ('apple', 'banana', 'cherry')
Stwórz program, który wykorzystuje operator + do połączenia tych
krotek w trzecią krotkę. W odpowiedzi wynik wydrukuj do konsoli
tak jak pokazano poniżej.
Oczekiwany wynik:
Tuple 1: (1, 2, 3)
Tuple 2: ('apple', 'banana', 'cherry')
Combined tuple: (1, 2, 3, 'apple', 'banana', 'cherry')
"""
tuple1 = (1, 2, 3)
tuple2 = ('apple', 'banana', 'cherry')
print(f"Tuple 1: {tuple1}")
print(f"Tuple 2: {tuple2}")
print(f"Combined tuple: {tuple1+tuple2}")


