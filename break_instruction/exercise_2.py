"""
Ćwiczenie 23
Załóżmy, że pracujesz nad projektem systemu monitorowania
paneli fotowoltaicznych i chcesz znaleźć pierwszy panel,
który osiągnął moc wyjściową powyżej określonego poziomu.
Możesz to zrobić za pomocą pętli for i instrukcji break.
Oto lista twoich paneli fotowoltaicznych:
panels = [
    {'id': 1, 'output_power': 200},
    {'id': 2, 'output_power': 150},
    {'id': 3, 'output_power': 250},
    {'id': 4, 'output_power': 180},
]
Napisz program, który znajdzie pierwszy panel, który osiągnął
moc wyjściową powyżej 200. Wynik wydrukuj do konsoli tak jak
pokazano poniżej.
Oczekiwany wynik:
The first panel with an output power greater than 200 is: 3
"""
panels = [
    {'id': 1, 'output_power': 200},
    {'id': 2, 'output_power': 150},
    {'id': 3, 'output_power': 250},
    {'id': 4, 'output_power': 180},
]
power = 200
for panel in panels:
    if panel['output_power'] > power:
        print(f"The first panel with an output power greater than {power} is: {panel['id']}")
        break



