"""
You are given an integer array nums and an integer k.

An array is considered balanced if the value of its maximum element is at most k times the minimum element.

You may remove any number of elements from nums​​​​​​​ without making it empty.

Return the minimum number of elements to remove so that the remaining array is balanced.

Note: An array of size 1 is considered balanced as its maximum and minimum are equal, and the condition always holds true.

Example 1:

Input: nums = [2,1,5], k = 2

Output: 1

Explanation:

    Remove nums[2] = 5 to get nums = [2, 1].
    Now max = 2, min = 1 and max <= min * k as 2 <= 1 * 2. Thus, the answer is 1.

Example 2:

Input: nums = [1,6,2,9], k = 3

Output: 2

Explanation:

    Remove nums[0] = 1 and nums[3] = 9 to get nums = [6, 2].
    Now max = 6, min = 2 and max <= min * k as 6 <= 2 * 3. Thus, the answer is 2.

Example 3:

Input: nums = [4,6], k = 2

Output: 0

Explanation:

    Since nums is already balanced as 6 <= 4 * 2, no elements need to be removed.

Constraints:

    1 <= nums.length <= 105
    1 <= nums[i] <= 109
    1 <= k <= 105
"""

# Fails for [5, 11, 20] and k=2
class medianSolution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        
        counter = 0
        # Sort
        nums.sort()
        # Set pointers to beginning and end
        left = 0
        right = len(nums) - 1
        # Loop while beginning < end
        while left < right:
            # Check if max <= min * k
            if nums[right] <= nums[left] * k:
                break
            # If not
            # Find median
            # Because of indexing, this means our list is odd length
            if (right - left) % 2 == 0:
                median_ind = (right - left) // 2 + left
                median = nums[median_ind]
            else:
                median_left = (right - left) // 2 + left
                median = (nums[median_left] + nums[median_left + 1]) / 2
            # Determine if min or max is further from median
            max_dist = abs(nums[right] - median)
            min_dist = abs(median - nums[left])
            # Move furthest one in and increment counter
            if max_dist > min_dist:
                right -= 1
            else:
                left += 1
            
            counter += 1
        
        return counter

# Fails for [8,99,65,16,39] k=3
class next_hopSolution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        
        counter = 0
        # Sort
        nums.sort()
        # Set pointers to beginning and end
        left = 0
        right = len(nums) - 1
        # Loop while beginning < end
        while left < right:
            # Check if max <= min * k
            if nums[right] <= nums[left] * k:
                break
            # If not
            # Find median
            # Because of indexing, this means our list is odd length
            next_left_dis = nums[right] - nums[left + 1] * k
            next_right_dis = nums[right - 1] - nums[left] * k

            if next_left_dis <= 0 or next_right_dis <= 0:
                counter += 1 
                break
            elif next_left_dis >= next_right_dis:
                right -= 1
            else:
                left += 1
            
            counter += 1

# Sliding window, by never decreasing the right we are always working with the largest window that includes the left index
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()

        ans = n
        right = 0
        for left in range(n):
            while right < n and nums[right] <= nums[left] * k:
                right += 1
            ans = min(ans, n - (right - left))

        return ans
        
        return counter