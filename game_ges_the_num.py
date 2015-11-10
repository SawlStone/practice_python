import random

step = 0

print('Hallo, what is your name?')
name = input()

number = random.randint(1, 20)
print('So, I set the number from 1 to 20.')

while step < 5:
    print('I set: ')
    player = input()
    player = int(player)

    step = step + 1
    if player < number:
        print('No, my number is higher')

    if player > number:
        print('No, my number is lower')

    if player == number:
        break

if player == number:
    print('Great, ' + name + '! shot numbers:', step)

if player != number:
    print('Wrong, my number is ', number)
