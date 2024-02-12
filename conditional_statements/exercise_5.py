"""
Ćwiczenie 8
Załóżmy, że prowadzisz sklep internetowy, w którym sprzedajesz różne produkty,
w tym elektronikę. Napisz program, który na podstawie kategorii produktu
i jego ceny obliczy wysokość podatku VAT.
Podane są poniższe dwie zmienne:
category = 'electronics'
price = 2000
W tym programie użyj instrukcji warunkowej if, elif i else, aby obliczyć
wysokość podatku VAT dla danego produktu w zależności od jego kategorii i ceny.

Jeśli kategoria produktu to 'electronics', program sprawdza, czy cena
przekracza 1000 zł.
Jeśli tak, VAT wynosi 23% ceny, a jeśli nie,VAT wynosi 8% ceny.
Jeśli kategoria produktu to 'clothing',VAT wynosi zawsze 23% ceny.
W pozostałych przypadkach VAT wynosi 21% ceny.
Na końcu program wyświetl informację o wysokości VAT dla danego produktu
tak jak pokazano poniżej.
Oczekiwany wynik:
The VAT for a product is 460.0 PLN.
"""
category = 'electronics'
price = 2000
if category == 'electronics':
    if price > 1000:
        vat = 0.23 * price
    else:
        vat = 0.08 * price
elif category == 'clothing':
    vat = price * 0.21
print("The VAT for a product is 460.0 PLN.")




