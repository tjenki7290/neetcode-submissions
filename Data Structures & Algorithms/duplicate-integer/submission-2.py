class Solution: 
    def hasDuplicate(self, nums):
        seen = set()#this set allows us to store unique values
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False