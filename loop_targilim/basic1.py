sum = 0         #קולט 6 מספרים בלולאה. מחשב את סכום המספרים ומדפיס ממוצע
count = 0

while count < 6:
    sum += int(input('enter number: '))
    count += 1

print('avg is: ', sum/6)