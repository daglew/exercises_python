"""
Ćwiczenie 10
Zaimplementuj funkcję o nazwie rectangle_area(),
która obliczy pole prostokąta.
Przykłady użycia:
[IN]: rectangle_area(2, 4)
[OUT]: 8
[IN]: rectangle_area(10, 6)
[OUT]: 60
W tym ćwiczeniu nie dokonujemy żadnej walidacji argumentów.
Zakładamy, że użytkownik przekazuje dodatnie wartości liczbowe.
Uwaga: Aby zaliczyć ćwiczenie wystarczy zdefiniować funkcję.
Nie trzeba jej wywoływać. Zaimplementowane testy sprawdzają
poprawność działania funkcji.
"""


def rectangle_area(side, base):
    area = side * base
    return area


"""
Ćwiczenie 11
Zaimplementuj funkcję o nazwie is_even(), która sprawdzi, 
czy liczba jest parzysta.
Przykłady użycia:
[IN]: is_even(10)
[OUT]: True
[IN]: is_even(13)
[OUT]: False
W tym ćwiczeniu nie dokonujemy żadnej walidacji argumentów. 
Zakładamy, że użytkownik przekazuje wartości liczbowe.
Uwaga: Aby zaliczyć ćwiczenie wystarczy zdefiniować funkcję.
Nie trzeba jej wywoływać. Zaimplementowane testy sprawdzają 
poprawność działania funkcji.
"""


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

