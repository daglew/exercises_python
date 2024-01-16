"""
Ćwiczenie 5
Stwórz trzy zmienne initial_amount, interest_rate oraz duration i przypisz do nich odpowiednio wartości 1000 PLN, 5% oraz 2 lata.
Oblicz wartość końcową inwestycji kwoty początkowej po 2 latach z uwzględnieniem kapitalizacji rocznej. Podana stopa procentowa jest stopą w skali roku i w obliczeniach należy ją zamienić na ułamek.
Uwaga: Aby zadanie zostało zaliczone poprawnie należy wydrukować tylko właściwy wynik do konsoli funkcją print().
Wskazówka: Aby obliczyć wartość inwestycji po 2 latach z uwzględnieniem kapitalizacji rocznej, należy skorzystać ze wzoru na wartość przyszłą:
fv = pv * (1 + r / 100) ** n, gdzie r / 100 to stopa procentowa w ułamkach.
fv - wartość przyszła
pv - wartość początkowa
r - roczna stopa procentowa
n - liczba okresów
"""

initial_amount = 1000
interest_rate = 5
duration = 2

fv = initial_amount * (1 + interest_rate / 100) ** duration

print(fv)

