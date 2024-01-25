"""
Ćwiczenie 2
Podane są poniższe dwa zbiory:
set1 = set([1, 2, 3, 4, 5])
set2 = set([4, 5, 6, 7, 8])
Stwórz program, który wykona operacje na zbiorach takie jak set.union(),
set.intersection(), set.difference() i set.symmetric_difference().
W odpowiedzi wynik wydrukuj do konsoli tak jak pokazano poniżej.
Oczekiwany wynik:
Union set: {1, 2, 3, 4, 5, 6, 7, 8}
Intersection set: {4, 5}
Difference set: {1, 2, 3}
Symmetric difference set: {1, 2, 3, 6, 7, 8}
"""
set1 = set([1, 2, 3, 4, 5])
set2 = set([4, 5, 6, 7, 8])
union_set = set1.union(set2)
print(f"Union set:", union_set)

intersection_set = set1.intersection(set2)
print(f"Intersection set:", intersection_set)

difference_set = set1.difference(set2)
print(f"Difference set:", difference_set)

symmetric_difference_set = set1.symmetric_difference(set2)
print(f"Symmetric difference set:", symmetric_difference_set)
