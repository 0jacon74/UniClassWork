
def listen():
    print("What sound did you hear?")
    sound = input()
    print("That was a loud "+ sound + "!")

#listen()
#basic function


def identity():
    see = input("What do you see? ")
    if see == "a large boulder":
        print("Its time to run!")
    else:
        print("We will be fine.")

#identity()

def escape(plan):
    if plan == "jumping over":
        print("We cannot escape that way! The boulder is too big!")
    elif plan == "running around":
        print ("We cannot escape that way! The boulder is moving to fast")
    elif plan == "cross bridge ahead":
        print ("That might just work! Let's go!")
    else:
        print("We cannot escape that way! The boulder is in the way!")

#escape("cross bridge ahead")
#User defined function with parameter

