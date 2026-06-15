class Solution:
    def hasDuplicate(self, nums):
        seen = set()

        for n in nums:
            seen.add(n)

        if len(seen) != len(nums):
            return True
        else:
            return False