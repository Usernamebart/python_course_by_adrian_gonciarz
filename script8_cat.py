# Zadanie1 z zajęć:
# 1. Stwórz klasę Cat
# 2. Niech kot przyjmuje imie w trakcie tworzenia
# 3. Stwórz dwa koty o różnych imionach

class Cat:
    def __init__(self, cat_name):
        self.cat_name = cat_name

first_cat = Cat('Miau')
second_cat = Cat('Mrau')

print(first_cat.cat_name)
print(second_cat.cat_name)

# Zadanie 2 z zajęć:
# 1.Pozwól opcjonalnie podać rasę kota / race = None
# 2. Stwórz metodę meow(), która wyprintuje “Meow!”
# 3. Stwórz metodę say_hello(), za pomocą której kot wydrukuje powitanie, poda swoje imie i jeśli zdefiniowany
# jest rasa kota – kota poda  swoją rasę
# 4. Do jednego ze stworzonych kotów dodaj rasę
# 5.Niech jeden z kotów zrobi meow!
# 6. Niech oba koty się przedstawią

class Cat:
    def __init__(self, cat_name, race = 'Whatever'):
        self.cat_name = cat_name
        self.race = race

    def meow(self):
        print("Meeeooooow")

    def say_hello(self):
        print(f'Hi I am a cat and my name is {self.cat_name}')
        if self.race:
            print(f'And my race is {self.race}.')
        else:
            print('Jestem dachowcem i nie mam rasy :(')

my_first_cat = Cat("No-one")
my_second_cat = Cat("Nevermind")
my_first_cat.meow()
my_first_cat.say_hello()
my_second_cat.say_hello()

# Zadanie 3 z zajęć:
# Dla klasy Cat z poprzedniego zadania
# 1. Dodaj w konstruktorze pole is_hungry o domyślnej wartości True
# 2. Dodaj metodę feed(), która zmieni wartość is_hungry an False
# 3. Dodaj metodę purr(), która wydrukuje napis “Purr, purr” ale tylko wtedy gdy kot nie jest głodny
# 4. Stwórz nowego kota, nakarm go i zamrucz
