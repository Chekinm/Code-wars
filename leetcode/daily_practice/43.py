class Solution:
    def multiply(self, n1: str, n2: str) -> str:

        def sum_st(n1, n2):
            curr = 0
            res = []
            i = 1
            while i <= len(n1) and i <= len(n2):
                p = -i
                temp_res = int(n1[p]) + int(n2[p]) + curr
                res.append(str(temp_res % 10))
                curr = temp_res // 10
                i += 1
            while i <= len(n1):
                p = -i
                temp_res = int(n1[p]) + curr
                res.append(str(temp_res % 10))
                curr = temp_res // 10
                i += 1

            while i <= len(n2): 
                p = -i
                temp_res = int(n2[p]) + curr
                res.append(str(temp_res % 10))
                curr = temp_res // 10
                i += 1
            if curr:
                res.append(str(curr))

            return ''.join(reversed(res))


        def mult_by_num(num_st, number):
            curr = 0
            res = []
            i = 1
            number = int(number)

            while i <= len(num_st):
                p = -i
                temp_res = int(num_st[p]) * number + curr
                res.append(str(temp_res % 10))
                curr = temp_res // 10
                i += 1
            if curr:
                res.append(str(curr))
            return ''.join(reversed(res))



        if n1[0] == '0' or n2[0] == '0':
            return '0' 
        i = 1
        res = ''
        while i <= len(n2):
            p = -i
            res = sum_st(res, str(mult_by_num(n1, n2[p]))+'0'*(i-1))
            i += 1
        return res