count = 10          #עובר על כל המספרים הדו ספרתיים (10-99), ומדפיס את סכום המספרים שמסתיימים בספרה 0
sum = 0

while count>9 and count<100:
    if count%10 == 0:
        sum += count
    count +=1

print(sum)