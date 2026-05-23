import time
start = time.perf_counter()

n = 600851475143
prime_arr = [True] * (n+1)

prime_arr[0] = False
prime_arr[1] = False

for i in range(2,(n+1)):
    if(prime_arr[i] and (i*i)<=n):
        for j in range(i*i, n+1, i):
            prime_arr[j] = False

end = time.perf_counter()
print(f"Execution time: {end - start:.6f} seconds")
    
for i in prime_arr:
    print(i,end=" ")