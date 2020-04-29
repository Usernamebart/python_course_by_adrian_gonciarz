import random
import datetime

# Listy zawierające dane do losowania
female_fnames = ['Kate', 'Agnieszka', 'Anna', 'Maria', 'Joss', 'Eryka']
male_fnames = ['James', 'Bob', 'Jan', 'Hans', 'Orestes', 'Saturnin']
surnames = ['Smith', 'Kowalski', 'Yu', 'Bona', 'Muster', 'Skinner', 'Cox', 'Brick', 'Malina']
countries = ['Poland', 'United Kingdom', 'Germany', 'France', 'Other']

# current_year = datetime.datetime.now()
# birth_year = current_year.year - age

female_list = []
for r in range (0,5):
    f_firstname = random.choice(female_fnames)
    f_surname = random.choice(surnames)
    f_country = random.choice(countries)
    f_random_age = random.randint(5, 45)

    current_year = datetime.datetime.now()
    f_birth_year = current_year.year - f_random_age

    female_list.append(
        {
            'firstname' : f_firstname,
            'lastname' : f_surname,
            'email' : f'{f_firstname}.{f_surname}@example.com'.lower(),
            'age' : f_random_age,
            'country' : f_country,
            'adult' : f_random_age >=18,
            'birth_year' : f_birth_year
            }
        )

male_list = []
for r in range (0,5):
    m_firstname = random.choice(male_fnames)
    m_surname = random.choice(surnames)
    m_country = random.choice(countries)
    m_random_age = random.randint(5, 45)

    current_year = datetime.datetime.now()
    m_birth_year = current_year.year - m_random_age

    male_list.append(
        {
            'firstname' : m_firstname,
            'lastname' : m_surname,
            'email' : f'{m_firstname}.{m_surname}@example.com'.lower(),
            'age' : m_random_age,
            'country' : m_country,
            'adult' : m_random_age >=18,
            'birth_year' : m_birth_year
            }
        )

# check if famel list is filled with random data
# print(female_list[0:6])
# check if male list is field with random data
# print(male_list[0:6])

for f in female_list:
    print(f"Hi! I'm {f_firstname}{f_surname}. I come from {f_country} and i was born in {f_birth_year}")

for m in male_list:
    print(f"Hi! I'm {m_firstname}{m_surname}. I come from {m_country} and i was born in {m_birth_year}")
