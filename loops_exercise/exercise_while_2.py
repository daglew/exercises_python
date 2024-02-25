"""
Ćwiczenie 27
Załóżmy, że pracujesz nad projektem systemu, który ma na celu obliczenie
ilości składników potrzebnych do przygotowania określonej ilości wypieku
ciasta na podstawie przepisu. Zrób to za pomocą pętli while.
Oto przepis na przygotowanie porcji ciasta (podane wartości są wyrażone
w gramach):
proportions = {
    'flour': 500,
    'salt': 4,
    'sugar': 200,
    'butter': 200
}
Napisz program, który ma na celu obliczenie ilości składników potrzebnych
do przygotowania co najmniej 3000 gram ilości wypieku ciasta na podstawie
przepisu. Wynik wydrukuj do konsoli tak jak pokazano poniżej.
Oczekiwany wynik:
To prepare 3000 g of dough, you need:
Flour - 2000 g
Salt - 16 g
Sugar - 800 g
Butter - 600 g
"""
proportions = {
    'flour': 500,
    'salt': 4,
    'sugar': 200,
    'butter': 150
}
minimum_amount_of_baking = 3000
counter = 0
components = {}

while counter < minimum_amount_of_baking:
    for component, amount in proportions.items():
        if component not in components:
            components[component] = amount
        else:
            components[component] += amount
        counter += amount

print('To prepare', minimum_amount_of_baking, 'g of dough, you need:')
for component, amount in components.items():
    print(component.capitalize(), '-', amount, 'g')











