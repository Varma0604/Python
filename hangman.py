import random
from words import words
import string


def get_valid_word(words):
  word = random.choice(words) #randomly chooses letters from the list
  while "-" in word or " " in word:
    word  = random.choice(words)
  return word


def hangman():
  word =get_valid_word(words) 
  word_letters = set(word) #letters in the words
  alphabet = set(string.ascii_uppercase)
  used_letter = set() #what the user has guessed

  #getting the user input
  while len(word_letters) > 0:
    print("you have used these letters", " ".join(used_letter))
    #tell the user what the current word is
    word_list = [letter for letter in_word]
  
    user_letter = input("guess: ").upper()

    if user_letter in  alphabet - used_letter:
      used_letter.add(used_letter)
      if used_letter in word_letters:
        word_letters.remove(user_letter)

    elif user_letter in used_letter:
      print("You have already used this letter")

    else:
      print("Erro please try again")



hangman()