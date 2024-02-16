"""
Ćwiczenie 18
Załóżmy, że tworzysz sklep internetowy, w którym klienci mogą dodawać produkty
do koszyka i składać zamówienia. Chcesz napisać program, która policzy łączną
kwotę zamówienia na podstawie listy produktów i ich cen.
Podana jest poniższa lista zawierająca produkty i ich ceny w testowym koszyku
klienta:
products = [('T-shirt', 50.00), ('Pants', 100.00), ('Shoes', 150.00)]
Policz łączną kwotę zamówienia na podstawie podanej listy produktów i ich cen.
Wynik wydrukuj do konsoli tak jak pokazano poniżej.
Oczekiwany wynik:
The total order amount is: 300.0
"""
products = [('T-shirt', 50.00), ('Pants', 100.00), ('Shoes', 150.00)]

result = 0.0

for product in products:
    result += product[1]

print('The total order amount is:', result)

