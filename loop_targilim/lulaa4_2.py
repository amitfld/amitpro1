num = int(input('enter number: '))         #בודקת אם מספר שנקלט הוא ראשוני

for i in range(2, num):
    if num % i == 0:
        print('לא ראשוני')
        break
else:
    print('ראשוני')

