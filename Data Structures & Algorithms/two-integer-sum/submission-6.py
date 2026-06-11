class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for i, n in enumerate(nums):
            complement = target - n
            if complement in seen:
                if i < seen[complement]:
                    return [i, seen[complement]]
                else:
                    return [seen[complement], i]
            seen[n] = i