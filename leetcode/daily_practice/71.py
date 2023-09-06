class Solution:
    def simplifyPath(self, path: str) -> str:
        path += '/'
        current_word_list = []
        path_list = []
        current_word = ''
        right = 1
        while right < len(path):
            if path[right] == '/':
                if len(current_word_list):
                    current_word = ''.join(current_word_list)
                    current_word_list = []
                    if current_word == '..':
                        if len(path_list) != 0:
                            path_list.pop()
                    elif current_word != '.':
                        path_list.append(current_word)
            else:
                current_word_list.append(path[right])
            right += 1

        res = '/' + '/'.join(path_list) 

        return res
