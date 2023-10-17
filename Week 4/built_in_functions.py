
print("Program Started!")

letter = input("Please enter a standard character: ")

if len(letter) == 1:
    value = ord(letter)
    print("The ASCII code for "+ letter + " is " + str(value) + ".")
else:
    print("error: Input was not a single character")

print("Program Ended!")

