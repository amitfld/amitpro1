num = int(input('enter number: '))     #מקבלת מספר ומציירת משולש ישר זוית הפוך
str = ''

for i in range(1,num+1):
    for n in range(num,i-1,-1):
        str += '*'
    print(str)
    str = ''