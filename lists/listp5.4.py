want = 'yes'
list1 = []
list2 = []

while want == 'yes':
    list1.append(int(input('enter num for list1: ')))        #מקבל מהמשתמש שתי רשימות
    want = input('do you want to continue? ')                #מדפיס את אורך הרשימה החדשה שמורכבת משתי הרשימות

want = 'yes'
while want == 'yes':
    list2.append(int(input('enter num for list2: ')))
    want = input('do you want to continue? ')

new_l = list1 + list2
print(len(new_l))
