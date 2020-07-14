grade = input('enter grade: ').split()

fail_count = 0
pass_count = 0

for x in grade:
    if int(x) >= 60:
        pass_count += 1
    else:
        fail_count += 1

print(pass_count, 'students passed')
print(fail_count, 'stufents failed')