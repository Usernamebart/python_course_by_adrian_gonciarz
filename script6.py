def say_hello():
    print('Hello!')

say_hello()

def poem():
    print('Na straganie w dzień targowy', 'Takie słyszy się rozmowy:', '"Może pan się o mnie oprze,',
          'Pan tak więdnie, panie koprze."', sep='\n')

poem()

unit = 'kilometers'

def drive(distance):
    print(f'Drive straight for {distance} {unit}')

def run(speed):
    print(f'Run with speed {speed} for 10 {unit}')

def drive_with_speed(distance, speed):
    print(f'Drive straight for {distance} {unit} with speed {speed}')

# printuje drive, run i drive_with_speed z okreslonymi w nazwiasach parametrami
drive(100)
run(33)
drive_with_speed(20, 30)


def divisible_by_three(awesome_number):
    if awesome_number % 3 == 0:
        print("foo")
    else:
        print("bar")

#alternatywny zapis
def divisible_by_three_alternative(awesome_number):
    print('foo' if awesome_number % 3 == 0 else 'bar')


divisible_by_three(3333)
#printowanie alternatywnego zapisu
divisible_by_three_alternative(10)

my_list = [2, 4, 55]
list_length = len(my_list)


def sum_two_numbers(a, b):
    return a + b


x = 3
y = 10
x_plus_y = sum_two_numbers(x, y)
print(x_plus_y)


def hypotenuse(a, b):
    return (a ** 2 + b ** 2) ** 0.5


c = hypotenuse(4, 4)
print(c)
print(hypotenuse(3, 4))


def multiple_returns():
    return 1, 2, 3


result1, result2, result3 = multiple_returns()

a = [1, 11, 13, 77, 101]
b = [2, 22, 222, 2424, 2311, 10002, ]
c = [3]
d = []


def select_even(lis):
    return [e for e in lis if e % 2 == 0]


print(select_even(d))


def calculations(a, b, c):
    input_sum = a + b + c
    input_product = a * b * c
    return input_sum, input_product


print(*calculations(11, 22, 123))

drive_data = (50, 90)
drive_with_speed(*drive_data)

position = (0, 10, 30)
position_list = list(position)
print(position_list)
