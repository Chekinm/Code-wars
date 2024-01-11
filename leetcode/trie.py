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
