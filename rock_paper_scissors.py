import random

choices = ['rock', 'paper', 'scissors']
computer_choice = random.choice(choices)

user_choice = input('Choose rock, paper or scissors:\n')

if user_choice == computer_choice:
    print("TIE")
elif user_choice == 'rock' and computer_choice== 'scissors':
    print("WIN - computer had " + computer_choice)
elif user_choice == 'paper' and computer_choice== 'rock':
    print("WIN - computer had " + computer_choice)
elif user_choice == 'scissors' and computer_choice== 'paper':
    print("WIN - computer had " + computer_choice)
else:
    print ("You lose :( computer had " + computer_choice)
