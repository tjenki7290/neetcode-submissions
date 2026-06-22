class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        #create our two pointers 
        L = 0
        R = len(s) - 1

        while L < R:
            if not s[L].isalnum():
                L += 1
                continue
            if not s[R].isalnum():
                R -= 1
                continue
            
            if s[L] != s[R]:
                return False
            else:
                L += 1
                R -= 1

        return True

                
