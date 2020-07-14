max_place = 0          #קולט 7 מספרים ומדפיס את המספר הסידורי של הערך הגבוה ביותר שנקלט
max_num = 0


for i in range(1,8):         #שימוש בלולאת for
    num = int(input('enter number: '))
    if(i == 1):
        max_place = i
        max_num = num
    elif num > max_num:
        max_num = num
        max_place = i

print(max_place)