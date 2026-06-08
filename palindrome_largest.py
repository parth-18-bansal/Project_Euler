import math
import time
start = time.perf_counter()

largest_prime = 0

# def palindrome(x):
#     digits = []

#     n = x

#     while(n!=0):
#         i = n // 10
#         d = n - i*10
#         digits.append(d)
#         n = i

#     i = 0
#     j = len(digits) - 1

#     while (i<j):
#         if(digits[i] == digits[j]):
#             i = i + 1
#             j = j - 1

#         else:
#             return False

#     return True

def palindrome_str(x):
    return str(x) == str(x)[::-1]

for a in range(100,1000):
    for b in range(100,1000):
        x = a * b
        if (palindrome_str(x)):
            if (x > largest_prime):
                largest_prime = x

print(largest_prime)

end = time.perf_counter()
print(f"Execution time: {end - start:.6f} seconds")



