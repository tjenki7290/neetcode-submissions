class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums)- 1
        while L <= R:
            mid = (L+R)//2
            if target == nums[mid]:
                return mid

            #if this confitional passes then the left sorted portion doesnt contain break
            if nums[L] <= nums[mid]:
                #check to see if the target is NOT in the left sorted portion
                if target > nums[mid] or target < nums[L]:
                    L = mid + 1
                else: #target is in the left sorted portion
                    R = mid - 1

            #else the right sorted portion doesnt contain the break
            else:
                if target < nums[mid] or target > nums[R]:#check to see if target is NOT in the right sorted portion
                    R = mid - 1
                else:
                    L = mid + 1
        return -1