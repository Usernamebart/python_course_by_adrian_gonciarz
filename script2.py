description = 'My name is Bart. I work as a tester'
greeting = "Hello Friend!"

print('Moja ulubiona książka to "Wzgórze psów"')
print("W McDonald's kupuje tylko kawę")

#Escapowanie stringów poprzez '\'
print("Moja ulubiona książka to \"Wzgórze psów\"")
print('W McDonald\'s kupuje tylko kawę')

bio1 = 'Nazywam się Bart.'
bio2 = 'Pracuję jako tester.'

#sklejanie stringów
bio = bio1 + bio2
print(bio, sep=' ')

login = 'admin1'
password = 'haslo2020'

print(f'Login: {login}, password: {password}')

pi = 3.14
print(f'Pole koła o promieniu 2 to {pi * 2**2}')

#liczby integer (całkowite)
age = 38
thousand = 1_000
milion = 1_000_000

#liczby float (zmiennoprzecinkowe)
height = 1.82
weight = 74.
pi = 3.1415
atom_size = 1e-9

#typ wartosci zmiennej
print(f'Typ wartości przypisanej do zmiennej pi to {type(pi)}')

# ctrl+d = dubluje linijke w ktorej jestesmy

h = 3
a = 5
triangle_area = 1/2 * a * h
print(triangle_area)

#potęgowanie (w przykłądzie: potęga druga)

power_sum = h**2 + a**2
print(power_sum)

#pierwiastek drugiego stopnia z 3

sqrt_3 = 3**0.5
print(sqrt_3)

#boolean - Treu / False

is_adult = True # z małej litery nie zrozumie. Musi byćz dużej
is_boy = True
is_day = False

#iloczyn logiczny and
is_adult_boy = is_adult and is_boy

is_boy_or_day = is_boy or is_day

age = 20
can_ride_moto = age >= 24 #to przyjmuje wartość False, czyli zmienna can_ride_moto przyjmie wartość False
print(can_ride_moto)

#zamiana string na int
my_phone = '123123123'
my_phone_int = int(my_phone)

#zamiana int na string
lenght = 666
lenght_string = str(lenght)

