class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        viewed_dict = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in viewed_dict:
                return [viewed_dict[need], i]
            viewed_dict[num] = i