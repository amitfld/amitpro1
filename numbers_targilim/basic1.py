day = int(input('enter day: '))      #מקבל תאריך מפורק ומרכיב לתאריך בפורמט dd/mm/yy
month = int(input('enter month: '))
year = int(input('enter year'))

print(day, '/', month, '/', year%100//10, year%10, sep='')