class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = {}

        for world in strs:
            tmp = [0] * 26
            for c in world:
                index = ord(c) - ord('a')
                tmp[index] +=1
            key = tuple(tmp)

            if key in store:
                store[key].append(world)
            else:
                store[key] = [world]
        
        output = list(store.values())

        return output
        