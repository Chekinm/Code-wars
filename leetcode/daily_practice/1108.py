class Solution:
    def defangIPaddr(self, address: str) -> str:
        a = list(address)
        res = []
        for char in a:
            if char == '.':
                res.append('[.]')
            else:
                res.append(char)
        return ''.join(res)
        