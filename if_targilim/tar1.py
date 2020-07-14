num1 = int(input('enter number: '))  # מקבל שני מספרים ובודק אם סכומם זוגי
num2 = int(input('enter number: '))

if (num2 + num1) % 2 != 0:
    print('e-zugi')
else:
    print('zugi')
