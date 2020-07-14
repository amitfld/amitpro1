num = int(input('enter number:'))     #מקבלת מספר ומציירת משולש ישר זווית
str = ''

for i in range(1,num+1):
    for n in range(i):
        str += '*'
    print(str)
    str = ''