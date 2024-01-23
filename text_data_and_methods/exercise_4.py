""""
Ćwiczenie 14
Podany jest poniższy ciąg znaków:
text = 'script.py view.jpg README.md main.py'
Stwórz program, który w podanym ciąg znaków zliczy liczbę wystąpień
rozszerzenia 'py'.
Wynik wydrukuj do konsoli tak jak pokazano poniżej.

Oczekiwany wynik:
The extension '.py' appears 2 times in the text.
"""

text = 'script.py view.jpg README.md main.py'
name = ".py"
quantity = text.count(name)
print(f'The extension \'{name}\' appears {quantity} times in the text.')
