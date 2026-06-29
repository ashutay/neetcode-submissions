class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        max_seq = 0
        
        for num in hash_set:
            if num - 1 in hash_set:
                continue

            current_length = 1

            need_num = num + 1
            while need_num in hash_set:
                current_length += 1
                need_num = need_num + 1

            max_seq = max(max_seq, current_length)

        return max_seq