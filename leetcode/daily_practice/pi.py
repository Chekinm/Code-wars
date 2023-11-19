from random import randint
from math import pi

# square 1, 1

n = 100000000
count_in = 0

for i  in range (n):
    x = randint(-1000000, 1000000) 
    y = randint(-1000000, 1000000)  
    r = ( x * x  + y * y) 

    
    if r <= 1000000000000:
        count_in += 1

pi_num = 4 * count_in / n

print(pi_num)
print(pi)

    