str1 = input('enter sentance: ')

print(len(str1))                    #מדפיס את אורך המחרוזת

print(str1[2:6])                    #מדפיס את האות השלישית עד השישית במחרוזת

list1 = str1.split(' ')             #מפרק את המחרוזת איפה שיש רווח(מילה ראשונה) ויוצר רשימה
print(list1[0]*3)                   #מחזיר את המילה הראשונה 3 פעמים צמוד

str2 = str.capitalize(str1)         #יוצר מחרוזת חדשה מהמחזורת הישנה שהמילה הראשונה מתחילה באות גדולה
print(str2)