"""
Ćwiczenie 3
Podana jest poniższa lista:
list1 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
Stwórz program, który wykorzysta konstrukcję set() do usunięcia duplikatów i
utworzenia zbioru z unikalnymi elementami tej listy. Następnie przekształć
otrzymany zbiór na listę i wynik wydrukuj do konsoli tak jak pokazano poniżej
Oczekiwany wynik:
List with duplicates: [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
List without duplicates: [1, 2, 3, 4, 5]
"""
list1 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
list1_without_duplicates = set(list1)
print(f"List with duplicates: {list1_without_duplicates}")

duplicates_lists1 = list1
print(f"List without duplicates: {duplicates_lists1}")


