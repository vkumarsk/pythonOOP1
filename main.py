# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from datetime import date

class Pets:
  def __init__(self, species, breed, name, color, gender, owner, address, birthdate):
    self.species = species
    self.breed = breed
    self.name = name
    self.color = color
    self.gender = gender
    self.owner = owner
    self.address = address
    self.birthdate = birthdate



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


class Dog(Pets):
  def display2(self, species, breed, name, color, gender):
    self.species = 'canis Familiaris'
    self.breed = breed
    self.name = name
    self.color = color
    self.gender = gender

  def printDog(self):
      print('The species, breed, name, color and Gender of the Dog is', self.species, self.breed, self.name, self.color, self.gender)

a = Dog("canis Familiaris", "labrador", "Rudy", "Black", "0", "Ron", "231 abc st", "3-5-2016")
b = a.printDog()


class Puppy(Dog):
    def display3(self, birthdate):
        self.birthdate = birthdate

    def calculateAge(birthdate):
        today = date.today()
        ageYear = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        ageMonth = today.month - birthdate.month
        age = (ageYear * 12) + ageMonth
        return age

    Age = calculateAge(date(2017, 2, 3))
    print('The Age of the puppy in months is', Age)

    def play(self):
        print›("'(___()'`;\n /, /`\n \\\\\"--\\\\'")

    print("'(___()'`;\n /, /`\n \\\\\"--\\\\'")