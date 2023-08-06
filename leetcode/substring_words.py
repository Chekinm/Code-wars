class Solution:
    from collections import Counter, deque
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        result = []

        count_dict = dict(Counter(words))
        len_word = len(words[0])
        len_words = len(words)
        len_sub = len_word * len_words
        
        def sub_string_is_valid(sub_string):
            
            local_count_dict = count_dict.copy()
            for i in range(0, len(sub_string), len_word):
                word = sub_string[i:i+len_word]
                
                if word not in local_count_dict:
                    return False
                else:
                    local_count_dict[word] -= 1
                    if local_count_dict[word] == 0:
                        del local_count_dict[word]
                    
            return True      
        
        for i in range(len(s) - len_sub + 1):
            sub_str = s[i:i + len_sub]
            if sub_string_is_valid(sub_str):
                result.append(i)

        return result