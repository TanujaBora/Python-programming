import random
word_list = ["aardvark","baboon","camel"]

# TODO-1 - randomly select a word from the word_list and assign it variable chosen word then print it
chosen_word = random.choice(word_list)
print(chosen_word)

# TODO- 2 - ask the user to guess a word and the make the guess lower case
user_guess = input('Guess a letter: ').lower()
# TODO - 3 - check if the letter is in the given word if it is print right if not print wrong
for letter in chosen_word:
    if letter == user_guess:
        print("right")
    else:
        print("wrong")
