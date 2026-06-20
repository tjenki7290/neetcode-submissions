class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        R = len(s) - 1
        L = 0
        
        while L < R:
            #if either values at lindices L, R don't contain .isalnum() values then you just increment them by 1 in their respective direction
            if not s[L].isalnum():
                L += 1
                continue
            
            if not s[R].isalnum():
                R -= 1
                continue

            #now that we know they're both at numeric values check to see that the values are the same if not, return False
            if s[L] != s[R]:
                return False
            
            L += 1
            R -= 1

        return True