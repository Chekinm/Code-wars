class TrieObj:

    def __init__(self, letter):
        self.value = letter
        self.childs = {}
        self.count_word = 0
        


class Trie:

    def __init__(self):
        self.head = TrieObj(None)
        self.total = 0

    def insert(self, word):
        curr_node = self.head
        for i in range(len(word)):
            pair = word[i] + word[len(word)-i-1]
            if pair in curr_node.childs:
                curr_node = curr_node.childs[pair]
                if curr_node.count_word:
                    self.total += curr_node.count_word
            else:
                curr_node.childs[pair] = TrieObj(pair)
                curr_node = curr_node.childs[pair]
        curr_node.count_word += 1




class Solution:
    def countPrefixSuffixPairs(self, words: list[str]) -> int:

        
        pref = Trie()
        
        for word in words:
            pref.insert(word)

        return pref.total
            
s = Solution()

# s1 = ["abab","ab"]
# s2 = ["a","aa","aa","b","ab"]
# s1 = ["b","ba","b","bb","b","ab"]
# a = s.countPrefixSuffixPairs(s1)

a = s.countPrefixSuffixPairs(["aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa","aaaaa"])
print(a)