num1 = int(input('enter number: '))     #קולט מספר שאורכו לא ידוע. מדפיס את סכום ספרותיו
sum = 0

if num1 < 0:
    num1 *= -1

while num1//10 != 0:
    sum +=  num1%10
    num1 //= 10

sum += num1%10

print(sum)