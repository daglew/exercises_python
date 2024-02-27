"""
Ćwiczenie 29
Napisz program, który symuluje ładowanie baterii solarnych,
zakładając stałą moc ładowania baterii oraz pojemność baterii.
Podane są poniższe zmienne:
hour = 8
solar_power = 50
battery_capacity = 500
battery_level = 0
Bateria zaczyna ładowanie się o godzinie 8:00, a kończy o godzinie 15:00.
W każdej iteracji pętli while dodajemy do zmiennej battery_level wartość
solar_power, a następnie inkrementujemy wartość hour. Jeśli zmienna
battery_level osiągnie wartość battery_capacity lub będzie poza
zakresem czasowym ładowania, pętla zostanie przerwana. Po zakończeniu
pętli while, wyświetlamy aktualny poziom naładowania baterii solarnych
tak jak poniżej.
Oczekiwany wynik:
The solar battery charge level is: 350 Watt-hours.
"""
hour = 8
solar_power = 50
battery_capacity = 500
battery_level = 0
while hour < 15 and battery_level < battery_capacity:
    battery_level += solar_power
    hour += 1

print(f"The solar battery charge level is: {battery_level} Watt-hours.")





