from math import sqrt
def min_square(n):

    sq = [i * i for i in range(1, int(sqrt(n))+1)]

    dp = {0:0, 1:1}
    
    for i in range(2, n+1):
        var = []
        k = 0
        while k < len(sq) and i-sq[k] in dp:
            var.append(dp[i-sq[k]] + 1)
            k += 1
        dp[i] = min(var)
    print(dp)
    return dp[n]

print(min_square(12))

        

