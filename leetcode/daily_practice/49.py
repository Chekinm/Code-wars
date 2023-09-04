# it is in leetcode format with class solution

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        word_dict = {}

        for word in strs:
            word_key = ''.join(sorted(list(word)))
            if word_key in word_dict:
                word_dict[word_key].append(word)
            else:
                word_dict[word_key] = [word]
        
        return word_dict.values()