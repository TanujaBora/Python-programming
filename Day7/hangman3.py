import random
word_list = ["aardvark","baboon","camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

''' TODO-1 - create an empty sting called palceholder
for each letter in chosen_word, add a _ placeholder'''
placeholder = ''
for letter in chosen_word:
    placeholder += "_"
print(placeholder)

end_game = False
correct_letters = []
# ask the user to guess a word and the make the guess lower case
while not end_game:
    user_guess = input('Guess a letter: ').lower()
    display = ""
# TODO - 2- create a "display' that puts the guess letter in the right position and _ in
    for letter in chosen_word:
        if letter == user_guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    if "_" not in display:
        end_game = True
        print("You win!")
    print(display)

