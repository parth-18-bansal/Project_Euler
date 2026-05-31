a = 10
b = 10

lp = 0

def palindrome(x):
    digits = []

    p = 0

    n = x

    while(n!=0):
        i = n // 10
        d = n - i*10
        digits.append(d)
        n = i

    i = 0
    j = len(digits) - 1

    while (i<j):
        if(digits[i] == digits[j]):
            i = i + 1
            j = j - 1

        else:
            p = -1
            break

    if(p == 0):
        if( x > lp ):
            lp = x

while (a<100):
    while (b<100):
        x = a * b
        palindrome(x)
        b = b + 1

    a = a + 1

print(lp)




# for i in digits:
#     print(i)


