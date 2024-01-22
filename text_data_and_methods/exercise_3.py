"""
Ćwiczenie 13
Podana jest poniższa zmienna text zawierająca ciąg znaków:
text = ' Python '
Stwórz program, który wykorzystując odpowiednie metody tekstowe z
podanego ciąg znaków wydrukuje do konsoli poniższy tekst:
Original text:  Python
Uppercase text:  PYTHON
Lowercase text:  python
Stripped text: Python
Replaced text:  Cython
"""

text = ' Python '
print("Original text:", text)
print("Uppercase text:", text.upper())
print("Lowercase text:", text.lower())
print("Stripped text:", text.strip())
print("Replaced text:", text.replace('P', 'C'))

