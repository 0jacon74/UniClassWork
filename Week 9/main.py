from human import Human
from robot import Robot

if __name__ == '__main__':
    human1 = Human()
    human1.display()
    robot1 = Robot()
    robot1.display()

    print(robot1)
    print(repr(robot1))
    print(human1)
    print(repr(human1))

