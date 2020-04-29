import random

found = False
number = 0
while not found:
    number = random.randint(1, 1_000_000)
    found = number % 13 == 0

print(number)

#######

numbers_list = [1,3,15,17,90,112] # lista z liczbami
numbers_squared_list = [] # lista z liczbami podniesionymi do potegi drugiej
for i in numbers_list:
    numbers_squared_list.append(i ** 2) # dopisujemy do nowej listy elementu z listy z liczbami podniesionymi do kwadratu

# alternatywny zapis / lc => list comprehension / transformacja list
numbers_squared_by_lc = [i ** 2 for i in numbers_list]

########

numbers_list = [1,3,15,17,90,112]
numbers_squared_list = []
for i in numbers_list:
    if i % 3 == 0:
    numbers_squared_list.append(i ** 2)

# alternatywny zapis / lc => list comprehension / transformacja list
numbers_squared_by_lc = [i ** 2 for i in numbers_list if i % 3 == 0]

