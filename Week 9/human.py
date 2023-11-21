class Human:

    MAX_ENERGY = 100

    def __init__(self, name="Human", age=0, energy = MAX_ENERGY):

        self.name = name
        self.age = age
        self.energy = energy

    def display(self):
        print(f"I am {self.name}")

    def __repr__(self):
        return f'Human(name={self.name}, age={self.age})'

    def __str__(self):
        return f'Human {self.name} is {self.age} years old.'

    def grow(self):
        self.age = self.age + 1

    def eat(self, amount):
        self.energy = self.energy + amount

    def eat(self, amount, max=MAX_ENERGY):
        if self.energy < max:
            self.energy = self.energy + amount
            if self.energy > max:
                self.energy = max