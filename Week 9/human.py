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