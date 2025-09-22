def guessing_game():
    target = 15
    guess = int(input("Enter your guess: "))
    while(guess!=target):
        if guess>target:
            print("Too high! Try again.")
        if guess<target:
            print("Too low! Try again.")
        guess = int(input("Enter your guess: "))
    return "Congratulations! You guessed it!"
