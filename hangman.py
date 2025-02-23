import random
# imports Python module random

# fetching the words from a text file, returns "default" if the file is not found
def get_random_word():
  try:
    with open("words.txt", "r", encoding="utf-8") as file:
      words = [line.strip() for line in file if line.strip()]
    return random.choice(words) if words else "default"
  except FileNotFoundError:
    print("Error: words.txt is missing!")
    return "default"

# shows the word with the correct guessed letters, or _ 
def display_word(word, guessed_letters):
  return " ".join(letter if letter in guessed_letters else "_" for letter in word)

# draws a hang man in different stages
def draw_hangman(attempts):
    stages = [
        """
         -----
         |   |
         |   O
         |  /|\\
         |  / \\
         |
        ---
        """,
        """
         -----
         |   |
         |   O
         |  /|\\
         |  / 
         |
        ---
        """,
        """
         -----
         |   |
         |   O
         |  /|\\
         |  
         |
        ---
        """,
        """
         -----
         |   |
         |   O
         |  /|
         |  
         |
        ---
        """,
        """
         -----
         |   |
         |   O
         |   |
         |  
         |
        ---
        """,
        """
         -----
         |   |
         |   O
         |  
         |  
         |
        ---
        """,
        """
         -----
         |   |
         |   
         |  
         |  
         |
        ---
        """
    ]
    print(stages[attempts])

# prints the game and chosen sentences in the terminal
def hangman():
  word = get_random_word()
  guessed_letters = set()
  attempts = 6

  print ("Welcome to the Hangman game")

  while attempts > 0:
    draw_hangman(attempts)
    print("The word:", display_word(word, guessed_letters))
    print(f"Guessed letters: {", ".join(guessed_letters)}")
    print(f"Attempts left: {attempts}")

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
      print("Please only enter ONE letter")
      continue

    if guess in guessed_letters:
      print("You have already guessed this letter...")
      continue

    guessed_letters.add(guess)

    if guess in word:
      print("Good guess! That letter is in the word")
      if all(letter in guessed_letters for letter in word):
        print("Congrats! You guessed the correcct word!:", word)
        return
      
    else:
      print("Sorry, that letter was not in the word...")
      attempts -= 1

  draw_hangman(attempts)
  print("Game over! The word was:", word)

# runs the program
if __name__ == "__main__":
  hangman()