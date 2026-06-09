import math
import time
start = time.perf_counter()

check = -1

number = 20

def smallest_multiple(x):
    for i in range(2,21):
        if(x%i !=0):
            return False
    
    return True

while(check == -1):
    if(smallest_multiple(number)):
        print("Answer:",number)
        check = 1
    else:
        number = number + 2

end = time.perf_counter()
print(f"Execution time: {end - start:.6f} seconds")