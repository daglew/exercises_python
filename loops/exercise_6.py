"""
Ćwiczenie 20
Załóżmy, że w sklepie internetowym, który tworzysz, chcesz umożliwić
klientom filtrowanie produktów według kategorii. Chcesz napisać program,
który wyświetli tylko te produkty, które należą do wybranej kategorii.
Oto lista twoich produktów w testowym sklepie internetowym:
products = [
    ('T-shirt', 'Clothing', 50.00),
    ('Pants', 'Clothing', 100.00),
    ('Shoes', 'Footwear', 150.00)
]
Napisz program, który wyświetli tylko te produkty, które należą do
kategorii 'Clothing'. Wynik wydrukuj do konsoli tak jak pokazano poniżej.
Oczekiwany wynik:
T-shirt 50.0
Pants 100.0
"""
products = [
    ('T-shirt', 'Clothing', 50.00),
    ('Pants', 'Clothing', 100.00),
    ('Shoes', 'Footwear', 150.00)
]
category = "Clothing"
for clothes in products:
    if clothes[1] == category:
        print(clothes[0], clothes[2])

