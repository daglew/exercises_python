"""
Ćwiczenie 1
Wykorzystując odpowiednią funkcję sprawdź typ podanych obiektów:
(1, 2, 3)
{1, 2, 3}
[1, 2, 3]
{1: 1, 2: 2, 3: 3}
'123'
123
W odpowiedzi wydrukuj każdy typ do konsoli w osobnej linii tak jak
pokazano poniżej.
Oczekiwany wynik:
<class 'tuple'>
<class 'set'>
<class 'list'>
<class 'dict'>
<class 'str'>
<class 'int'>
"""
object_types = [(1, 2, 3), {1, 2, 3}, [1, 2, 3], {1: 1, 2: 2, 3: 3}, '123', 123]
for object in object_types:
    print(type(object))


