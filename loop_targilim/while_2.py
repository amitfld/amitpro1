age = int(input('enter name: '))     #קולט גיל בלולאה. כל עוד הגיל תקין (בין 0-120), מחזיר הדפסה לפי קבוצת גיל

while age >= 0 and age <= 120:
    if age>=0 and age<=18:
        print('child')
    elif age>=19 and age<=60:
        print('adult')
    elif age>=61 and age<=120:
        print('senior')
    age = int(input('enter name: '))

print('error')