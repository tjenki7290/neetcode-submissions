class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #create two pointers 
        L = 0 
        R = len(heights) - 1
        #create a place to store the max value
        max_area = 0
        #create width and height variables
        width = 0
        height = 0
        while L < R:
            #calculate the max area 
            temp_area = 0
            width = R - L
            if heights[L] < heights[R]:
                height = heights[L]
            if heights[R] < heights[L]:
                height = heights[R] 
            if heights[L] == heights[R]:
                height = heights[L]
            temp_area = height * width
            #see if new area is bigger then previous area 
            if temp_area > max_area:
                max_area = temp_area
            
            #see which of the two pointers(L and R) have a smaller height and move that pointer inwards
            if heights[L] < heights[R]:
                L += 1
                continue
            if heights[R] < heights[L]:
                R -= 1
                continue
            if heights[R] == heights[L]:
                R -= 1
        return max_area