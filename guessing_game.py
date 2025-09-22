def guessing_game():
    target = 15
    guess = int(input("Enter your guess: "))
    while(guess!=target):
        guess = int(input("Enter your guess: "))
        if guess>target:
            print("Too high! Try again.")
        if guess<target:
            print("Too low! Try again.")
    return print("Congratulations! You guessed it!")
