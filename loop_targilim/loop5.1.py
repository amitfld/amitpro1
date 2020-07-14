oreh = int(input('enter oreh: '))         #קולט אורך ורוחב ומדפיס מלבן
rohav = int(input('enter rohav: '))
rohav_str = ''
oreh_str = ''

for i in range(rohav):
    rohav_str += '* '

print(rohav_str)

for i in range(oreh):
    oreh_str += '*'
    for n in range(rohav*2-3):
        oreh_str += ' '
    oreh_str += '*'
    print(oreh_str)
    oreh_str = ''


print(rohav_str)