from collections import OrderedDict


def find_s(s):

    l=0
    cur_dict = {}
    max_len = 0
    max_str = slice(0,0)
    for i, char in enumerate(s):
        
        if char in cur_dict:
            if i - 1 - l > max_len:
                max_len = i - 1 - l
                max_str = slice(l, i)
            list_char = list(cur_dict.keys())
            k = 0
            while list_char[k] != char:
                cur_dict.pop(list_char[k])
                k += 1
            cur_dict.pop(list_char[k])
            l = l + k + 1
            cur_dict[char] = i
        else:
            cur_dict[char] = i
        print(cur_dict)
    return s[max_str], max_len

print(find_s('abcabafghbabaaabbabcda'))
