day = int(input('enter day: '))      #מקבל תאריך מפורק ומדפיס תאריך בפורמט dd/mm/yy
month = int(input('enter month: '))
year = int(input('enter year: '))

if day<1 or day> 31 or month<1 or month>12 or year<1950 or year>2020:
    print('error')
else:print('the date is: ', day, '/', month,'/', int(year%100/10),int(year%10), sep='')

