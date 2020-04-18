# Exercise1

# Używając podanych zmiennych:
# first_name = 'James'
# last_name = 'Micheals'
# email = 'jmichaels@example.com'
# phone = '12343214433'
# age = 44
# Wydrukuj dokładnie tak sformatowany tekst:
# My name is James Michaels.
# I'm 44 years old.
# You can contact me via email: jmicheals@example.com or phone: 12343214433.

first_name = 'James'
last_name = 'Bond'
email = 'mynameisbond@james.bond'
phone = 'unknown_number'
age = 44

print(f"Exercise1:\n"
      f"My name is {first_name} {last_name}.\n"
      f"I'm {age} years old.\n"
      f"You can contact me via email: {email} or phone: {phone}.\n")

# Exercise2

# Zdefiniuj dwie zmienne (użyjesz ich poniżej):
#     • pi - zawierającą wartość liczby pi z dokładnością do czwartego miejsca po przecinku
#     • r - zawierającą promien koła o wartości 20
# Przypisz do nowych zmiennych:
#     • circumference - obwód koła o promieniu r
#     • area – pole koła o promieniu r

pi = 3.1415
r = 20

circumference = 2 * pi * r
area = pi * r**2

print('Exercise2:\n'
      'Circumference of the wheel with radius', r, 'is:', round(circumference,3), '\n'
      'Area of the wheel with radius', r, 'is:', round(area,3), '\n')

# Exercise3

# Używając twierdzenia Pitagorasa oblicz długość przeciwprostokątnej trójkąta prostokątnego z bokami przy kącie prostym o wartościach:
#     • a = 5
#     • b = 13
# Wynik wydrukuj z zaokrągleniem do dwóch miejsc po przecinku.
# Policz i wydrukuj pole i obwód tego trójkąta.

a = 5
b = 13

c = (a**2 + b**2)**0.5

# alternatywne obliczenie c:
# #c = (a**2)+(b**2)**0.5

circumference = a + b + c
area = (a * b) * 0.5

# alternatywne obliczenie pola:
#area = 0.5 * a * b


print('Exercise3:\n'
      'Lenght of the counter-rectangular triangle with sides at right angles', a, 'and', b, 'is:', round(c,2), '\n'
      'Circumference of the rectangular triangle with sides', a, ',', b, 'and', round(c,2), 'is:', round(circumference,2), '\n'
      'Area of the rectangular triangle with sides', a, ',', b, 'and', round(c,2), 'is:', round(area,2), '\n')

# Exercise4

# W pewnym sklepie wprowadzono promocję, z której skorzystać mogą osoby spełniające jeden z następujących warunków:
# 1. Wszystkie osoby powyżej 65 roku życia
# 2. Kobiety do 16 roku życia włącznie lub powyżej 45 roku życia
# 3. Mężczyźni od 20 do 40 roku życia włącznie
# Policz wartość zmiennej typu boolean can_use_promotion opisującą czy dana osoba może skorzystać z promocji dla następujących osób:
# · Marta, studentka w wieku 22 lat
# · Pan Marian, emeryt w wieku 72 lata
# · Pani Ewa, 46 letnia księgowa
# · Tomek, uczen w wieku 12 lat
# · Janusz, kierowca Passata w kwiecie wieku (40 lat)

person1 = 'Marta'
age = 22
gender = 'female'
can_use_promotion1 = (age>65) or ((gender=='female') and (age<=16 or age>45)) or ((gender=='male') and (age>=20 and age<=40))

person2 = 'Mr Marian'
age = 72
gender = 'male'
can_use_promotion2 = (age>65) or ((gender=='female') and (age<=16 or age>45)) or ((gender=='male') and (age>=20 and age<=40))

person3 = 'Mrs Ewa'
age = 46
gender = 'female'
can_use_promotion3 = (age>65) or ((gender=='female') and (age<=16 or age>45)) or ((gender=='male') and (age>=20 and age<=40))

person4 = 'Tomek'
age = 12
gender = 'male'
can_use_promotion4 = (age>65) or ((gender=='female') and (age<=16 or age>45)) or ((gender=='male') and (age>=20 and age<=40))

person5 = 'Janusz'
age = 40
gender = 'male'
can_use_promotion5 = (age>65) or ((gender=='female') and (age<=16 or age>45)) or ((gender=='male') and (age>=20 and age<=40))

print('Exercise4:\n'
      f'Can {person1} use promotion? - {can_use_promotion1}\n'
      f'Can {person2} use promotion? - {can_use_promotion2}\n'
      f'Can {person3} use promotion? - {can_use_promotion3}\n'
      f'Can {person4} use promotion? - {can_use_promotion4}\n'
      f'Can {person5} use promotion? - {can_use_promotion5}\n')

# alternatywne wyprintowanie z użyciem if'a
# if can_use_promotion1 == True:
#       print(f'Can {person1} use promotion? - Yes, {person1} can use promotion')
# else:
#       print(f"Can {person1} use promotion? - No, {person1} can't use promotion")
#
# if can_use_promotion2 == True:
#       print(f'Can {person2} use promotion? - Yes, {person2} can use promotion')
# else:
#       print(f"Can {person2} use promotion? - No, {person2} can't use promotion")
#
# if can_use_promotion3 == True:
#       print(f'Can {person3} use promotion? - Yes, {person3} can use promotion')
# else:
#       print(f"Can {person3} use promotion? - No, {person3} can't use promotion")
#
# if can_use_promotion4 == True:
#       print(f'Can {person4} use promotion? - Yes, {person4} can use promotion')
# else:
#       print(f"Can {person4} use promotion? - No, {person4} can't use promotion")
#
# if can_use_promotion5 == True:
#       print(f'Can {person5} use promotion? - Yes, {person5} can use promotion')
# else:
#       print(f"Can {person5} use promotion? - No, {person5} can't use promotion")
