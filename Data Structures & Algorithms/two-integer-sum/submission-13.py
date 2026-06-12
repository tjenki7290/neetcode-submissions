class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {} #we want to create a hashmap to store past numbers we've looped over

        for i, n in enumerate(nums): #enumerate allows me to query by both the index and the value
            complement = target - n

            if complement in seen: #if the complement is found in the hashmap return the 
            #current indices of both the value the loop is currently on, and the 
            #index of the complement
                return [seen[complement], i]
            seen[n] = i
            
               

