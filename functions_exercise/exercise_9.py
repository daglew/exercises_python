"""
Ćwiczenie 9
Napisz funkcję print_odd_numbers(), która zwróci listę liczb
nieparzystych większych od zera i mniejszych od 20.
Oczekiwany wynik:
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
Uwaga: Aby zaliczyć ćwiczenie wystarczy zdefiniować funkcję.
Nie trzeba jej wywoływać. Zaimplementowane testy sprawdzają
poprawność działania funkcji.
"""


def print_odd_numbers():
    list_after_change = []
    for i in range(20):
        if i % 2 != 0:
            list_after_change.append(i)
    return list_after_change

