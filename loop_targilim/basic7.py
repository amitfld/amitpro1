sum = 0              #קולט 5 מספרים בלולאה. סוכם את סכום הספרות הימניות של המספרים
count = 1

while count <= 5:
    num = int(input('enter number: '))
    sum += num%10
    count +=1

print(sum)