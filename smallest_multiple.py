# import math
# import time
# start = time.perf_counter()

# check = -1

# number = 20

# def smallest_multiple(x):
#     for i in range(2,21):
#         if(x%i !=0):
#             return False
    
#     return True

# while(check == -1):
#     if(smallest_multiple(number)):
#         print("Answer:",number)
#         check = 1
#     else:
#         number = number + 2

# end = time.perf_counter()
# print(f"Execution time: {end - start:.6f} seconds")



# 2nd way
import math
import time
start = time.perf_counter()
prime_arr = bytearray([1]) * 21

prime_arr[0] = 0
prime_arr[1] = 0

array_prime = []

for i in range (2,21):
    if(prime_arr[i] == 1 and i*i<=20):
        for j in range(i*i,21,i):
            prime_arr[j] = 0

for i in range(2,21):
    if(prime_arr[i] == 1):
        array_prime.append(i)

for i in array_prime:
    print(i, end = " ")

number = 1

for i in array_prime:
    n = i
    while(n<=20):
        if((n*i) <= 20):
            n = n * i
        else:
            break

    number = number * n
print(" ")
print("Answer:", number)

end = time.perf_counter()
print(f"Execution time: {end - start:.6f} seconds")