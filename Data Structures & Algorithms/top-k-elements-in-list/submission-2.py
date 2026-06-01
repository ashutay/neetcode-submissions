class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent_dict = {}

        for num in nums:
            frequent_dict[num] = frequent_dict.get(num, 0) + 1
        
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, frequent in frequent_dict.items():
            bucket[frequent].append(num)
        
        answer = []
        for frequents in reversed(bucket):
            for num in frequents:
                answer.append(num)
                if len(answer) == k:
                    return answer