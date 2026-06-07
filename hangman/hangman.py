import random
from random_word import RandomWords
hangman_stages = [
    """
     -----
     |   |
         |
         |
         |
         |
    =========""",
    """
     -----
     |   |
     O   |
         |
         |
         |
    =========""",
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========""",
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    """
     -----
     |   |
     O   |
    /|\  |
         |
         |
    =========""",
    """
     -----
     |   |
     O   |
    /|\  |
    /    |
         |
    =========""",
    """
     -----
     |   |
     O   |
    /|\  |
    / \  |
         |
    ========="""
]
w=RandomWords()
print("loading word...")
word=w.get_random_word()
print(word)
n=len(word)
display=["-"]*n
print("-"*n)
count=0
guess=input(("guess the correct letter:")).lower()
while True:
    right=0
    for i,letter in enumerate( word):
        if letter==guess:
            display[i]=letter
            right=1
    if(right==0):
        count+=1
        print(f"wrong!!you have {6-count} chances")
    print(hangman_stages[count])
    if count==6:
        print("you faile!!your man is hanged")
        break       
    print("".join(display))
    if "".join(display)==word:
        print("YOU WON THE GAME!")
        break
    print()
    guess=input(("guess the correct letter:")).lower()
