# Stores the name
WhileName = str(input("Enter your name: "))

while WhileName == str(): # Checks whether if there's a string in there or not
    print("I asked you for your name. Where is it.") # If there's nothing in the box prompt this shows up
    WhileName = str(input("Enter your name: ")) # Brings this prompt back again for the user to enter

print(f"Woop woop! Your name is {WhileName}!") # Boo yah!