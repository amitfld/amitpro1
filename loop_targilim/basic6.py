sum_pass = 0         #קולט ציונים. כל עוד נקלט ציון חוקי (0-100). מחשב ממוצע ציונים עוברים(לפחות 60) וממוצע של הציונים הנכשלים
sum_fail = 0
count_pass = 0
count_fail = 0

grade = int(input('enter grade between 0-100: '))

while grade>=0 and grade<=100:
    if grade >= 60:
        sum_pass += grade
        count_pass += 1
    else:
        sum_fail += grade
        count_fail += 1
    grade = int(input('enter grade between 0-100: '))

if(count_pass == 0):
    print('לא הוזנו ציונים עוברים')
else:print('pass avg:', sum_pass/count_pass)

if count_fail == 0:
    print('לא הוזנו ציונים נכשלים')
else:print('fail avg: ', sum_fail/count_fail)