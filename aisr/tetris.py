import asyncio
import os
import keyboard


class Field:  # will be our state
    

    def __init__(self):
        self.field = [['.'] * 10 for i in range(10)]


    def __str__(self):
        return '\n'.join([''.join(row) for row in self.field])


async def pr(a):
    while True:
        
        os.system('cls')
        print(a)
        await asyncio.sleep(1)


async def key_input(a, m, n):
    while True:
        a.field[m][n] = '.' 
        if keyboard.is_pressed("left"):
            n = n-1 if n > 1 else 0
        elif keyboard.is_pressed("right"):
            n = n + 1 if n < 8 else 9
        a.field[m][n] = 'x' 
        
        await asyncio.sleep(0.2)


async def main():
    a = Field()
    m = 5
    n = 5
    a.field[m][n] = 'x' 
    cr_command = key_input(a, m, n)
    cr_pr = pr(a)
    print(cr_command, cr_pr)
    await asyncio.gather(cr_pr, cr_command) 


asyncio.run(main())