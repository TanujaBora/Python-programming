import random
# Rock Paper Scissors ASCII Art

Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''



Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_art = [Rock, Paper, Scissors]
user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: '))

if user_choice < 0 or user_choice >= 3:
    pass
else:
    print('you chose:')
    print(game_art[user_choice])
    computer_choice = random.randint(0,2)
    print('computer chose:')
    print(game_art[computer_choice])
# if user_choice == computer_choice:
#     print('it is a tie, play again')
# elif user_choice == 0 and computer_choice == 1:
#     print('you win')
# elif user_choice == 1 and computer_choice == 0:
#     print('you lose')
# elif user_choice == 2 and computer_choice == 1:
#     print('you win')
# else:
#     print('you lose')

if user_choice >= 3 or user_choice < 0:
    print('you typed an invalid number. you lose!')
elif user_choice == 0 and computer_choice == 2:
    print('you win!')
elif computer_choice == 0 and user_choice == 2:
    print('you lose!')
elif computer_choice > user_choice:
    print('you lose')
elif user_choice > computer_choice:
    print('you win')
elif user_choice == computer_choice:
    print('its a draw!')