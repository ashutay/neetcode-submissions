class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []

        for world in strs:
            parts.append(f"{len(world)}#{world}")
        
        return '' . join(parts)

    def decode(self, s: str) -> List[str]:
        output = []
        cur = 0;
       
        while cur < len(s):
            separator_indx = cur

            while s[separator_indx] != '#':
                separator_indx += 1
            
            word_len = int(s[cur:separator_indx])
            
            word = s[separator_indx + 1 : separator_indx + 1 + word_len]
            output.append(word)

            cur = separator_indx + 1 + word_len
        
        return output

            

            

