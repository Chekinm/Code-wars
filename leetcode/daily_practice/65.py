from string import ascii_letters

class Solution:
    @staticmethod
    def check_num(num):
        try:
            float(num)
            return True
        except:
            return False
    @staticmethod  
    def check_num_int(num):
        try:
            int(num)
            return True
        except:
            return False

    

    def isNumber(self, s: str) -> bool:
        wrong_letter = set(ascii_letters)
        wrong_letter.remove('e')
        wrong_letter.remove('E')
        if not set(s).isdisjoint(wrong_letter):
            return False
        s = s.lower()
        spl = s.split('e')
        if len(spl) > 2:
            return False
        if len(spl) == 1:
            return self.check_num(spl[0])
        if len(spl) == 2:
            return all((self.check_num(spl[0]), self.check_num_int(spl[1])))
        
        