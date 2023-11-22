big_tuple = (
    set(((0,0),(1,0))),
    set(((1,0),(1,1))),
    set(((1,0),(1,1),(1,2))),
    set(((1,0),(1,1),(1,2))),
    set(((1,1),(1,2),(1,3))),
    set(((1,1),(1,2),(1,3))),
    set(((1,2),(1,3),(1,4))),
    # set(((1,3),(1,4))),
    # set(((0,4),(1,4)))
)
big_set = list(big_tuple)

big_set.sort(key=len)

new_set = []
new_set.append(big_set[0])

print(f'{new_set=}')
i = 0

while i < len(big_set):
    while i < len(big_set):
        
        if not any(bool(big_set[i].intersection(st)) for st in new_set):
            new_set.append(big_set[i])
            print(new_set)
        i +=1 



print(f'{new_set=}')
            