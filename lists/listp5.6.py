x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

x2 = x[7:10]        #יוצר רשימה חדשה מהרשימה הקיימת, המורכבת משלושת המספרים האחרונים של הרשימה
print(x2)

x2 = x[::-1]        #הופך את הרשימה, מדפיס אותה הפוכה
print(x2)

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(0,10,2):                #מדפיס את המספרים שנמצאים באינדקסים הזוגיים
    print(x[i])

x2 = []
for i in x:                 #יוצר רשימה חדשה המורכבת מהמספרים האי-זוגיים שנמצאים ברשימה המקורית
    if i%2 != 0:
        x2.append(i)
print(x2)

n1 = int(input('enter number: '))      #קולט 3 מספרים
n2 = int(input('enter number: '))
n3 = int(input('enter number: '))
x2 = [n1,n2]
x[4:6] = x2                            #מחליף את המספרים באינדקסים 4 ו-5 במספר שנקלט
x.append(n3)                           #מחליף את המספר האחרון ברשימה במספר שנקלט מהמשתמש
print(x)

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x2 = []
for i in x:                            #מרכיב רשימה חדשה שכוללת את המספרים מהרשימה המקורית מוכפלים ב2
    x2.append(i*2)
print(x2)

x2 = []
x2.append(x[0])                 #מרכיב רשימה חדשה המורכבת רק מהמספר הראשון והאחרון של הרשימה המקורית
x2.append(x[len(x)-1])
print(x2)