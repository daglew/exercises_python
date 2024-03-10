"""
Ćwiczenie 4
Odczytaj podany plik products_2.txt zawierający dane dotyczące produktów w
sklepie internetowym:
smartfon,3000,10
laptop,5000,5
tablet,2000,12
Przedstaw te produkty w postaci listy słowników i przypisz do zmiennej products:
[{'name': 'smartfon', 'price': 3000.0, 'quantity': 10},
 {'name': 'laptop', 'price': 5000.0, 'quantity': 5},
 {'name': 'tablet', 'price': 2000.0, 'quantity': 12}]
Następnie wykorzystując pętlę for wydrukuj każdy produkt z listy products
do konsoli tak jak poniżej.
Oczekiwany wynik:
{'name': 'smartfon', 'price': 3000.0, 'quantity': 10}
{'name': 'laptop', 'price': 5000.0, 'quantity': 5}
{'name': 'tablet', 'price': 2000.0, 'quantity': 12}
"""


products = []


with open('products_2.txt', 'r') as file:
    for line in file:
        name, price, quantity = line.strip().split(',')
        products.append({
            'name': name,
            'price': float(price),
            'quantity': int(quantity)
        })

for product in products:
    print(product)

