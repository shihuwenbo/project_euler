def is_palindrome(s):
    if(len(s) <= 1):
        return True
    if(s[0] == s[len(s)-1]):
        return is_palindrome(s[1:len(s)-1])
    return False

max = -1
for i in xrange(100, 1000):
    for j in xrange(100, 1000):
        prod = i*j
        if(is_palindrome(str(prod))):
            if(prod > max):
                max = prod

print max
