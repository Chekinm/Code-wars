from collections import deque, Counter
from typing import List


class Solution:

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        count_dict = dict(Counter(words))
        control_deque = deque()
        left = 0
        len_word = len(words[0])
        len_words = len(words)
        result = []

        for start_ind in range(len_word):
            left = start_ind
            control_deque = deque()
            for i in range(start_ind, len(s), len_word):
                sub_word = s[i:i + len_word]  # get new word
                if sub_word not in words:  # if subwords
                    control_deque = deque()
                    left = i + len_word
                    continue
                if (sub_word in control_deque and
                   control_deque.count(sub_word) == count_dict[sub_word]):
                    while control_deque[0] != sub_word:
                        control_deque.popleft()
                        left += len_word
                    else:
                        control_deque.popleft()
                        control_deque.append(sub_word)
                        left += len_word
                else:
                    control_deque.append(sub_word)

                if len(control_deque) == len_words:
                    result.append(left)

        return result
