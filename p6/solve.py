num1 = 0
num2 = 0
for i in xrange(1,101):
    num1 += i
    num2 += i*i
num1 = num1*num1

print num1-num2
