# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from datetime import date
from dataclasses import dataclass

@dataclass()
class Pets:
    species : str
    breed : str
    name : str
    color : str
    gender : str
    owner : str
    address : str
birthdate : date

def calculateAge(birthdate):
   today = date.today()
   age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
   return age

PetAge = calculateAge(date(2017, 2, 3))
print('The Age of the pet is', PetAge)

def printname(self):
    print('The name of the pet is', self.name, 'of species', self.species, 'of color', self.color)

x = Pets("Dog", "GoldenRetreiver", "Tom", "brown", "1", "John","123 abc st", "3-2-2017")
y = x.printname()

@dataclass()
class Dog(Pets):
    species : 'canis Familiaris'
    breed : str
    name : str
    color : str
gender : str

def printDog(self):
    print('The species, breed, name, color and Gender of the Dog is', self.species, self.breed, self.name, self.color, self.gender)

a = Dog("canis Familiaris", "labrador", "Rudy", "Black", "0", "Ron", "231 abc st", "3-5-2016")
b = a.printDog()

@dataclass()
class Puppy(Dog):
    birthdate : date

    def calculateAge(birthdate):
        today = date.today()
        ageYear = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        ageMonth = today.month - birthdate.month
        age = (ageYear * 12) + ageMonth
        return age

    Age = calculateAge(date(2017, 2, 3))
    print('The Age of the puppy in months is', Age)

    def play(self):
        print("'(___()'`;\n /, /`\n \\\\\"--\\\\'")

    print("'(___()'`;\n /, /`\n \\\\\"--\\\\'")