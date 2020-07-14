str = input('enter string: ')
tav = input('enter tav: ')
count = 0

for i in range(len(str)):
    if str[i] == tav:
        count +=1

print(count)