def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
    data = sorted(nums1 + nums2)
    n = len(data)

    if n % 2 != 0:
        return data[n // 2]
    else:
        a = data[n // 2 - 1] + data[n // 2]
        return a / 2
