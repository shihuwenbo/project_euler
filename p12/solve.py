import math

def count_divisors(n):
    cnt = 0
    for i in xrange(1, int(math.floor(math.sqrt(n)))+1):
        if(n%i == 0):
            if(i == math.sqrt(n) or i == 1):
                cnt += 1
            else:
                cnt += 2
    return cnt

num = 1
j = 2
while(True):
    if(count_divisors(num) > 500):
        print num
        break
    num += j
    j += 1
