"""
Ćwiczenie 19
Załóżmy, że w sklepie internetowym, który tworzysz, chcesz zaimplementować
funkcjonalność rabatów dla klientów, którzy kupią więcej niż jeden produkt.
Chcesz napisać program, który obliczy łączną kwotę zamówienia z uwzględnieniem
10% rabatu, jeśli klient kupił więcej niż jeden produkt.
Podana jest poniższa lista zawierająca produkty i ich ceny w testowym koszyku
klienta:
products = [('T-shirt', 50.00), ('Pants', 100.00), ('Shoes', 150.00)]
Policz łączną kwotę zamówienia na podstawie podanej listy produktów,
ich cen i zastosowanego rabatu. Wynik wydrukuj do konsoli tak jak
pokazano poniżej.
Oczekiwany wynik:
The total order amount after applying the discount is: 270.0
"""

products = [('T-shirt', 50.00), ('Pants', 100.00), ('Shoes', 150.00)]

order_amount = 0.0

if len(products) > 1:
    discount = 0.1
else:
    discount = 0.0

for product in products:
    order_amount += product[1]

together_with_discounts = order_amount - (order_amount * discount)
print('The total order amount after applying the discount is:', together_with_discounts,)
