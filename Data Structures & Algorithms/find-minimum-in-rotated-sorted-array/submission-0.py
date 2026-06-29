class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) - 1
        while L < R:
            #claculate mid and then check to see where mid lands out of the variables
            mid = (L + R)//2
            if nums[mid] > nums[R]:
                L = mid + 1
            else:
                R = mid
        return nums[L]
       