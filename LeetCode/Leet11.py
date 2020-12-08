class Solution(object):
    def maxArea(self, height: List[int]) -> int:
        area = 0
        i1 = 0
        i2 = len(height) - 1
        while i1 < i2:
            h = min(height[i1], height[i2])
            area = max(area, h * (i2 - i1))
            if height[i1] < height[i2]:
                i1 += 1
            else:
                i2 -= 1
        return area
