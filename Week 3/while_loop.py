
avoid = input("How many obstacles must I avoid?")
obstacles = 0

while obstacles < int(avoid):
    obstacles = obstacles + 1
    print ("Avoiding... Done! "+ str(obstacles) + " obstacles avoided.")

print("All obstacles have been avoided.")