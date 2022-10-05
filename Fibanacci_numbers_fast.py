a, b = 1, 0
m = 10**9+7
for i in bin(int(input())):
    a, b = a*a+b*b, b*(a+a+b)
    if i == "1":
        a, b = b, a + b
    a %= m
    b %= m
print(b)