factor = int(input('enter factor: '))          #קולט פקטור. קולט חמישה ציונים.

sum = 0
new_sum = 0
count = 1
newgrade =0

while count<=5:
    grade = int(input('enter grade: '))
    sum += grade
    newgrade = grade + (grade * factor // 100)
    new_sum += newgrade
    print(newgrade)            #מדפיס לכל ציון את הציון החדש לאחר חישוב הפקטור
    count += 1

avg = sum/5
new_avg = new_sum/5

print('avg is :', avg, '\n', 'new_avg is :', new_avg, sep='')  #מדפיס ממוצע ציונים לפני הפקטור
print(new_avg - avg)                                           # מדפיס ממוצע ציונים לאחר פקטור
