num = input('enter num of computer: ')     # קולט מספר מחשבים שטופלו היום. אם לא נקלט, ייחשב כ15(ברירת מחדל). יש להדפיס את מספר המחשבים שיש לטפל בהם מחר - כפול שתיים מהמספר היום

if num == "":
    num = 15
else:
    num = int(num)

print("tomorrow you will deal with:", num*2)