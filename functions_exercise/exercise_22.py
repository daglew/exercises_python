"""
Ćwiczenie 23
Napisz generator o nazwie fibonacci(), który będzie zwracać kolejne liczby
z ciągu Fibonacciego. Generator powinien działać w nieskończoność,
tzn. zwracać kolejne liczby aż do przekroczenia zakresu typu int.
Przykłady użycia:

[IN]: fib = fibonacci()
[IN]: next(fib)
[OUT]: 0
[IN]: next(fib)
[OUT]: 1
[IN]: next(fib)
[OUT]: 1
[IN]: next(fib)
[OUT]: 2
[IN]: next(fib)
[OUT]: 3
[IN]: next(fib)
[OUT]: 5

Uwaga: Aby zaliczyć ćwiczenie wystarczy zdefiniować generator.
Nie trzeba go wywoływać. Zaimplementowane testy sprawdzają
poprawność działania generatora.
"""


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

