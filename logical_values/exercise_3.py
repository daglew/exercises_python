"""
Ćwiczenie 3
Podane są poniższe dwie zmienne:
a = 5
b = 10
Wyznacz wartość logiczną poniższych wyrażeń:
(a < b) i b > 0
a == b lub b != 0
not (a >= b)
W każdym przypadku wydrukuj otrzymaną wartość logiczną do konsoli.
Oczekiwany wynik:
True
True
True
"""
a = 5
b = 10
print(bool((a < b) and b > 0))
print(bool(a == b or b != 0))
print(bool(not (a >= b)))


