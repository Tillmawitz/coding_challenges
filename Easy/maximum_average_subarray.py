"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:

Input: nums = [5], k = 1
Output: 5.00000

Constraints:

    n == nums.length
    1 <= k <= n <= 10^5
    -10^4 <= nums[i] <= 10^4
"""

# Too slow because we are constantly recalculating the sum
class tooSlowSolution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = float('-inf')
        start = 0
        end = k - 1

        while end < len(nums):
            working_avg = sum(nums[start:end + 1]) / k
            max_avg = max(max_avg, working_avg)
            start += 1
            end += 1

        return max_avg

# Similar window idea to before, but instead of recalculating whole sum we shift the window and subtract the beginning number and add the next one to the window sum. This is an optimal solution.
class betterSolution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = float('-inf')
        start = 0
        end = 0
        window_sum = 0

        while end < len(nums):
            if end - start + 1 < k:
                window_sum += nums[end]
                end += 1
            else:
                window_sum += nums[end]
                max_avg = max(max_avg, window_sum / k)
                window_sum -= nums[start]
                start += 1
                end += 1


        return max_avg