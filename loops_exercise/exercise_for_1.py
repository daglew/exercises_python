"""
Ćwiczenie 26
Załóżmy, że pracujesz nad projektem systemu rezerwacji
pokojów hotelowych i chcesz wyświetlić tylko te pokoje,
które są dostępne w określonym przedziale czasowym.
Zrób to za pomocą pętli for i instrukcji continue.
Oto lista wszystkich pokoi hotelowych:
rooms = [
    {
        'number': 101,
        'available_dates': [
            '2023-05-10',
            '2023-05-11',
            '2023-05-12',
        ],
    },
    {
        'number': 102,
        'available_dates': [
            '2023-05-10',
            '2023-05-11',
        ],
    },
    {
        'number': 103,
        'available_dates': [
            '2023-05-11',
            '2023-05-12',
            '2023-05-13',
        ],
    },
    {
        'number': 105,
        'available_dates': [
            '2023-05-10',
            '2023-05-11',
            '2023-05-12',
            '2023-05-13',
        ],
    },
    {
        'number': 107,
        'available_dates': [
            '2023-05-11',
            '2023-05-12',
        ],
    },
    {
        'number': 110,
        'available_dates': [
            '2023-05-10',
            '2023-05-11',
            '2023-05-12',
            '2023-05-13',
        ],
    },
]
Napisz program, który wyświetli tylko te pokoje,
które są dostępne w określonym przedziale
czasowym - od 2023-05-11 do 2023-05-13 włącznie.
Wynik wydrukuj do konsoli tak jak pokazano poniżej.
Oczekiwany wynik:
Room number 103 is available.
Room number 105 is available.
Room number 110 is available.
"""
rooms = [
    {
        'number': 101,
        'available_dates': [
            '2023-05-10',
            '2023-05-11',
            '2023-05-12',
        ],
    },
    {
        'number': 102,
        'available_dates': [
            '2023-05-10',
            '2023-05-11',
        ],
    },
    {
        'number': 103,
        'available_dates': [
            '2023-05-11',
            '2023-05-12',
            '2023-05-13',
        ],
    },
    {
        'number': 105,
        'available_dates': [
            '2023-05-10',
            '2023-05-11',
            '2023-05-12',
            '2023-05-13',
        ],
    },
    {
        'number': 107,
        'available_dates': [
            '2023-05-11',
            '2023-05-12',
        ],
    },
    {
        'number': 110,
        'available_dates': [
            '2023-05-10',
            '2023-05-11',
            '2023-05-12',
            '2023-05-13',
        ],
    },
]
from_date = '2023-05-11'
to_date = '2023-05-13'

for room in rooms:
    if from_date not in room['available_dates'] or to_date not in room['available_dates']:
        continue
    print(f"Room number {room['number']}, 'is available.")


