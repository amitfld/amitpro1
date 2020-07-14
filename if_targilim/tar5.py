num1 = int(input('enter number: '))    #מקבל שני מספרים. אם שניהם זוגיים מדפיס את סכומם. אם לא, מדפיס את מכפלתם
num2 = int(input('enter number: '))

if num1 % 2 ==0 and num2 % 2 ==0:
    print(num2 + num1)
else:print(num2*num1)