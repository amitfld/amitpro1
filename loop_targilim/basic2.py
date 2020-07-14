sum = 0        #קולט 6 מספרים בלולאה. מחשב סכום המספרים הזוגיים, ומדפיס את ממוצעם
count = 0
count_zugi = 0

while count < 6:
    num = int(input('enter number: '))
    if num%2 == 0:
        sum += num
        count_zugi += 1
    count += 1

print('avg is: ', sum/count_zugi)