class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        for s_letter in s:
            if s_letter in s_dict:
                s_dict[s_letter]+=1
            else:
                s_dict[s_letter] = 1

        for t_letter in t:
            if t_letter in t_dict:
                t_dict[t_letter]+=1
            else:
                t_dict[t_letter]=1

        return s_dict == t_dict