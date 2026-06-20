class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        for c in s:
            #going to check to see if the current char is in pairs, if it is it means it is a closing bracket, since we are mapping key:close to value:open
            if c in pairs: #-1 index in a stack shows the last element added
                if stack and stack[-1] == pairs[c]:
                    stack.pop()#pop off the top element since it found a valid pair
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

