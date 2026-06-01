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
        wolrd_len = ''

        while (cur < size):
            while(s[cur] != '#'):
                wolrd_len += s[cur]
                cur += 1
            
            if s[cur] == '#':
                cur += 1
            
            world = ''
            for i in range(int(wolrd_len)):
                world += s[cur]
                cur += 1
            
            wolrd_len = ''
            output.append(world)
        
        return output

            

            

