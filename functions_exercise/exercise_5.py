"""
Ćwiczenie 5
Podane są poniższe zmienne:
x = 5
y = 3
expression1 = '2 * 3 + 5'
expression2 = 'x + y'
expression3 = 'max([5, 2, 8, 1, 9, 3])'
Wykorzystując odpowiednią funkcję wbudowaną, wykonaj wyrażenia języka
Python podane jako ciąg znaków - zmienne expression1, expression2 i
expression3. Wynik wydrukuj do konsoli tak jak pokazano poniżej.
Oczekiwany wynik:
The result of the expression1 is: 11
The result of the expression2 is: 8
The maximum value in the list is: 9
"""
x = 5
y = 3

expression1 = '2 * 3 + 5'
expression2 = 'x + y'
expression3 = 'max([5, 2, 8, 1, 9, 3])'

first_result = eval(expression1)
print('The result of the expression1 is:', first_result)
second_result = eval(expression2)
print('The result of the expression2 is:', second_result)
third_result = eval(expression3)
print('The maximum value in the list is:', third_result)


