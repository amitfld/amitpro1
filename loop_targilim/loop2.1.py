grade = int(input('enter grade: '))        #קולט ציונים כל עוד הציון חוקי (בין 0-100)
sum = 0
count = 0
max = 0

while 0 <= grade <= 100:
    if grade>max:
        max = grade

    sum += grade
    count += 1
    grade = int(input('enter grade: '))

avg = sum/count
print('highest grade is :', max, '\n', 'grades avg is :', avg, '\n','highest grade - grades avg is : ', max-avg, sep='')

#מדפיס: ציון גבוה ביותר, ממוצע ציונים, הפרש בין הציון הכי גבוה לממוצע