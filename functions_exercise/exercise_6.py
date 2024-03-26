"""
Ćwiczenie 6
Przy pomocy odpowiedniej funkcji wbudowanej oraz pętli for
wydrukuj poniższe wartości do konsoli.
Oczekiwany wynik:
1 2 3 4 5 6 7 8 9
0 2 4 6 8
100 90 80 70 60 50 40 30 20 10
Zwróć uwagę na białe znaki. Po każdej liczbie wstawiony został
znak spacji.
"""
for number in range(1, 10):
    print(number, end=" ")
print()

for number in range(0, 10, 2):
    print(number, end=" ")
print()

for number in range(100, 0, -10):
    print(number, end=" ")

