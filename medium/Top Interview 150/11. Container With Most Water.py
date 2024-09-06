def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    max_area = left = 0
    right = len(height) - 1
    while left < right:
        area = min(height[right], height[left]) * (right - left)
        max_area = max(max_area, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area

# print(maxArea([1,8,6,2,5,4,8,3,7]))
