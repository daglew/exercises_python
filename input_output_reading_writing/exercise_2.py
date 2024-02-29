with open('simple.txt', 'r') as file:
    line = file.readline()
    print(line)

with open('simple.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

with open('simple.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line, end='')

with open("simple.txt", 'r') as file:
    line = file.readline()
    while line:
        print(line, end='')
        line = file.readline()

with open('simple.txt', 'r') as file:
    lines = file.read()
    print(lines)

"""
Ćwiczenie 2
Wczytaj plik data.txt przy użyciu metody readlines().
Rezultat (listę) wydrukuj do konsoli tak jak pokazano poniżej.
Oczekiwany wynik:
['KGHM, 100\n', 'PKN Orlen, 90\n', 'PKO BP, 42\n', 'Tauron, 30\n', 'Orange, 25\n']
"""
with open('data.txt', 'r') as file:
    lines = file.readlines()
    print(lines)


