def gcd(a, b):
    a, b = abs(a), abs(b)
    if b == 0:
        return a
    return gcd(b, a % b)
print(gcd(48, 9)) 
print(gcd(0, 5))   
print(gcd(-12, 8)) 