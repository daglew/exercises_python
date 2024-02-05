"""
Ćwiczenie 21
Utwórz poniższe dwa słowniki:
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
Następnie zaktualizuj słownik dict1 wartościami ze słownika dict2.
W odpowiedzi wydrukuj słownik dict1 do konsoli.
Oczekiwany wynik:
{'a': 1, 'b': 3, 'c': 4}
"""
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

dict1.update(dict2)
print(dict1)

