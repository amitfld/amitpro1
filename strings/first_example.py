str1 = input('enter string: ')

print("=============================")
print('string * 2 = ', str1*2)                                   #ידפיס פעמיים
print("=============================")
print('first tav in string:      ', str1[0])                     #מתייחס לתו באינדקס הנתון בסוגריים המרובעות
print("=============================")
print('string lenght:   ', len(str1))                            #מתייחס לאורך של המחרוזת
print("=============================")

for i in str1:                                                   #רץ על המחרוזת. האינדקס פה יהיה התו עצמו במחרוזת, ולא ישמש כמיקום
    print('current tav in string:     ', i)
print("=============================")
print('last tav in string:     ', str1[len(str1)-1])             #מתייחס לתו האחרון במחרוזת.
print("=============================")

ch = input('enter tav: ')
print('is tav in string?(true or false):     ', ch in str1)      #מדפיס True או False תלוי אם התו נמצא במחרוזת
if ch in str1:                                                   #בודק אם התו נמצא במחרוזת ומחזיר הודעה מתאימה
    print('tav !!found!! found in string')
else:
    print('tav !!not!! found in string')
print("=============================")

if not ch in str1:                                               #בודק אם התו לא נמצא במחרוזת ומחזיר הודעה מתאימה
    print('tav !!not!! found in string')
else:
    print('tav !!found!! found in string')

print("=============================")

name = 'amit'                                                    #סוג נוסף של פירמוט באמצעות הצבה בסוגריים
age = 21
print('test format:    ''hello {0}, your name is {0}, and you are {1} years old'.format(name, age))
print("=============================")
print('test format:    'f'your name is: {name}, and you are {age} years old')

str2 = 'abcdef12345'
print('places 2 to 4:   ', str2[2:5])                            #מתייחס למחרוזת מהמיקום השני עד הרביעי(לא מתייחס למספר השני שכתבנו)
print("=============================")
print('from start to place 4:    ', str2[:5])                    #מתייחס למחרוזת מההתחלה עד התו הרביעי(המספר שכתבנו פחות 1)
print("=============================")
print(str2[5:])                                                  #מתייחס למחרוזת מהמיקום השלישי עד הסוף
print("=============================")
print(str2[1:7:2])                                               #מתייחס למחרוזת בין המיקום הראשון לשישי(לא כולל 7), בקפיצות של 2
print("=============================")
print(str2[7:1:-1])                                              # מתייחס למחרוזת מהמיקום השביעי עד השני(לא כולל 1) בקפיצה אחורה בגלל המינוס
print("=============================")
print(str2[::-1])                                                #מחזיר את המחרוזת הפוכה
print("=============================")
print(str2[-1])                                                  #מחזיר את התו האחרון במחרוזת
print("=============================")

adress = input('enter adress: ')
print('adress in separate lines:  ', adress.replace(' ', '\n'))  #מחזיר את המחרוזת כך שכל פעם שיש רווח, במקומו תרד שורה
print("=============================")
adress2 = str.capitalize(adress)                                 #יוצר מחרוזת חדשה שבנויה מהישנה, רק שהאות הראשונה במחרוזת, תהיה אות גדולה
print('same adress but capitalized:     ', adress2)
print("=============================")
print('makes a list of this adrerss, separated when space:    ', adress.split(' '))       # פקודה זו מפרקת את המחרוזת כרשימה, מפורקת, לפי תו שנגדיר לה (במקרה הזה רווח)