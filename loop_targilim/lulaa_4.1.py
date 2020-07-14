num1 = int(input('enter number: '))            #קולט שני מספרים
num2 = int(input('enter number: '))

if num1<num2:
    for i in range(num1 + 1, num2):         #בודק מי מהם הגדול ואז מריץ לולאה לבדוק איזה מספרים ביניהם זוגיים (לא כולל אותם)
        if i % 2 == 0:
            print(i)
elif num2<num1:
    for i in range(num2 + 1, num1):
        if i % 2 == 0:
            print(i)
else:print('numbers are equals')


