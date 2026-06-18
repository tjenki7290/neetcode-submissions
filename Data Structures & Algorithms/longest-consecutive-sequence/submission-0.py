class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        num_set = set(nums)
        for n in nums:
            if (n-1) not in num_set:
                current = n
                length = 1
                while (current + 1) in num_set:
                    current += 1
                    length += 1
                if max_length < length:
                    max_length = length

        return max_length
                

