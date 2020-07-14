num1 = int(input('enter number: '))  # מקבל מספר ובודק אם הוא בן 3 ספרות. אם כן מדפיס את סכום ספרותיו. אם לא מדפיס שגיאה
num2 = num1

if num1 < 0:
    num2 = num2 * -1

count = 1

while int(num1 / 10) != 0:
    count += 1
    num1 /= 10

if count == 3:
    print(num2 % 10 + num2 // 10 % 10 + num2 // 100)
else:
    print('error')
