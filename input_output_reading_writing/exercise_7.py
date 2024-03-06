"""
Ćwiczenie 8
Podana jest poniższa lista produktów:
products = [
    {'name': 'T-shirt', 'price': 29.99},
    {'name': 'Shoes', 'price': 99.99},
    {'name': 'Pants', 'price': 49.99},
]

Zapisz listę produktów do pliku tekstowego o nazwie products.txt.
Każdy produkt zapisz jako wiersz, który składa się z nazwy produktu
i ceny, oddzielonych przecinkiem. Każdy wiersz zakończ znakiem
nowej linii \n.
Zawartość pliku products.txt po zapisaniu danych:
T-shirt,29.99
Shoes,99.99
Pants,49.99

"""
products_3 = [
    {'name': 'T-shirt', 'price': 29.99},
    {'name': 'Shoes', 'price': 99.99},
    {'name': 'Pants', 'price': 49.99},
]

with open('products_3', 'w') as file:
    for product in products_3:
        file.write(f"{product['name']},{product['price']}\n")



