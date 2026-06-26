class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longest = 0
        counts = [0] * 26

        for r in range(len(s)):
            counts[ord(s[r]) - 65] += 1
            #now we need to do our check to see if a window is invalid 
            while (r-l +1) - max(counts) > k: #while the number of elements needing to be changed is larger than k(number of elements that can be changed)
                #remove the value at counts[ord(s[l])] position
                counts[ord(s[l]) - 65] -= 1
                #increment l by 1 to move the window
                l += 1

            #valid window
            longest = max(longest, (r - l + 1))

        return longest