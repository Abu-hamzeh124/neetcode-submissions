class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxi = 0
        i, j = 0, len(heights) - 1
        while i < j:
            width = j - i
            height = min(heights[i], heights[j])
            area = width * height
            if area > maxi:
                maxi = area
            elif height == heights[i]:
                i += 1
            else:
                j -= 1
               
        return maxi
