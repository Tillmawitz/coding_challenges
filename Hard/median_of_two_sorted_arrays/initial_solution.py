class Solution:
    def median_of_list(self, nums: List[int], length: int) -> float:
        if length % 2 == 0:
            return (nums[length // 2] + nums[length // 2 - 1]) / 2
        else:
            return nums[length // 2]

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        if m == 0:
            return self.median_of_list(nums2, n)
        elif n == 0:
            return self.median_of_list(nums1, m)

        total_length = m + n
        is_even = True if total_length % 2 == 0 else False
        i = 0
        median = 0

        if is_even:
            while i <= total_length // 2 - 1:
                if m == 0:
                    median = nums2.pop(0)
                    n -= 1
                elif n == 0:
                    median = nums1.pop(0)
                    m -= 1
                elif nums1[0] > nums2[0]:
                    median = nums2.pop(0)
                    n -= 1
                else:
                    median = nums1.pop(0)
                    m -= 1
                
                i += 1

            if m == 0:
                return (median + nums2[0]) / 2
            elif n == 0:
                return (median + nums1[0]) / 2
            else:
                return (median + min(nums1[0], nums2[0])) / 2 
        else:
            while i <= total_length // 2:
                if m == 0:
                    median = nums2.pop(0)
                    n -= 1
                elif n == 0:
                    median = nums1.pop(0)
                    m -= 1
                elif nums1[0] > nums2[0]:
                    median = nums2.pop(0)
                    n -= 1
                else:
                    median = nums1.pop(0)
                    m -= 1
                
                i += 1

            return median
        