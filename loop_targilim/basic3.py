count = 10       #עובר על כל המספרים הדו ספרתיים (10-99), ומדפיס את המספרים שמסתיימים בספרה 7

while count>9 and count<100:
    if count % 10 == 7:
        print(count)
    count += 1
