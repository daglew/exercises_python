text = "Przykładowy \ntekst."

dir(text)
print(dir(text))
print(help(str.count))


print(text.capitalize())

print(text.title())

print(text.count('Przykładowy'))

print(text.startswith("Przy"))
print(text.startswith("jest"))
print("przykładowy.".startswith("prz"))
print(text.endswith("t."))
print(text.find("tekst"))
print(text[text.find("tekst"):])

