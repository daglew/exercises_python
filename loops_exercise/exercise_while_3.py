"""
Ćwiczenie 28
Załóżmy, że pracujesz nad projektem symulacji lotu kosmicznego,
w którym musisz kontrolować zużycie paliwa w rakiecie.
Do wykonania zadania potrzebujesz zadeklarować kilka zmiennych, takich jak:
ilość paliwa w rakiecie
ilość paliwa zużywanego na sekundę
czas lotu
Zadeklarowałeś już poniższe zmienne:
fuel = 100
fuel_consumption_rate = 10
time = 0
Napisz program, który będzie kontrolować zużycie paliwa w rakiecie.
Przed rozpoczęciem każdej jednostki czasu wydrukuj do konsoli informację
o pozostałych jednostkach paliwa. Gdy paliwo zostanie wyczerpane,
wydrukuj do konsoli 'End of flight.'
Wyniki wydrukuj do konsoli tak jak pokazano poniżej.
Oczekiwany wynik:
Fuel remaining: 100 units.
Fuel remaining: 90 units.
Fuel remaining: 80 units.
Fuel remaining: 70 units.
Fuel remaining: 60 units.
Fuel remaining: 50 units.
Fuel remaining: 40 units.
Fuel remaining: 30 units.
Fuel remaining: 20 units.
Fuel remaining: 10 units.
End of flight.
"""
fuel = 100
fuel_consumption_rate = 10
time = 0

while fuel > 0:
    print(f"Fuel remaining: {fuel} units.")
    fuel -= fuel_consumption_rate
    time += 1
print(f"End of flight.")



