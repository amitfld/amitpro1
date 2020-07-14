age = int(input('enter age: '))   #מקבל גיל ובודק באיזה קבוצת גילאים הוא: ילד, מבוגר, זקן

if(age < 0):
    print('error')
elif (0 <= age <= 18):
    print('child')
elif 19 <= age <= 60:
    print('adult')
elif 61 <= age <= 120:
    print('senior')
else:print('error')

