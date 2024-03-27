"""
Ćwiczenie 1
Używając list comprehension wydrukuj do konsoli listę liczb od 0 do 30 (bez 30)
podzielnych przez 4.

Uwaga: Zadanie można zrobić przy pomocy jednej linii kodu.

Oczekiwany wynik:
[0, 4, 8, 12, 16, 20, 24, 28]
"""


divisible = [liczba for liczba in range(30) if liczba % 4 == 0]
print(divisible)

"""
Ćwiczenie 2
Podana jest poniższa lista:
words = ['cat', 'dog', 'rabbit', 'hamster', 'parrot', 'raccoon']
Wykorzystaj list comprehension, aby utworzyć nową listę o nazwie r_words, 
która zawiera tylko słowa z oryginalnej listy słów words, 
które zaczynają się na literę 'r'. W odpowiedzi wynik wydrukuj do konsoli.
Oczekiwany wynik:
['rabbit', 'raccoon']
"""

words = ['cat', 'dog', 'rabbit', 'hamster', 'parrot', 'raccoon']

r_words = [word for word in words if word[0] == 'r']
print(r_words)
