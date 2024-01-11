class Solution:
    def countAndSay(self, n: int) -> str:

        def say(num: str) -> str:
            r = 0
            l = 0
            res = []    
            while r < len(num):
                curr_num_count = 0 
                while r < len(num) and num[r] == num[l]:
                    curr_num_count += 1
                    r += 1
                res.append(str(curr_num_count) + num[l])
                l = r
            return ''.join(res)
        
        res = '1' # base
        for i in range(n-1):
            res = say(res)
            
        return res
            
                
