"""
Ćwiczenie 22
Dana jest lista zawierająca nazwy plików w pewnym katalogu:
files = [
    'run_me.py',
    'README.md',
    'help.txt.',
    'script.py',
    'menu.py',
    'main.py',
    'py',
]
Stwórz generator o nazwie py_file_generator(), który przefiltruje podane
nazwy i będzie zwracał tylko nazwy plików z rozszerzeniem '.py'.

Uwaga: Aby zaliczyć ćwiczenie wystarczy zdefiniować generator.
Nie trzeba go wywoływać. Zaimplementowane testy sprawdzają
poprawność działania generatora.
"""
files = [
    'run_me.py',
    'README.md',
    'help.txt.',
    'script.py',
    'menu.py',
    'main.py',
    'py',
]


def py_file_generator(lista):
    for item in lista:
        if item.endswith('.py'):
            yield item


file_gen = py_file_generator(files)
