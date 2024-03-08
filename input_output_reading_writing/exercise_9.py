"""
Ćwiczenie 10
Podane są poniższe informacje medyczne pacjenta:
first_name = 'Jan'
last_name = 'Kowalski'
weight = 75.5
height = 1.85
date_of_birth = '1990-01-01'
chronic_conditions = ['hypertension', 'diabetes']
medications = {
    'hypertension_medications': ['enalapril', 'hydrochlorothiazide'],
    'diabetes_medications': ['metformin'],
}


Za pomocą metody write() zapisz powyższe dane pacjenta do pliku o
nazwie patient_data.txt tak jak pokazano poniżej:
First name: Jan
Last name: Kowalski
Weight: 75.5 kg
Height: 1.85 m
Date of birth: 1990-01-01
Chronic conditions: hypertension, diabetes
Hypertension medications: enalapril, hydrochlorothiazide
Diabetes medications: metformin
"""
first_name = 'Jan'
last_name = 'Kowalski'
weight = 75.5
height = 1.85
date_of_birth = '1990-01-01'
chronic_conditions = ['hypertension', 'diabetes']
medications = {
    'hypertension_medications': ['enalapril', 'hydrochlorothiazide'],
    'diabetes_medications': ['metformin'],
}

with open('patient_data.txt', 'w') as file:
    file.write('First name: {}\n'.format(first_name))
    file.write('Last name: {}\n'.format(last_name))
    file.write('Weight: {} kg\n'.format(weight))
    file.write('Height: {} m\n'.format(height))
    file.write('Date of birth: {}\n'.format(date_of_birth))
    file.write('Chronic conditions: {}\n'.format(', '.join(chronic_conditions)))
    file.write('Hypertension medications: {}\n'.format(', '.join(medications['hypertension_medications'])))
    file.write('Diabetes medications: {}\n'.format(', '.join(medications['diabetes_medications'])))





