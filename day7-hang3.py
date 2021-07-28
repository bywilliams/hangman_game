# how to Angela resolved the exercise
import random

from hangman_art import stages, logo
from hangman_words import word_list
# simplificar => from hangman_words import word_list, dai não precisa colocar o hangman_words.

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print(logo)

# Create blanks _ in Display
display = []
for _ in range(word_length):
    display += "_"

lives = 6
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Clear terminal
    print("\033c")

    if guess in display:
        print(f"You've already guessed {guess}")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")

    print(f"{' '.join(display)}")

    # Check if there are no more "_" left in 'display'. Then all letters have been guessed.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
