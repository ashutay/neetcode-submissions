class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        valid_dict = {}

        for s_letter in s:
            if s_letter in valid_dict:
                valid_dict[s_letter]+=1
            else:
                valid_dict[s_letter] = 1

        for t_letter in t:
            if t_letter in valid_dict:
                valid_dict[t_letter]-=1
                if valid_dict[t_letter] == 0:
                    del valid_dict[t_letter]
            else:
                return False
        
        return len(valid_dict) == 0