class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is asleep")


class Dog(Animal):
    def __init__(self, name, breed, bark_volume):
        super().__init__(name)  # Call Animal's constructor
        self.breed = breed
        self.bark_volume = bark_volume

    def speak(self):
        print(f"{self.name} barks loudly at volume {self.bark_volume}!")


# Example usage:
dog = Dog("Rex", "German Shepherd", 10)

print(f"Name: {dog.name}")
print(f"Breed: {dog.breed}")
print(f"Is Alive: {dog.is_alive}")
dog.eat()
dog.speak()
