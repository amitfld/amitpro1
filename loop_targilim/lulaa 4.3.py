from random import randint

num = randint(1,9)                      #מייצר מספר רנדומלי. המשתמש צריך לנחש את המספר בהכוונה של התכנית(קר/חם)
count = 0
guess = 0

while count == 0:
    guess = int(input('enter your guess: '))
    if(guess == num):
        print('this is the number, good guess!')
        break
    elif guess > num:
        print('your guess is higher than the number')
    else:
        print('your guess is lower than the number')