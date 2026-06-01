class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(0, len(nums)):
            need = target - nums[i]
            if need in nums:
                for j in range(i+1, len(nums)):
                    if need == nums[j]:
                        return [i,j]
                    j+=1
            i+=1


        