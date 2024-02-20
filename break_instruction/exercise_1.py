"""
Ćwiczenie 22
Załóżmy, że prowadzisz wypożyczalnię samochodów elektrycznych i chcesz
znaleźć pierwszy samochód z pełnym naładowaniem baterii ze swojej floty.
Zrób to za pomocą pętli for i instrukcji break.
Oto lista twoich samochodów elektrycznych w twojej flocie:
cars = [
    {'model': 'Tesla', 'mileage': 15000, 'battery_level': 100},
    {'model': 'Nissan', 'mileage': 30000, 'battery_level': 75},
    {'model': 'BMW', 'mileage': 5000, 'battery_level': 100},
    {'model': 'Ford', 'mileage': 20000, 'battery_level': 50}
]
Napisz program, który znajdzie pierwszy samochód z pełnym naładowaniem
baterii z podanej floty. Wynik wydrukuj do konsoli tak jak pokazano poniżej.
Oczekiwany wynik:
The first car with a full charge is: Tesla
"""
cars = [
    {'model': 'Tesla', 'mileage': 15000, 'battery_level': 100},
    {'model': 'Nissan', 'mileage': 30000, 'battery_level': 75},
    {'model': 'BMW', 'mileage': 5000, 'battery_level': 100},
    {'model': 'Ford', 'mileage': 20000, 'battery_level': 50}
]
category = "model"
for car in cars:
    if car["battery_level"] == 100:
        print("The first car with a full charge is:", car["model"])
        break

