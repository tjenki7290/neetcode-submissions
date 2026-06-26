class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}

        #initialize countT map 
        for c in t:
            countT[c] = 1 + countT.get(c, 0) #use .get so if theres no value for c you can have a default value

        have, need = 0, len(countT)
        res, resLen = [-1,-1], float("infinity")
        l = 0

        for r in range(len(s)):
            c = s[r] #the character we just reached in the loop
            window[c] = 1 + window.get(c,0) #same reasoning as to why it was used earlier

            #checking to see if c is even in countT and that the current window satasfies that character in countT
            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                #update our result
                if (r-l + 1) < resLen: 
                    res = [l,r] #where the two pointers are actually located this is important, cause we will be outputting the substring not the length of substring
                    resLen = (r - l + 1) #length of the window
                #pop from the left of our window (also why we are looping)
                window[s[l]] -= 1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l+=1

        l, r =res

        return s[l:r +1] if resLen != float("infinity") else ""