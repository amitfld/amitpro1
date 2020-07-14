num1 = int(input('enter number: '))    #קולט שני מספרים בלולאה. כל עוד שניהם זוגיים, מדפיס את סכומם. כאשר אחד מהם או יותר, לא יהיה זוגי, ידפיס את מכפלתם
num2 = int(input('enter number: '))

while num1%2 == 0 and num2%2 == 0:
    print('sum is:', num2+num1)
    num1 = int(input('enter number: '))
    num2 = int(input('enter number: '))

print('multiply is:', num1*num2)