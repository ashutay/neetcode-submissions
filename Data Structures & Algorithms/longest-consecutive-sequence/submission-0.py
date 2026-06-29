class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        has_map = set()
        max_seq = 0
        local_max = 0

        for num in nums:
            if num - 1 in nums:
                continue

            has_map.add(num)
            local_max = 1

            need_num = num + 1
            while True:

                if need_num in nums:
                    has_map.add(need_num)
                    local_max = local_max + 1
                    need_num = need_num + 1
                else:
                    if local_max > max_seq:
                        max_seq = local_max
                    local_max = 0
                    break

        return max_seq