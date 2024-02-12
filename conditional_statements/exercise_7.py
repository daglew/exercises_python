"""
Ćwiczenie 10
Załóżmy, że prowadzisz sklep internetowy, w którym sprzedajesz różne produkty,
w tym książki. Napisz program, który na podstawie kategorii książki i jej
ilości w magazynie obliczy rabat na zakup.
Podane są poniższe trzy zmienne:
category = 'crime'
quantity = 5
book_price = 100
W tym programie użyj instrukcji warunkowej if, elif i else, aby obliczyć
rabat na zakup książek w zależności od ich kategorii i ilości.

Jeśli kategoria książek to 'crime', program sprawdza, czy ilość książek
wynosi co najmniej 5. Jeśli tak, rabat wynosi 20% ceny, jeśli ilość wynosi
co najmniej 3, rabat wynosi 10% ceny, a w przeciwnym razie nie ma rabatu.

Jeśli kategoria książek to 'fantasy', program sprawdza, czy ilość książek
wynosi co najmniej 10. Jeśli tak, rabat wynosi 25% ceny, jeśli ilość wynosi
co najmniej 5, rabat wynosi 15% ceny, a w przeciwnym razie nie ma rabatu.

Dla wszystkich innych kategorii książek, program sprawdza, czy ilość książek
wynosi co najmniej 20. Jeśli tak, rabat wynosi 10% ceny, jeśli ilość wynosi
co najmniej 10, rabat wynosi 5% ceny, a w przeciwnym razie nie ma rabatu.
Następnie oblicz cenę książki po zastosowaniu rabatu. Na końcu wyświetl
informację o ostatecznej cenie książki po rabacie.
Oczekiwany wynik:
The total price after the discount is 80.0 PLN.
"""
category = 'crime'
quantity = 5
book_price = 100

if category == 'crime':
    if quantity >= 5:
        discount = 0.20
    elif quantity >= 3:
        discount = 0.10
    else:
        discount = 0

elif category == 'fantasy':
    if quantity >= 10:
        discount = 0.25
    elif quantity >= 5:
        discount = 0.15
    else:
        discount = 0

else:
    if quantity >= 20:
        discount = 0.10
    elif quantity >= 10:
        discount = 0.05
    else:
        discount = 0

price = book_price * (1 - discount)
print(f"The total price after the discount is {price} PLN.")

