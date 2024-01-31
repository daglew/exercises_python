"""
Ćwiczenie 12
Podana jest poniższa lista zagnieżdżona:
fruits = [
    ['apple', 'banana', 'cherry'],
    ['orange', 'kiwi', 'melon'],
    ['grape', 'pear', 'plum'],
]
Stwórz program, który wykorzystuje operator wycinania,
aby wyświetlić tylko wybrane elementy z listy wewnętrznej.
Wynik wydrukuj do konsoli tak jak pokazano poniżej.
Oczekiwany wynik:
Last item of first nested list: cherry
First two items of second nested list: ['orange', 'kiwi']
Last two items of third nested list: ['pear', 'plum']
"""
fruits = [
    ['apple', 'banana', 'cherry'],
    ['orange', 'kiwi', 'melon'],
    ['grape', 'pear', 'plum'],
]

print(f"Last item of first nested list: {fruits[0][2]}")
print(f"First two items of second nested list: {fruits[1][0:2]}")
print(f"Last two items of third nested list: {fruits[2][-2::]}")

