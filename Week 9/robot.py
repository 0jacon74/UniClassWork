class Robot:
    MAX_ENERGY = 100

    def __init__(self, name="Robot", age=0, energy=0):
        self.name = name
        self.age = age
        self.energy = energy

    def __repr__(self):
        return f'robot(name={self.name}, age={self.age})'

    def __str__(self):
        return f'Robot {self.name} is {self.age} years old.'

    def display(self):
        print(f"I am {self.name}")
