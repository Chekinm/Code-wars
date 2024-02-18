class TrieObj:

    def __init__(self, letter):
        self.value = letter
        self.childs = {}
        self.has_elem = False


class Trie:

    def __init__(self):
        self.head = TrieObj(None)

    def insert(self, word):
        curr_node = self.head
        for letter in word:
            if letter in curr_node.childs:
                curr_node = curr_node.childs[letter]
            else:
                curr_node.childs[letter] = TrieObj(letter)
                curr_node = curr_node.childs[letter]
        curr_node.has_elem = True

    def search(self, word):
        curr_node = self.head
        for letter in word:
            if letter in curr_node.childs:
                curr_node = curr_node.childs[letter]
            else:
                return False
        if curr_node.has_elem:
            return True
        return False

    def startsWith(self, startsWith):
        curr_node = self.head
        for letter in startsWith:
            if letter in curr_node.childs:
                curr_node = curr_node.childs[letter]
            else:
                return False
        return True


    def lenght_of_prefix(self, word):
        curr_node = self.head
        count = 0
        for letter in word:
            if letter in curr_node.childs:
                count += 1
                curr_node = curr_node.childs[letter]
            else:
                break 
        return count




class Solution:

    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        t = Trie()
        for num in arr1:
            s_num = str(num)
            t.insert(s_num)
        print(t)
        longest = 0
        for num in arr2:
            s_num = str(num)
            curr = t.lenght_of_prefix(s_num)
            print(s_num, curr)
            longest = max(curr, longest)


s = Solution()


s.longestCommonPrefix(arr1 = [1,10,100,2,3,23,23333333334], arr2 = [2, 23, 1000])

