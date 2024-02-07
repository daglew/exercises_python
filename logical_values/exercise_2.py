"""
Ćwiczenie 2
Podane są poniższe trzy zmienne:
x = 3
y = 5
z = 0
Wyznacz wartość logiczną poniższych wyrażeń:
(x > y) i (z < y)
(x > y) lub (z < y)
W każdym przypadku wydrukuj otrzymaną wartość logiczną do konsoli.
Oczekiwany wynik:
False
True
"""
x = 3
y = 5
z = 0
print(bool((x > y) and (z < y)))
print(bool((x > y) or (z < y)))

