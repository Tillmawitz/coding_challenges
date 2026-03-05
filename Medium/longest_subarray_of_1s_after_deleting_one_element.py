"""
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.

Constraints:

    1 <= nums.length <= 105
    nums[i] is either 0 or 1.
"""

# This is an optimal solution, uses sliding window
class mySolution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = right = 0
        last_deletion = float('-inf')
        longest_subarray = 0

        while right < len(nums):
            if nums[right] == 0 and last_deletion >= 0:
                # roll up accordian
                longest_subarray = max(longest_subarray, right - left - 1)
                left = last_deletion + 1
                last_deletion = right
            elif nums[right] == 0:
                last_deletion = right
            
            right += 1
        
        return max(longest_subarray, right - left - 1)