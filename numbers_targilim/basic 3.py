name = input('enter name: ')        # מקבל שם, שנה נוכחית, וגיל. לאחר מכן גם שנה עתידית. מדפיס את גיל האדם בשנה העתידית
year = int(input('enter year: '))
age = int(input('enter age: '))

future_year = int(input('enter future year: '))

print(name, "will be", future_year-year+age)