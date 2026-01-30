class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        left = 0
        right = len(nums1)

        while left <= right:
            part_a = (left + right) // 2
            part_b = (len(nums1) + len(nums2) + 1) // 2 - part_a

            a_left = float('-inf') if part_a - 1 < 0 else nums1[part_a - 1]
            a_right = float('inf') if part_a >= len(nums1) else nums1[part_a]
            b_left = float('-inf') if part_b - 1 < 0 else nums2[part_b - 1]
            b_right = float('inf') if part_b >= len(nums2) else nums2[part_b]

            if a_left <= b_right and b_left <= a_right:
                if (len(nums1) + len(nums2)) % 2 == 0:
                    return (max(a_left, b_left) + min(a_right, b_right)) / 2
                else:
                    return max(a_left, b_left)
            elif a_left > b_right:
                right = part_a - 1
            else:
                left = part_a + 1