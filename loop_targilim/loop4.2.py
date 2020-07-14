num = int(input('enter number: '))      #קולט מספר, מדפיס את הספרה השמאלית שלו (לא ידטע מכמה ספרות מורכב המספר)

while num//10 != 0:
    num //= 10

print(num)