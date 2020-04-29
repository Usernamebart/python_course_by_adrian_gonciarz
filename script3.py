#Przykłady funkcji

print('Hello')
a = round(3.1415, 2)
print(a)

x, y = 10, -7
greater_number = max(x, y)
lesser_number = min(x, y)
print(greater_number)
print(lesser_number)

#abs -> funkcja wartości bezwzględnej
print(abs(-121))

#Zadanie 1

# Mając dane:
# a, b, c = 12.4, 3, -50
# oraz funkcje min(), abs(), print() wydrukuj wartość bezwzględną najmniejszej z nich. Czy potrafisz zrobić to w jednej linijce?

a, b, c = 12.4, 3, -50
min_number = min(a, b, c)
abs_min_number = abs(min_number)
print(abs_min_number)
print(abs_min_number)
print(abs(min(a, b, c)))

#################

first_name = 'bart'
print(first_name.upper())
print(first_name.capitalize())

#Zadanie2

# Używając zmiennych
# name, company = 'ricardo', 'fbi'
# oraz method upper() i capitalize() wydrukuj zdanie:
# "Officer Ricardo works for FBI"

name, company = 'ricardo', 'fbi'
print(f'Officer {name.capitalize()} works for {company.upper()}')

#################

### LISTY ###

friends = ['John', 'Thomas', 'Kate', 'Martha']
print(friends[0])
print(friends[2])
#drukujemy długość listy
print(len(friends))
#.append -> dodajemy element na koniec listy
friends.append('Andrew')
print(friends[4])
print(len(friends))
print(friends[-2])
#nadpisujemy/zmieniamy element z indexem 0
friends[0] = 'George'
print(friends[0])

#Zadanie3

# Wykonaj poniższe:
# a.Stwórz listę swoich 5 ulubionych filmów
# b.Wydrukuj długość listy
# c.Wydrukuj 3 element tej listy
# d.Dodaj na koniec listy element “Joker”
# e.Wydrukuj ostatni element na liście
# f.Wydrukuj dwa pierwsze elementy listy

movies = ['Se7en', 'Fight Club', 'Black Hawk Down', 'Memento', 'Iron Man'],
print('List contains', len(movies), 'elements')
print('Third element of the list is', movies[2])
movies.append('Joker')
print('Last element of the list is', movies[-1])
print('First two elements of the list are', movies[0], 'and', movies[1])
#alternatywny zapis print('First two element of the list are', movies[0:2])

### SŁOWNIKI ###

friend = {
    #pary klucz: wartość
    'email': 'andrew@mail.com',
    'city': '3city',
    'age': 38,
    'has_pets': False,
    'favourite_bands': ['Slayer', 'Metallica'],
}
print(friend['age'])
# print(*friend, sep=', ')
friend['has_pets'] = True
friend['favourite_bands'].append('Anthrax')
friend['company'] = 'Fake Co.'

print(friend)

#usuwanie całego klucza
# del friend['city']

#Zadanie 4

#słowmik dla Polski

poland = {
    'country_name': 'Poland',
    'language': 'Polish',
    'population': 37_970_000,
    'capital': 'Warsaw',

    'famous_people': ['Grażyna', 'Andrzej']
}
print(poland['famous_people'][-1])

#Zadanie 5

# Utwórz listę 3 słowników zawierających opis krajów: Polska, Francja, Kanada.
# Następnie wydrukuj:
# a.Stolicę ostatniego kraju
# b.Populację pierwszego kraju
