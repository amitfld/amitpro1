sum = 0

for i in range(5):
    price = int(input('enter price: '))
    sum = sum+price
    if sum>=1000:
        print('too expensive!!!')
        break
print(sum)