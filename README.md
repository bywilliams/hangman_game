 # Hangman Game Python Version

![Badge](https://img.shields.io/static/v1?label=PYTHON&message=3.8.10&color=blue&style=for-the-badge&logo=Python)

***

Game console made in Python with Pycharm IDE. 

* This project was made in Pycharm IDE 
* This project relies on internal components to function.

### **Intention**

***

The purpose of this project was to practice for & While Loops, if/else , Lists, Strings, range, Modules in Python.

___

___

### Explanation of the Game

The game asks the user to guess a letter of a secret word, if the user guesses some letter of the secret word, the game shows in which part of the word is the letter he hit. if errs loses 1 life and a part of the body appears in the gibbet, every time he errs the same happens, so if the whole body appears in the gibbet it is game over.

---

### Summary of the Code

This algorithm was made with <b>3 python files</b>, being one of them the main file that will start the game.

* **Class of the main file (day7-hang3)**
  Variables:
    - chosen_word = a string that will receive a random word from the word_list in the hangman_words class.
    - word_length = an integer that takes the total of existing characters in chose_word.
    - display = an empty list to receive the characters that will be guessed by the user.
    - lives = an integer to receive a user life numbers.
    - end_of_game = a boolean that is used in a loop as a condition for the game continue or not.
* **Module hangman_words**
  Variables:
    - word_list = a List that receives all the words used in the game.
* **Module hangman_art**
  Variables:
  - stages = a list that receives the art of user life stages in the form of ASCII.
  - logo = a String with the logo game in ASCII

#### Imports

###### In day7-hang3

    - import random;
    - from hangman_art import stages, logo;
    - from hangman_words import word_list

### Loops

Loop to run the game.

##### In day7-hang3.py

~~~python
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

~~~

> This while loop makes the main logic of the game, which is to check if the user still has enough life numbers to keep trying to hit all the letters that exist in the secret word.


# Image of Application

![image da aplicação](/home/kyorazo/curso_python_angela/Curso Angela/day 7/images/hangman.gif)

# Instalation

Clone this repository in your local machine with the command:

- git clone https://github.com/bywilliams/hangman_game.git


## Author

***

> William Silva -> [site e portfolio pessoal](https://bywilliams.github.io/site/)

**Thank you for following the documentation and explanation of this little algorithm.**