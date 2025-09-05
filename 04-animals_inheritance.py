from abc import ABC, abstractmethod

class Zoo:
    def __init__(self):
        self.animals_counter = {}
        self.animals = []

    def add_animal(self, animal):
        species = type(animal).__name__
        if species in self.animals_counter:
            self.animals_counter[species] += 1
        else:
            self.animals_counter[species] = 1

        self.animals.append(animal)

    def list_animals(self):
        return self.animals_counter

    def species_filter(self, species):
        filtered_animals = []

        for animal in self.animals:
            if isinstance(animal, species):
                filtered_animals.append(animal)
        
        for f in filtered_animals:
            print(f)


class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def speak():
        pass

    def present(self):
        return f"My name is {self.name} and I am {self.age} years old"
    
    def __str__(self):
        return f"Species: {self.__class__.__name__}, Name: {self.name}, Age: {self.age}"
    
class Dog(Animal):
    def speak(self):
        return "Woof, Woof! "

class Cat(Animal):
    def speak(self):
        return "Meoowww"

dog1 = Dog("Johnny", 10)
dog2 = Dog("John", 1)
cat1 = Cat("Luna", 5)
cat2 = Cat("Theo", 9)
cat3 = Cat("Leo", 2)

print(dog1.speak())
print(cat1.speak())

print(dog1.present())
print(cat1.present())

zoo = Zoo()
zoo.add_animal(dog1)
zoo.add_animal(dog2)
zoo.add_animal(cat1)
zoo.add_animal(cat2)
zoo.add_animal(cat3)

print(zoo.list_animals())

print("\n")
print("Showing all dogs with filter method:")
(zoo.species_filter(Dog))

print("\n")
print("Showing all cats with filter method:")
(zoo.species_filter(Cat))