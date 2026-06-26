class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L, R = 0, 0
        window_set = set()#is going to be the same size as the window
        max_len = 0
        while R < len(s):
            while s[R] in window_set: #handles our duplicate problem
                window_set.remove(s[L]) #pretty much going to remove the items from the set until there are no longer any dupliates (this could take one iteration or it could make our set start back at 1)
                L += 1
            window_set.add(s[R]) #if not a duplicate add value at R
            max_len = max(max_len, len(window_set))
            R += 1
        return max_len

