from collections import Counter


class Solution:
    def maxPalindromesAfterOperations(self, words: list[str]) -> int:
        
        c_total = Counter()
       
        for word in words:
            c = Counter(word)
            c_total.update(c)
        
        count_char_odd_total = 0
        count_char_even_total = 0

        for value in c_total.values():
            if value % 2:
                count_char_odd_total += 1
                count_char_even_total += value - 1
            else:
                count_char_even_total += value
        
        words.sort(key=len)
        res = 0
        for word in words:
            if len(word) % 2:
                if count_char_odd_total > 0:
                    count_char_odd_total -= 1
                    count_char_even_total -= (len(word) - 1)
                else:
                    count_char_even_total -= (len(word))

                if count_char_odd_total >= 0 and count_char_even_total >= 0:
                    res += 1
                
                print(word, count_char_odd_total, count_char_even_total, res)
                
            else:
                count_char_even_total -= (len(word))
                if count_char_even_total >= 0:
                    res += 1
                print(word, count_char_odd_total, count_char_even_total, res)
                    
        return res
        

 









s = Solution()

#print(s.maxPalindromesAfterOperations(["abbb","ba","aa"]))
print(s.maxPalindromesAfterOperations(["a","a","caa"]))



#print(s.maxPalindromesAfterOperations(["nulr","owdyq","ycjof","td","fzuz","avzi","pkmb","odpx","efcv","vx","qo","c"]))
#print(s.maxPalindromesAfterOperations(["cd","ef","a"]))