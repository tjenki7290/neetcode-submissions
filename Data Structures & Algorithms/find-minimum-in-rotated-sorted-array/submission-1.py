class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums) - 1
        while L < R:
            mid = (L+R)//2 #gives the average of the two endpoints then rounds down
            if nums[mid] > nums[R]:
                L = mid + 1
            else:
                R = mid
        return nums[L]