#Zadanie2 - oblicznie BMI

# Napisz metodę calculate_bmi, która przyjmie 2 parametry:
#  • Wagę w kilogramach
#  • Wzrost w metrach
# I zwróci wartość współczynnika BMI dla tych danych https://pl.wikipedia.org/wiki/Wska%C5%BAnik_masy_cia%C5%82a
# Policz współczynnik BMI dla następujących danych:
#  • Waga 80.3 kg, wzrost 1.80m
#  • Waga 119.9 kg, wzrost 1.71m

def calculate_bmi(kg, m):
    return kg / m**2

kg1 = 80.3
m1 = 1.80
kg2 = 119.9
m2 = 1.71

your_bmi1 = calculate_bmi(kg1, m1)
your_bmi2 = calculate_bmi(kg2, m2)

print(f'With your weight {kg1}kg and your height {m1}m your BMI is: ', round(your_bmi1,2))
print(f'With your weight {kg2}kg and your height {m2}m your BMI is: ', round(your_bmi2,2))

#Zadanie3 - ryzyko chorób

# Napisz metodę która przyjmie wartość współczynnika BMI i wydrukuje status naszej wagi zgodnie z tabelą w artykule
# Wikipedii jako:
#  • Niedowaga
#  • Optimum
#  • Nadwaga
#  • Otyłość

def weight_status(bmi):
    if bmi < 18.5:
        print('With given BMI your weight status is: Underweight')
    elif 18.5 <= bmi < 24.50:
        print('With given BMI your weight status is: Optimum')
    elif 24.50 <= bmi < 30.0:
        print('With given BMI your weight status is: Overweight')
    else:
        print('With given BMI your weight status is: Obesity')

weight_status(26)

#Zadanie4 - Napisz skrypt, który zapyta użytkownika o wagę i wzrost następnie wydrukuje
#informację o statusie wagi (niedowaga/optimum/nadwaga/otyłość)

height = float(input('Tell me what is your height (in meters, eg. 1.75): '))
weight = float(input('And now tell me what is your weight (in kilos, eg. 70.0): '))

your_bmi = weight / height**2

if your_bmi < 18.5:
    print(f'With your height {height}m and weight {weight}kg your BMI is', round(your_bmi,2), 'so you are underweight :(')
elif 18.5 <= your_bmi < 24.50:
    print(f'With your height {height}m and weight {weight}kg your BMI is', round(your_bmi,2), 'so you have optimum weight :)')
elif 24.50 <= your_bmi < 30.0:
    print(f'With your height {height}m and weight {weight}kg your BMI is', round(your_bmi,2), 'so you are overweight :(')
else:
    print(f'With your height {height}m and weight {weight}kg your BMI is', round(your_bmi,2), 'so you have obsity! :(')
