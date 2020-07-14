password = input('enter password: ')           #קולט סיסמא ואז קולט סיסמא לאימות. כל עוד נקלטת סיסמא לאימות שגויה, יש להמשיך לקלוט.
password2 = input('enter password again:')     #כאשר נקלטת סיסמא לאימות תקינה, יש להדפיס הודעה "הצלחה". לאחר חמש קליטות שגויה, יש לסיים את הקליטה ולהדפיס שגיאה-יותר מדי ניסיונות
count = 1

while password != password2 and count < 5:
    password2 = input('wrong password, enter password again:')
    count += 1

if count == 5:
    print('יותר מדי ניסיונות')
else: print('הצלחה')