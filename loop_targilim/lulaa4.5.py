how_many = int(input('how many number is sidra? : '))
x = []
add = 0

for i in range(how_many):
    if i == 0:
        x = [0]
    elif i == 1:
        x += [1]
    else:
        x.append(x[i-2] + x[i-1])

print(x)