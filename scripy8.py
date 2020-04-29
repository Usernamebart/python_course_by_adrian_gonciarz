# abstrakcje i obiekty (reprezentacja bytów o wspólnych cechach)
# klasy posiadają cechy i zachowania

# metoda to funkcja ktora jest w  klasie

# dzisiaj budowanie klas z metoadami w środku

class Student:
    pass # nie robi nic ale klasa już jest widoczna dla kompilatora
    def __init__(self, name): # metoda zwana konstruktorem
        self.name = name # definicja zmiennej (kazda instancja bedzie miala inne zmienne) / self.name = pole klasy

    def greetings(self):
        print(f'Hello! My name is {self.name}')

student_kasia = Student('Kasia') # instancja klasy student
student_adam = Student('Adam') # instancja klasy student

# print(student_kasia.name)
# print(student_adam.name)

# printowanie z greetings

student_kasia.greetings()
student_adam.greetings()
