# Zadanie1

# 1. Zdefiniuj listę “primes” zawierającą 10 kolejnych liczb pierwszych zaczynając od 2
# (https://www.matemaks.pl/liczby-pierwsze.html)
# 2. Wydrukuj długość tej listy
# 3. Dodaj na koniec listy 11tą liczbę pierwszą
# 4. Stwórz drugą listę “primes_four” zawierającą pierwsze 4 elementy “primes”
# 5. Wydrukuj ostatni z elementów “primes_four”
# 6. Używając funkcji sum() (https://docs.python.org/3/library/functions.html#sum)
# policz sumę “primes” i “primes_four”. Ile razy większa jest suma “primes” od “primes_four”?

print('Exercise1:')
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
print('"Prime" list contain', len(primes), 'elements')

#adding one more prime number to the end of the list
primes.append(31)
print('"Prime" list contain', len(primes), 'elements')

primes_four = primes[0:4]
print('"Prime_four" list contain', len(primes_four), 'elements')
print('Last element of "prime_four" list is', primes_four[-1])

sum_primes = sum(primes)
print('Sum of all elements in "prime" list is', sum_primes)
sum_primes_four = sum(primes_four)
print('Sum of all elements in "prime_four" list is', sum_primes_four, '\n')

#Zadanie2

# 1. Zapisz do zmiennej listę [22, 3.3, -2, 5, 701, 42, -120, 35, 69.9, 123, -444, 0.0, 0]
# 2. Używając funkcji sorted() (https://docs.python.org/3/library/functions.html#sorted)
# przypisz do innej zmiennej posortowaną listę z pierwszego punktu
# 3. Wydrukuj pierwszy i ostatni element nowej listy

print('Exercise2:')
the_list = [22, 3.3, -2, 5, 701, 42, -120, 35, 69.9, 123, -444, 0.0, 0]
the_sorted_list = sorted([22, 3.3, -2, 5, 701, 42, -120, 35, 69.9, 123, -444, 0.0, 0])

print('These are the elements of "the list"', the_list)
print('These are sorted elements of "the list"', the_sorted_list)

print('The first element of the sorted list is', the_sorted_list[0],
      '\nThe last lement of the sorted list is', the_sorted_list[-1], '\n')

#Zadanie3

# 1. Stwórz słownik opisujący ulubiony zespół (albo jakikolwiek zespół), który zawiera następujące klucze:
# a. name - nazwa zespołu
# b. country – kraj pochodzenia
# c. albums – lista tytułów albumów
# d. start_year - rok rozpoczęcia działalności
# e. albums_sold – liczba sprzedanych albumów
# 2. Dodaj do słownika nowy klucz: active – opisujący czy zespol jest aktywny (prawda/fałsz)
# 3. Dodaj do klucza albums nowy album na koniec listy
# 4. Wydrukuj wszystkie albumy
# 5. Zmien wartość active na przeciwną
# 6. Zwiększ wartość sprzedanych albumów o 1 (gratuluję zakupu!)

fav_band = {
    'name' : 'son_of_a_gun',
    'country' : 'Nowhere',
    'albums' : ['First_one', 'Never_done', 'Always_last'],
    'start_year' : '1990',
    'albums_sold' : 6_666_665
}

fav_band['active'] = False
fav_band['albums'].append('Last_of_the_lasts')

print(fav_band['albums'])

fav_band['active'] = not fav_band['active']
print(fav_band['active'])

fav_band['albums_sold'] = fav_band['albums_sold'] +1
#alternatywny zapis fav_band['albums_sold'] += 1
print(fav_band['albums_sold'])

# Zadanie4
#
# 1. W zmiennej “bands” stwórz listę 3 zespołów opisanych słownikami z zadania 3
# 2. Wydrukuj kraj pochodzenia ostatniego zespołu
# 3. Wydrukuj pierwszy album drugiego zespołu
# 4. Wydrukuj stan aktywności (klucz “active”) pierwszego zespołu

