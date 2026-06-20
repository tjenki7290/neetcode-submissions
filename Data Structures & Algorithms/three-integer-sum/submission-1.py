class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort the list 
        nums.sort()
        
        #store the length so you don't recompute it
        n = len(nums)

        #init an empty answer array
        answer = []

        for i in range(n):
            #we are going to do some prereq checks that would automatically break the loop
            if nums[i] > 0:
                break #breaks the loop and will casue the return answers to run
            elif i > 0 and nums[i] == nums[i-1]: #skips duplicates, basically saying that if the the next value = the previous value, you've already found all triplets for that number
                continue #continue just moves on from this duplicate
            
            lo = i + 1
            hi = n - 1

            while lo < hi: #keep looping until the pointers meet
                summ = nums[i] + nums[lo] + nums[hi]
                if summ == 0:
                    answer.append([nums[i], nums[lo], nums[hi]]) #found an answer so add it to the list
                    lo, hi = lo + 1, hi - 1 #keep moving both pointers inward, towards eachother
                    
                    while lo < hi and nums[lo] == nums[lo - 1]:#comparing current index to previous index to see if duplicat , list is sorted so this works
                        lo += 1 #skip that index because its a duplicate

                    while lo < hi and nums[hi] == nums[hi + 1]:
                        hi -= 1 #skip that index because its a duplicate
                elif summ < 0:
                    lo += 1 #sum is too small move lo to right
                else:
                    hi -= 1 #sum is too big move high to left

        return answer
            