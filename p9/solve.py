solved = False
for c in xrange(1, 1001):
    for b in xrange(1, c):
        for a in xrange(1, b):
            if(a+b+c == 1000 and a*a+b*b == c*c):
                print a*b*c
                solved = True
                break
        if(solved == True):
            break
    if(solved == True):
        break
