class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)

        for inx in range(1, len(nums)):
            left[inx] = left[inx - 1] * nums[inx - 1]

        right = [1] * len(nums)
        for inx in range(len(nums) -2, -1, -1):
            right[inx] = right[inx + 1] * nums[inx + 1]
            
        result = []
        for inx in range(len(nums)):
            result.append(left[inx] * right[inx])
        
        return result