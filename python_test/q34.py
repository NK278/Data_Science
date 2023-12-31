class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def display(self):
        print(f"Nmae: {self.name} , Species: {self.species}")
class Dog(Animal):
    def __init__(self,name, species, breed, owner):
        super().__init__(name,species)
        self.breed=breed
        self.owner=owner
    def display(self):
        super().display()
        print(f"Breed: {self.breed} , Owner:{self.owner} ")
if __name__=="__main__":
    animal_instance = Animal(name="Tiger", species="Feline")
    print("Information about the Animal:")
    animal_instance.display()
    print("\n")
    dog_instance = Dog(name="Buddy", species="Canine", breed="Golden Retriever", owner="Alice")
    dog_instance.display()
