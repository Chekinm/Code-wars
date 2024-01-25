s =  111
x = 3


def count(power, curr_sum=0, prev_sum=None, max_sum=111, x=1, num=0, base_num=0, base_add=0):
    if prev_sum is None:
        prev_sum = {}
    if power not in prev_sum:
        prev_sum[power] = curr_sum
  
    weight = 2 ** (x * (power - 1)) if power else 1
    mask = 2**(power * x - 1) if power else 0
    print(bin(mask))
    s = curr_sum
    flag = True
    while num < 2**(power * x) + base_num:
        add1 = (bin(num & mask).count('1') + base_add) * weight
        add2 = prev_sum[power]
        print(f'{num=}, {bin(num).zfill(20)}, {add1=}, {add2=}')
        if s + add1 + add2 > max_sum:
            flag = False
            return (s if power != 1 else s + add1 + add2,
                    num,
                    flag,
                    prev_sum,
                    num,
                    bin(num & mask).count('1') + base_add,
                    )
        

        s += add1 + add2
        num += weight
    return s, num, flag, prev_sum, base_num, base_add

def main(max_sum, x, num=0, prev_sum=None):
    print(f'{max_sum=}, {x=}, {num=}')
    i = 1
    num = num
    s = 0
    base_num = 0
    base_add = 0
    flag = True
    prev_sum = prev_sum
    while s <= max_sum and flag:            
        s, num, flag, prev_sum, base_num, base_add = count(
            i,
            curr_sum=s,
            prev_sum=prev_sum,
            x=x,
            num=num,
            max_sum=max_sum,
            base_num=base_num,
            base_add=base_add
            )
        print(f'{s=}, {num=}, {flag=}, {s=}')
        if flag:
            i += 1
        if not flag:
            flag = True
            i = 1

    return s, num - 1
            


print(main(4096, 6))
