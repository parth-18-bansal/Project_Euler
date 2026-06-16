# import time
# start = time.perf_counter()

# n = 10001

# number_of_primes = int((n/3) * 10)*2*2


# prime_arr = bytearray([1]) * (number_of_primes+1)

# prime_arr[0] = 0
# prime_arr[1] = 0

# for i in range(2,(number_of_primes+1)):
#     if((prime_arr[i] == 1) and (i*i)<=number_of_primes):
#         for j in range(i*i, number_of_primes+1, i):
#             prime_arr[j] = 0

# count = 0

# for i in range(2,number_of_primes+1):
#     if(count == 10001):
#         print(i-1)
#         break
#     else:
#         if(prime_arr[i] == 1):
#             count = count + 1

# end = time.perf_counter()
# print(f"Execution time: {end - start:.6f} seconds")


# 2nd way
import time
import math
start = time.perf_counter()

n = 10001

number_of_primes = int(n*((math.log(n)) + math.log(math.log(n)))) # prime number theorem

prime_arr = bytearray([1]) * (number_of_primes+1)

prime_arr[0] = 0
prime_arr[1] = 0

for i in range(2,(number_of_primes+1)):
    if((prime_arr[i] == 1) and (i*i)<=number_of_primes):
        for j in range(i*i, number_of_primes+1, i):
            prime_arr[j] = 0

count = 0

for i in range(2,number_of_primes+1):
    if(count == 10001):
        print(i-1)
        break
    else:
        if(prime_arr[i] == 1):
            count = count + 1

end = time.perf_counter()
print(f"Execution time: {end - start:.6f} seconds")


