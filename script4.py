print('Today is friday')

is_day = True
if is_day:
    print('Sun is shining')

print('Let\'s have a beer')

temp_celsius = 0
pressure_hpa = 1013
if temp_celsius == 0 and pressure_hpa == 1013:
    print('In water freezing point')
else:
    print('Not in water freezing point')

print('Today is friday')

is_day = False
if is_day:
    print('Sun is shining')
else:
    print('Have a good night!')

print('Let\'s have a beer')

performance = 99.99

if performance >= 115:
    print('Excelent!')
elif performance >= 105:
    print('Very good!')
elif 100.00 <= performance >= 104.99:
    print('Alright!')
else:
    print('Not good enough! Work harder!')

price = 100
free_product = True
cash_amount = 90
N = price - cash_amount

if free_product:
    print('You get the product for free!')
if cash_amount >= price:
    print('You can buy this product.')
else:
    print('You need', N, 'more cash to buy this product')

my_list = [1, 3, 5, 7, 9, 11]
my_new_list = my_list[0:3]

for i in range(0, 100):
    print(i)
    print(i**2)

for i in range(1, 101):
    print(i)
    print(i**2)
for i in range(100, -1, -1):
    print(i)

for i in range(10):
#alternatywnie for _ in range(10):
    print('Python is super!')

my_list = [1, 3, 5, 7, 9, 11]

for i in my_list:
    print(i, i*4)
