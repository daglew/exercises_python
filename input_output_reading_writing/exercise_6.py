"""
Ćwiczenie 7
Utwórz listę z podanych nazw technologii:
'python'
'java'
'sql'
'sas'
Następnie zapisz każdy element listy w nowej linii pliku techs.txt.
Oczekiwana zawartość pliku techs.txt:
python
java
sql
sas

Zwróć uwagę na ostatnią pustą linię.
"""

technology_list = ['python', 'java', 'sql', 'sas']

with open('tech_list', 'w') as file:
    for tech in technology_list:
        print(tech, file=file)






