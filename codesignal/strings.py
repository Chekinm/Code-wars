from itertools import permutations
from collections import deque
from random import shuffle
arr = []
a = ['a']*400
for i in range(400):
    a[i] = 'b'
    arr.append(''.join(a))

shuffle(arr)
print('ready')
arr = ["abc", 
 "bef", 
 "bcc", 
 "bec", 
 "bbc", 
 "bdc"]


def diff (str1, str2):
    n = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            n += 1
    return n
# def solution(s):
#     # i need to compare two strings and found how many characters is a difference
#     def diff (str1, str2):
#         n = 0
#         for i in range(len(str1)):
#             if str1[i] != str2[i]:
#                 n += 1
#         return n

#     perms = permutations(s, len(s))
    
#     for var in perms:
#         flag = True
#         for i in range(len(s) - 1):
#             if diff(var[i], var[i+1]) != 1:
#                 flag = False
        
#         if flag ==True:
#             return True
#     return False
        

def get_string(arr):
    len1 = len(arr)
    answer = deque()
    answer.append(arr[5])
    arr.pop(5)
    flag = True
    while len(arr) and flag:
        flag = False
        for i in range(len(arr)):
            if diff(answer[-1], arr[i]) == 1:
                answer.append(arr[i])
                arr.pop(i)
                flag = True
                break
        for j in range(len(arr)):
            if diff(answer[0], arr[j]) == 1:
                answer.appendleft(arr[j])
                arr.pop(j)
                flag = True
                break
        

    len2 = len(answer)
    return(answer, arr, len1 == len2)

print(get_string(arr))




        

