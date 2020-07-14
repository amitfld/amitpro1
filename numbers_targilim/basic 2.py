num = int(input('enter 3 digits number:'))     #מקבל מספר בן 3 ספרות ומדפיס אותו הפוך

print(num%10*100+num//10%10*10+num//100%10)
