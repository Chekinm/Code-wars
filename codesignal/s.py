
def solution(s):
    def diff (str1, str2):
        n = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                n += 1
        return n     
    len1 = len(s)
    answer = deque()
    answer.append(s[0])
    s.pop(0)
    flag = True
    while len(s) and flag:
        flag = False
        for i in range(len(s)):
            if diff(answer[-1], s[i]) == 1:
                answer.append(s[i])
                s.pop(i)
                flag = True
                break
        for j in range(len(s)):
            if diff(answer[0], s[j]) == 1:
                answer.appendleft(s[j])
                s.pop(j)
                flag = True
                break
        

    len2 = len(answer)
    return(len1 == len2)



        