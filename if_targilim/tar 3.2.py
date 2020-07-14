num1 = int(input('enter number: '))   #מקבל שלושה מספרים ובודק מי מהם הוא הגדול ביותר. מדפיס הודעות בהתאם
num2 = int(input('enter number: '))
num3 = int(input('enter number: '))

if num1 == num2 or num1 == num3 or num2 == num3:
    print('error, you entered two equals numbers or more')
elif num1 > num2 and num1 > num3:
    print(num1, 'is the biggest')
elif num2 > num1 and num2 > num3:
    print(num2, 'is the biggest')
else:print(num3, 'is the biggest')