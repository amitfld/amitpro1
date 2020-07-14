from random import randint

num = int(input('enter number between 0-100: '))         #המשתמש בוחר מספר בין 0 ל100 והתכנית מנחשת את המספר לפי הכוונה של המשתמש: נמוך מדי, גבוה מדי
guess = 10
times = 0
count = 0
answer = 'x'
range_low = 0
range_high = 100

while num<0 or num>100:
    num = int(input('invalid number, please enter number again: '))

guess = randint(range_low,range_high)

while count == 0:
    times += 1
    answer = input('my guess is : ' + str(guess)+ ', is it correct?')
    if(answer == 'correct'):
        print('it took me:', times, 'guesses')
        break
    elif answer == 'low':
        range_low = guess+1
        guess = randint(range_low,range_high)
    else:
        range_high = guess-1
        guess = randint(range_low,range_high)