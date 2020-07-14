sum = 0
num1 = int(input('enter 3 digits number: '))   #קולט מספר בלולאה כל עוד המספר תלת ספרתי. כשהמספר תלת ספרתי, מדפיס את סכום ספרותיו. אם הוא לא תלת ספרתי-נגמרת הלולאה ותודפס שגיאה
num2 = num1
count = 1

while int(num1//10 != 0):
    count += 1
    num1 //= 10

while count == 3:
    print('sum is:', num2 % 10 + num2 // 10 % 10 + num2 // 100)

    num1 = int(input('enter 3 digits number: '))
    num2 = num1
    count = 1
    while int(num1 //10 != 0):
        count += 1
        num1 //= 10

print('error')
