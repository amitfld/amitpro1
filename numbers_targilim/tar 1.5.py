cursalary = int(input('enter your current salary:'))    #מקבל משכורת ואחוז גידול למשכורת, ומדפיס משכורת חדשה
precent = int(input('eneter the percentage of increase in salary:'))

new_salary= cursalary*precent/100 + cursalary

print('your new salary is:', new_salary)