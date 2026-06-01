class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent_dict = {}

        for num in nums:
            if num in frequent_dict:
                frequent_dict[num] += 1
            else:
                frequent_dict[num] = 1
        
        busket = [[] for _ in range(len(nums) + 1)]
        for num, frequent in frequent_dict.items():
            busket[frequent].append(num)
        
        answer = []
        for frequents in reversed(busket):
            for num in frequents:
                answer.append(num)
                if len(answer) == k:
                    return answer