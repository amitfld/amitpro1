num1 = int(input('enter number: '))    #מקבל מספרים ובודק את ההפרש ביניהם
num2 = int(input('enter number: '))

if(num1 == num2):
    print('0')
elif num2 > num1:
    print(num2 - num1)
else:print(num1 - num2)