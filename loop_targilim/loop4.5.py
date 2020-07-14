num1 = int(input('enter number: '))     #קולט שני מספרים חיוביים.
num2 = int(input('enter number: '))

count = 0

while num1 < num2:                      #מוודא שהמספר הראשון גדול מהשני
    num1 = int(input('enter a bigger number: '))

while num2*count + num2 <= num1:        #מחשב את מנת החלוקה של המספר הראשון בשני(ללא אופרטור חילוק)
    count +=1

print(count)
print(num1 - (count*num2))              #מחשב שארית חלוקה של המספר הראשון בשני ללא אופרטור שארית