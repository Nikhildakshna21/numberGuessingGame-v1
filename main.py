import random
import math

max = int(input('enter the maximum number:'))
chance = 10
number = random.randint(1,max)
count = 0
guess = 0

if max < 10:
    chance= math.ceil(max/2)

print('you have {0} guesses'.format(chance))
print('lets start')

while count < chance:
    guess = int(input('enter your guess:'))

    if guess < number:
        count+=1
        print('your number is lesser than my number')
        print('try again. you have {0} more chance(s)'.format(chance-count))
    
    elif guess > number:
        count+=1
        print('your number is greater than my number')
        print('try again. you have {0} more chance(s)'.format(chance-count))

    elif guess == number:
        print('yay! you find my number in {0} chances. the number is {1}'.format(count,number))
        break
        
    