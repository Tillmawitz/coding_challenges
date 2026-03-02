"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Constraints:

    1 <= nums.length <= 105
    nums[i] is either 0 or 1.
    0 <= k <= nums.length
"""

# Sliding window problem, except now we are tracking the window size and sliding when we encounter a 0 after hitting our "flip max" (k). When hitting a 0 after the flip max, we slide up the start to just past the last 0 encountered.
class mySolution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = end = 0
        count = 0
        largest_sub = 0
        
        while end < len(nums):
            if nums[end] == 1 or count < k:
                largest_sub = max(largest_sub, end - start + 1)
                if nums[end] == 0:
                    count += 1
                end += 1
            else:
                while nums[start] != 0:
                    start += 1
                start += 1
                largest_sub = max(largest_sub, end - start + 1)
                end += 1
        
        return largest_sub

# A cleaner version, I need to get better at my choice of conditions and viewing problems atomically
class betterSolution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        curr = 0
        ans = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                curr += 1

            while curr > k:
                if nums[left] == 0:
                    curr -= 1
                left += 1
            
            ans = max(ans, right - left + 1)

        return ans