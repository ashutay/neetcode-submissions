class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ''

        for world in strs:
            output += f"{len(world)}#{world}"
        
        return output

    def decode(self, s: str) -> List[str]:
        output = []

        size = len(s)
        if size == False:
            return output

        cur = 0;

        wolrd_len = ''
        while (True):
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

            if cur == size:
                break
        
        return output

            

            

