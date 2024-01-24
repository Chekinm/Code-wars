def pi_function(s):
    pi = [0] * len(s)
    j = 0
    for i in range(1, len(s)):
        while j != 0 and s[j] != s[i]:
            j = pi[j - 1]
        if s[j] == s[i]:
            j += 1
        pi[i] = j
    return pi

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:

        pi_a = pi_function(a + '#' + s)[len(a):]
        pi_b = pi_function(b + '#' + s)[len(b):]
        
        la = len(a)
        lb = len(b)
        res = []

        for i in range(len(pi_a)):
            if pi_a[i] == la:
                ind = i - la + lb
                d = 0
                flag = True
                
                while d <= k and flag:
                    
                    if 0 <= ind - d < len(pi_a) and pi_b[ind - d] == lb:
                        res.append(i - la)
                        flag = False
                        break
                         
                    if 0 <= ind + d < len(pi_a) and pi_b[ind + d] == lb:
                        res.append(i - la)
                        flag = False
                        break
                    d += 1
    
        return res
            
            
        
            