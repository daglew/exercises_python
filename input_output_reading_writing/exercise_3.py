"""
Ćwiczenie 3
Odczytaj podany plik products.txt zawierający dane dotyczące produktów
w sklepie internetowym. Pomiń pierwszą linię pliku zawierającą nagłówek
pliku i w postaci listy wydrukuj każdy kolejny wiersz pliku do konsoli
tak jak pokazano poniżej.
Oczekiwany wynik:
['Printed T-shirt', '29.99', 'Classic white t-shirt with a printed design on the front']
['Sweatpants', '49.99', 'Black sweatpants made from a soft material']
['Evening Dress', '99.99', 'Elegant evening dress with a deep neckline']
['Sport Shoes', '79.99', 'Lightweight sport shoes perfect for running.']
"""

with open('products.txt', 'r') as file:
    lines = file.readlines()

lines = lines[1:]

products = []
for line in lines:
    change = line.strip().split(';')
    products.append(change)

for product in products:
    print(product)


