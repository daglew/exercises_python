#
# file = open('simple.txt', 'r')
# for line in file:
#     print(line, end='')
#
# file.close()


"""
Ćwiczenie 1
Odczytaj podany plik data.txt zawierający dane dotyczące notowań 
trzech spółek. Wydrukuj każdą linię do konsoli.
Oczekiwany wynik:
KGHM, 100
PKN Orlen, 90
PKO BP, 42
Tauron, 30
Orange, 25
PGE, 20
"""
with open('data.txt', 'r') as file:
    for line in file:
        print(line, end='')



