class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) #mapping the charCount of each string to list of Anagrams

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
                
            key = tuple(count)
            result[key].append(s)

        return list(result.values())