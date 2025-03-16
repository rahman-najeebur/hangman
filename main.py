import random
import hangman_words
import hangman_art

LIVES = 6

# TODO-01: print the hangman logo
print(hangman_art.logo)

# TODO-02: generate a random word
word = random.choice(hangman_words.word_list)
print(word)

# TODO-03: create blanks spaces
display = ""
for letter in word:
    display += "-"

print(f"word to guess: {display}")

# TODO-04: create a list which keep track of the correct letter placement.
correct_list = []
count = LIVES

# TODO-05: main logic
is_game_on = True
while is_game_on:
    # ask the user input
    guess_letter = input("Guess a letter: ").lower()

    display = ""
    if guess_letter in word:
        for letter in word:
            if letter == guess_letter:
                display += letter
                correct_list.append(letter)
            elif letter in correct_list:
                display += letter
            else:
                display += "-"

        print(display)
        print(hangman_art.stages[len(hangman_art.stages) - 1])
        if "-" not in display:
            is_game_on = False

    else:
        count -= 1
        print("You Guess a wrong Letter which is not in word. You Lose a Life.")
        print(hangman_art.stages[count])
        print(f"{15 * "*"} {count} / {LIVES} LIVES LEFT {15 * "*"}")
        if count <= 0:
            is_game_on =  False
