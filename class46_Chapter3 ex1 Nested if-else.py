import random

winning_number = random.random()

number=int(input('Input any number of your choice '))
if number == winning_number:
    print('CORRECT! you have guessed the number')
else:
    if number >= winning_number:
        print('Too high')
    else:
        print('Too low')