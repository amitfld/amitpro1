num = int(input('enter number: '))    #קולט מספרים כל עוד לא נקלט 0 (גם מספרים שליליים). יש להציג בסוף את המספר החיובי הכי נמוך שנקלט
min = 0
count = 0

while num != 0:
    if num > 0:
        if count == 0:
            count += 1
            min = num
        elif num < min:
            min = num
    num = int(input('enter number: '))

print(min)

