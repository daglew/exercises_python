"""
Ćwiczenie 10
Stwórz poniższą listę zagnieżdżoną:
fruits = [['apple', 'banana'], ['cherry', 'orange'], ['kiwi', 'melon']]
Następnie wydrukuj podaną listę oraz pierwszy element drugiej zagnieżdżonej
listy tak jak pokazano poniżej.
Oczekiwany wynik:
Nested list: [['apple', 'banana'], ['cherry', 'orange'], ['kiwi', 'melon']]
First item of second nested list: cherry
"""
fruits = [['apple', 'banana'], ['cherry', 'orange'], ['kiwi', 'melon']]
print(f"Nested list: {fruits}")
print(f"First item of second nested list: {fruits[1][0]}")

