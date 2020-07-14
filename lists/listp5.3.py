from random import randint
x = []
num = 0                                 #מייצרת 10 מספרים אקראיים בין 1 ל1000 ויוצרת מהם רשימה

for i in range(10):
    num = randint(1,1000)
    x.append(num)

print(x)