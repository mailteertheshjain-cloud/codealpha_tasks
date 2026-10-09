import random

words = ["apple", "tiger", "house", "chair", "mango"]
word = random.choice(words)
guessed = []
chances = 6

while chances > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"

    print("Word:", display)

    if display == word:
        print("You won!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed:
        print("Already guessed!")
    elif guess in word:
        guessed.append(guess)
        print("Correct guess!")
    else:
        chances -= 1
        print("Wrong guess! Chances left:", chances)

if chances == 0:
    print("You lost! The word was:", word)