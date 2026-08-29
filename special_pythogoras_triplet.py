import time
start = time.perf_counter()

x = 1000
ans = 0

for a in range(1,x+1):
    if(ans == 1):
        break

    for b in range(a,x+1):
        c = 1000 - a - b

        if(b>c or a>c):
            break

        if(((a*a) + (b*b)) == (c*c)):
            print(a,b,c)
            ans = 1
            print("Answer:",(a*b*c))
            break

end = time.perf_counter()
print(f"Execution time: {end - start:.6f} seconds")




