"""
Ćwiczenie 11
Podana jest poniższa lista:
fruits = ['apple', 'banana', 'cherry', 'orange', 'kiwi']
Stwórz program, który wykorzystując operator wycinania (slicing),
aby wyświetlić tylko wybrane elementy z listy tak jak podano poniżej.
Oczekiwany wynik:
List: ['apple', 'banana', 'cherry', 'orange', 'kiwi']
Slice 1: ['banana', 'cherry']
Slice 2: ['apple', 'banana', 'cherry']
Slice 3: ['orange', 'kiwi']
Slice 4: ['banana', 'orange']
"""
fruits = ['apple', 'banana', 'cherry', 'orange', 'kiwi']

print(f"List: {fruits}")
print(f"Slice 1:  {fruits[1:3]}")
print(f"Slice 2:  {fruits[0:3]}")
print(f"Slice 3:  {fruits[-2::]}")
print(f"Slice 4:  {fruits[1:5:2]}")












