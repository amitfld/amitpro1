index = 0               #תכנית הקולטת 10 ציונים
sum = 0
wrong = 0

for i in range(10):
    grade = int(input('enter a grade between 0-100: '))
    for n in range(4):
        if grade<0 or grade>100:
            grade = int(input('error, enter grade again: '))      #בודקת על כל ציון אם הוא חוקי. אם לא מבקשת שוב- עד חמש פעמים
        else:                                                     #לאחר חמש פעמים תסתיים התכנית ותודפס שגיאה
            break                                                 #אם נצליח לקלוט 10 ציונים נדפיס ממוצע שלהם
    else:
        print('error')
        wrong =1
    if(wrong == 1):
        break
    else:
        sum += grade
else:
    print('avg is:', sum/10)

