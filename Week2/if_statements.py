#print("Please enter an activity")
#answer = input()
#if answer == "Calculate":
#    print("Performing calculations...")
#else:
#    print("Performing activity...")
#print("Activity Completed!")

print("What direction should I move in (up, down, left, right)?")
direction = input()
if direction == "up":
    print ("I am moving in an upward direction!")
elif direction == "down":
    print ("I am moving in an downward direction!")
elif direction == "left":
    print ("I am moving left!")
elif direction == "right":
    print ("I am moving right!")
else:
    print ("That is not a direction!")