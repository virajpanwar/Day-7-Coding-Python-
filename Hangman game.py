import random
from hangman_art import *
from hangman_words import *
from replit import clear

end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives=6

print(logo)
  #Testing code
print(f'Pssst, the solution is {chosen_word}.')

  #Create blanks
display = []
for _ in range(word_length):
      display += "_"
guessed=[]
while not end_of_game:
      guess = input("Guess a letter: ").lower()
      clear()
      if guess in guessed:
        print(f"Already guessed {guess}\n")
        print(f"{' '.join(display)}")
        print(stages[lives])
        continue
      if len(guess)>1:
        print("Please enter a single letter\n")
        print(f"{' '.join(display)}")
        print(stages[lives])
        continue
      guessed.append(guess)
      
      #Check guessed letter
      for position in range(word_length):
          letter = chosen_word[position]
          if letter == guess:
              display[position] = letter
              print(stages[lives])
      if guess not in chosen_word:
        print(f"{guess} is not in the chosen word")
        lives -= 1
        print(stages[lives])
      #Join all the elements in the list and turn it into a String.
      print(f"{' '.join(display)}")

      #Check if user has got all letters.
      if "_" not in display:
          end_of_game = True
          print("\nYou win.")
      if lives == 0:
        end_of_game = True
        print("\nYou lose.")
        print(stages[lives])
