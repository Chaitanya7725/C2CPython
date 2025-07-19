# class Animal:
#     def __init__(self, name, species, color): 
#         self.name = name
#         self.species = species
#         self.color = color

# class Amphibian(Animal):
#     def __init__(self, name, species, color, adaptation):
#         super().__init__(name, species, color) 
#         self.adaptation = adaptation
#         self.has_backbone = True
#         self.blood_type = 'cold'
    
#     def adapt(self):
#         threatened = True
#         if threatened:
#             print(f'The {self.name} is a {self.color} {self.species} that will use their {self.adaptation} to protect themselves. ')


# salamander = Amphibian('Olm', 'salamander', 'pink', 'electrosensitive organs that can sense electrical fields')
# frog = Amphibian('Froggy','frog', 'pink', 'electrosensitive organs that can sense electrical fields')


# salamander.adapt()


class People:
  def __init__(self,name,age,gender):
    self.name = name
    self.age = age
    self.gender = gender

class Student1(People): 
    def __init__(self, name, age, gender, grade, gradYear): 
        super( ).__init__(name, age, gender) 
        self.grade = grade
        self.gradYear = gradYear
    
    def talk(self):
        print('My name is ' , self.name)
        print('My age is ' , self.age)
        print('My gender is ' , self.gender)
    
    def graduate(self):
       print("I am graduating in ", self.gradYear)

class Student2(People): 
    def __init__(self, name, age, gender, grade, gradYear): 
        super( ).__init__(name, age, gender) 
        self.grade = grade
        self.gradYear = gradYear
    
    def talk(self):
        print('My name is ' , self.name)
        print('My age is ' , self.age)
        print('My gender is ' , self.gender)
    
    def graduate(self):
       print("I am graduating in ", self.gradYear)


john1 = Student1('John1',15,'Male','A',2026) #new object of student class
# john2 = Student2('John2',16,'Male','B',2027) #new object of student class

john1.talk()
john1.graduate()

# john2.talk()
# john2.graduate()

import random

random_odd_number = random.randrange(1, 71)
print(random_odd_number)