"""
Ćwiczenie 25
Załóżmy, że pracujesz nad projektem systemu zarządzania szkoleniami
wojskowymi i chcesz wyświetlić tylko te szkolenia, które są przeznaczone
dla określonego stopnia wojskowego. Zrób to za pomocą pętli for i
instrukcji continue.
Oto lista szkoleń wojskowych:
trainings = [
    {'name': 'Basic marksmanship', 'rank': 'Private'},
    {'name': 'Infantry tactics', 'rank': 'Corporal'},
    {'name': 'Art of war', 'rank': 'Sergeant'},
    {'name': 'Heavy weapons specialist', 'rank': 'Captain'},
    {'name': 'Advanced first aid', 'rank': 'Private'},
    {'name': 'Combat engineering', 'rank': 'Corporal'},
    {'name': 'Field intelligence', 'rank': 'Sergeant'},
    {'name': 'Military law', 'rank': 'Captain'},
    {'name': 'Parachuting', 'rank': 'Private'},
    {'name': 'Amphibious assault', 'rank': 'Corporal'},
    {'name': 'Counterterrorism', 'rank': 'Sergeant'},
    {'name': 'Military diplomacy', 'rank': 'Captain'},
]
Napisz program, który wyświetli tylko te szkolenia, które są przeznaczone
dla stopnia wojskowego  'Sergeant'. Wynik wydrukuj do konsoli tak jak
pokazano poniżej.
Oczekiwany wynik:
Training for rank Sergeant is: Art of war
Training for rank Sergeant is: Field intelligence
Training for rank Sergeant is: Counterterrorism
"""
trainings = [
    {'name': 'Basic marksmanship', 'rank': 'Private'},
    {'name': 'Infantry tactics', 'rank': 'Corporal'},
    {'name': 'Art of war', 'rank': 'Sergeant'},
    {'name': 'Heavy weapons specialist', 'rank': 'Captain'},
    {'name': 'Advanced first aid', 'rank': 'Private'},
    {'name': 'Combat engineering', 'rank': 'Corporal'},
    {'name': 'Field intelligence', 'rank': 'Sergeant'},
    {'name': 'Military law', 'rank': 'Captain'},
    {'name': 'Parachuting', 'rank': 'Private'},
    {'name': 'Amphibious assault', 'rank': 'Corporal'},
    {'name': 'Counterterrorism', 'rank': 'Sergeant'},
    {'name': 'Military diplomacy', 'rank': 'Captain'},
]
rank = 'Sergeant'
for training in trainings:
    if training['rank'] != rank:
        continue
    print(f"Training for rank {rank} is:", training['name'])
