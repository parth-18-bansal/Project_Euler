import time
start = time.perf_counter()

n = 600851475143
#n = 16
#n = 13195
prime_arr = bytearray([1]) * (n+1)

prime_arr[0] = 0
prime_arr[1] = 0

for i in range(2,(n+1)):
    if((prime_arr[i] == 1) and (i*i)<=n):
        for j in range(i*i, n+1, i):
            prime_arr[j] = 0

end = time.perf_counter()
print(f"Execution time: {end - start:.6f} seconds")
    
for i in prime_arr:
    print(i,end=" ")