import math
import time
start = time.perf_counter()

n = 600851475143

ans = 1

farr = []
complement = 0

square_root_n = math.isqrt(n)

for i in range(3,(square_root_n+1),2):
    if(n%i == 0):
        farr.append(i)

for i in farr:
    i_is_prime = 1
    j = 3
    square_root_i = math.isqrt(i)
    while(j<=square_root_i):
                if ((i%j) == 0):
                    i_is_prime=-1
                    break
                else:
                    j = j + 2

    if(i_is_prime == 1):
         ans = i

    x = int(n/i)

    x_is_prime = 1
    square_root_x = math.isqrt(x)
    k = 3
    while(k<=square_root_x):
                if ((x%k) == 0):
                    x_is_prime=-1
                    break
                else:
                    k = k + 2

    if(x_is_prime == 1):
         print("Largest Prime:",x)
         complement = 1
         break
    
if(complement == 0):
    print("Largest Prime:",ans)

end = time.perf_counter()
print(f"Execution time: {end - start:.6f} seconds")
