"""
Ćwiczenie 24
Załóżmy, że pracujesz nad projektem symulacji lotów kosmicznych i
chcesz wyświetlić informacje tylko o tych misjach, które odbyły się
w przeszłości. Możesz to zrobić za pomocą pętli for i instrukcji continue.
Oto lista wszystkich misji kosmicznych:
missions = [
    {
        'name': 'Apollo 11',
        'date': '20.07.1969',
        'status': 'completed',
    },
    {
        'name': 'Mars Pathfinder',
        'date': '04.07.1997',
        'status': 'completed',
    },
    {
        'name': 'Chang\'e 4',
        'date': '03.01.2019',
        'status': 'in progress',
    },
    {
        'name': 'Cassini',
        'date': '15.10.1997',
        'status': 'completed',
    },
]
Napisz program, który wyświetli informacje tylko o tych misjach, które
nie mają statusu 'in progess'. Wynik wydrukuj do konsoli tak jak pokazano
poniżej.
Oczekiwany wynik:
Mission Apollo 11 took place on 20.07.1969
Mission Mars Pathfinder took place on 04.07.1997
Mission Cassini took place on 15.10.1997
"""
missions = [
    {
        'name': 'Apollo 11',
        'date': '20.07.1969',
        'status': 'completed',
    },
    {
        'name': 'Mars Pathfinder',
        'date': '04.07.1997',
        'status': 'completed',
    },
    {
        'name': 'Chang\'e 4',
        'date': '03.01.2019',
        'status': 'in progress',
    },
    {
        'name': 'Cassini',
        'date': '15.10.1997',
        'status': 'completed',
    },
]
for mission in missions:
    if mission['status'] == 'in progress':
        continue
    print('Mision', mission['name'], 'took place on', mission['date'])



