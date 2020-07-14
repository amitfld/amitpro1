count = 0
num = int(input('enter number: '))          #קולט מספרים עד שנקלט המספר 0. סופר כמה מהם מתחלקים ב-3 או ב-3. מדפיס את התוצאה

while num != 0:
    if num%3 == 0 or num%7 == 0:
        count +=1
    num = int(input('enter number: '))

print(count)