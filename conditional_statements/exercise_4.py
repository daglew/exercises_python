"""
Ćwiczenie 7
Do zmiennej o nazwie year przypisz wartość 2024.
Następnie wykorzystując instrukcję warunkową sprawdź,
czy wartość zmiennej przechowuje rok przestępny.
W każdym z tych dwóch przypadków wydrukuj do konsoli odpowiednio:
'The year 2024 is a leap year.'
'The year 2024 is not a leap year.'
Oczekiwany wynik:
The year 2024 is a leap year.
"""
year = 2024

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('The year', year, 'is a leap year.')
else:
    print('The year', year, 'is not a leap year.')

