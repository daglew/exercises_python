A = {1, 2, 3, 4, 5, 6, 7, 8, 9}
B = {7, 8, 9}
C = (8, 9)

print(A.issubset(B))
print(A.issubset({7, 8, 9}))
print(A.issuperset(C))
print(A.union(B))

print(A.intersection(B))

print(A.symmetric_difference(B))

print(A.copy())
