name = input('enter name: ')       #מקבל שם, גיל, עיר מגורים. מדפיס בשורה אחת
age = int(input('enter age: '))    # יש שימוש בפירמוט formatting
city = input('enter city: ')

print('my name is %s, i\'m %d years old, and i live in %s' % (name, age, city))