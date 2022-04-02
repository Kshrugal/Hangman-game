from random import choice

word = choice(["proj", "apes", "crypto", "code", "stonks"])

guessed = []
wrong = []

tries = 7

while tries > 0:

    out = ""
    for letter in word:# If the letter is in the word bank/word chosen
        if letter in guessed: 
            out = out + letter 
        else:
            out = out + "-"

    if out == word: 
        break

    print("Guess your word sean:", out)
    print(tries, "chances left")

    guess = input() # User input for guessing
    
    if guess in guessed or guess in wrong:
        print("Already guessed bruh", guess) # If the letter is already typed/guessed more than once
    elif guess in word:
        print("Yay")
        guessed.append(guess) # If user get the letter correct
    elif len(guess) > 1:
        print("Breh only one character")
        wrong.append(guess)# If user inputs more than one character
    else:
        print("Nope")
        tries = tries - 1
        wrong.append(guess)# If user gets guess wrong

    print()

if tries:
    print("You guessed the word, youre just lucky: ", word) # If user wins
else:
    print("You didn't get the word, L smh: ", word) # If user loses
