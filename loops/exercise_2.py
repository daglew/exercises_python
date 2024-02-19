"""
Ćwiczenie 16
Podany jest ciąg znaków:
hashtags = '#weekend#good#time#'
Napisz program, który wydrukuje do konsoli wyciągnięte z tego tekstu słowa tak,
aby każde słowo znajdowało się w osobnym wierszu.
Oczekiwany wynik:
weekend
good
time
"""
hashtags = '#weekend#good#time#'
result = " "
for i in hashtags:
    if i != "#":
        result = result + i
    else:
        print(result)
        result = " "



