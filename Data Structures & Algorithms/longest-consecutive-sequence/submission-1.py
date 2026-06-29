class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        max_seq = 0
        local_max = 0

        for num in hash_set:
            if num - 1 in hash_set:
                continue

            local_max = 1

            need_num = num + 1
            while True:

                if need_num in hash_set:
                    local_max = local_max + 1
                    need_num = need_num + 1
                else:
                    max_seq = max(max_seq, local_max)
                    break

        return max_seq