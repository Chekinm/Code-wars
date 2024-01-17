import itertools as it


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        map_dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        return list(''.join(i) 
                    for i in it.product(
                        *[map_dict[dig] for dig in digits]
                        )) if len(digits) > 0 else []
