class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):  
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m
        half_len = (m + n + 1) // 2  

        while left <= right:
            mid1 = (left + right) // 2
            mid2 = half_len - mid1

            maxLeft1 = nums1[mid1 - 1] if mid1 > 0 else float('-inf')
            minRight1 = nums1[mid1] if mid1 < m else float('inf')
            maxLeft2 = nums2[mid2 - 1] if mid2 > 0 else float('-inf')
            minRight2 = nums2[mid2] if mid2 < n else float('inf')

            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                if (m + n) % 2 == 0:  
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
                else: 
                    return max(maxLeft1, maxLeft2)
            elif maxLeft1 > minRight2: 
                right = mid1 - 1
            else: 
                left = mid1 + 1