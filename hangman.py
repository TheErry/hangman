import random
#imports Python module random

def get_random_word():
  words = ["hello", "world", "python", "artificial", "intelligence", "programming"]
  return random.choice(words)

def display_word(word, guessed_letters):
  return " ".join(letter if letter in guessed_letters else "_" for letter in word)

def hangman():
  word = get_random_word()
  guessed_letters = set()
  attempts = 6

  print ("Welcome to the Hangman game")

  while attempts > 0:
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


  print("Game over! The word was:", word)

if __name__ == "__main__":
  hangman()