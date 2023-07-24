# gas = [1, 2, 4 ,3, 4, 5, 4]
# cost = [3, 4, 4, 5, 1, 2, 4]
gas = [2,0,0,0,0,0,0] 
cost = [0,0,0,0,0,0,1]


def check_route(k, gas, cost):
    current_state = [0 for i in range(len(gas))]
    for i in range(k, len(gas) + k):
        n = i % len(gas)
        current_state[(n+1) % len(gas)] = current_state[n] + gas[n] - cost[n]
    return current_state


flag = False
for k in range(len(gas)):
    print(check_route(k, gas, cost))
#     if check_route(k, gas, cost):
#         print('We found a solution', k)
#         flag = True
#         break

# if not flag:
#     print('no solution')
