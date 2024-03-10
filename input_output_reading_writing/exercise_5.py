"""
Ćwiczenie 5
Podany jest plik tekstowy zawierający dane pomiarowe z elektrowni
wiatrowej (plik data.txt):
2023-03-31 12:00:00,2.3
2023-03-31 12:01:00,3.1
2023-03-31 12:02:00,2.7
Napisz program, który wczytuje ten plik tekstowy, przetwarza te
dane i oblicza całkowitą energię wygenerowaną przez elektrownię
wiatrową (druga kolumna pliku, energia wyrażona w MW).
Wynik wydrukuj do konsoli tak jak pokazano poniżej.
Oczekiwany wynik:
Total power generated: 8.10 MW
"""
with open('data_2.txt', 'r') as file:
    read_data_2 = file.read()

lines = read_data_2.split('\n')
total_power = 0

for line in lines:
    if line:
        power = float(line.split(',')[1])
        total_power += power

print(f'Total power generated: {total_power:.2f} MW.')

