class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []

        for world in strs:
            parts.append(f"{len(world)}#{world}")
        
        return '' . join(parts)

    def decode(self, s: str) -> List[str]:
        output = []

        size = len(s)
        cur = 0;
        word_len = ''

        while (cur < size):
            while(s[cur] != '#'):
                word_len += s[cur]
                cur += 1
            
            if s[cur] == '#':
                cur += 1
            
            word = s[cur:cur + int(word_len)]
            output.append(word)

            cur += int(word_len)
            word_len = ''
        
        return output

            

            

