class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #build the count dict, key is integer, value is frequency
        count = defaultdict(int)

        for i in nums: 
            count[i] += 1

        #this is going to be the key,value pairs, 
        pairs = [(count[n], n) for n in count] #I made the first element the frequency, hence the count[n]
        pairs.sort(reverse = True) #sorts by first element, which is why i created the pairs with frequency as first element. flips the sort to largest - smallest

        result = [pair[1] for pair in pairs[:k]]#basically saying pull out the number(stored at index 1), for the first k pairs

        return list(result)#for some reason saves .2mb of memory wrapping it in a list
