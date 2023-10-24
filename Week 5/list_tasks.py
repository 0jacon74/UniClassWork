#def directions(d1, d2, d3, d4):
#    steps = [d1, d2, d3, d4]
#    return (steps)

#def run_task_1():
#    list = directions("Move Forward", "Move Backwards", "Turn Left", "Turn Right")
#    print(list)

#run_task_1()

def movements(d1, n1, d2, n2, d3, n3, d4, n4):
    path = [d1, n1, d2, n2, d3, n3, d4, n4]
    return (path)


def run_task_2():
    print ("moving...")
    moving = movements("Move forward", 10, "Move backwards", 5, "Move Left", 3, "Move right", 1)
    print (moving)


run_task_2()