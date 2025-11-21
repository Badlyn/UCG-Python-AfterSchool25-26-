SecretNum = 7

guess = ()

while guess != SecretNum:
    guess = int(input("Guess the number between 1 and 10: "))

    if guess == SecretNum:
        print("Wow you're like the coolest guy ever. You like, won dude. Congrats on winning or something.")
    elif guess < SecretNum:
        print("Too low! Too friggan' slow! 🚶")
    elif guess > SecretNum:
        print("Too high! Too friggan' fast! 🏃")
