want = 'yes'
x = []

while want == 'yes':                         #קולט מספרים לרשימה מהמשתמש, כל עוד המשתמש רוצה להכניס מספרים
    x.append(int(input('enter number: ')))
    if input('do you want to continue? ') == 'yes':
        want = 'yes'
    else:
        want = 'no'

print('min is: ', min(x))                    #מדפיס את המינימוס ברשימה, את המקסימום ברשימה, ואת ממוצע הרשימה
print('msx is: ', max(x))
print('avg is: ', sum(x)/len(x))