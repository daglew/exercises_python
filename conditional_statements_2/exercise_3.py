"""
Ćwiczenie 13
Podane są dwie poniższe zmienne reprezentujące wzrost oraz wagę mężczyzny:
height = 1.85
weight = 85
Policz BMI dla tego mężczyzny i wydrukuj do konsoli tak jak pokazano poniżej.
Następnie w oparciu o wartość wskaźnika BMI wydrukuj do konsoli informację
korzystając z poniższych reguł:
bmi mniejsze niż 18.5 -> 'Underweight'
bmi większe lub równe 18.5 i mniejsze niż 25 -> 'Normal weight'
bmi większe lub równe 25 i mniejsze niż 30 -> 'Overweight'
bmi większe lub równe 30 -> 'Obese'
Oczekiwany wynik:
The patient's BMI is: 24.84
Normal weight
"""
height = 1.85
weight = 85
bmi = weight / (height ** 2)
print(f"The patient\'s BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("Underweight.")
elif bmi >= 18.5 and bmi < 25:
    print("Normal weight.")
elif bmi >= 25 and bmi < 30:
    print("Overweight.")
else:
    print("Obese.")


