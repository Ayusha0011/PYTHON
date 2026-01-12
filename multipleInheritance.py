class Animal:
    def __init__(self, name):   # 🛠️ fixed space
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):  # 👈 Multiple Inheritance
    pass

# Create instances
rabbit = Rabbit("Sheila")
hawk = Hawk("Richy")
fish = Fish("Bubbles")

# Run methods
rabbit.flee()    # Sheila is fleeing
hawk.hunt()      # Richy is hunting
fish.hunt()      # Bubbles is hunting
fish.flee()      # Bubbles is fleeing
rabbit.eat()     # Sheila is eating
