class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        viewed_dict = {}
        for i in range(0, len(nums)):
            need = target - nums[i]
            if need in viewed_dict:
                if i < viewed_dict.get(need):
                    return [i, viewed_dict.get(need)]
                else:
                    return [viewed_dict.get(need), i]
            viewed_dict[nums[i]] = i
            i+=1


        