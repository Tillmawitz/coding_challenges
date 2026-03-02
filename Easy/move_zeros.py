"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:

Input: nums = [0]
Output: [0]

Constraints:

    1 <= nums.length <= 104
    -231 <= nums[i] <= 231 - 1
 
Follow up: Could you minimize the total number of operations done?
"""

# This was the optimal solution, optimal was only provided in c++. I think the solutions are compared cross-language, as my solution only beat 22% of solutions in terms of memory.
class mySolution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = last_zero = 0

        while i < len(nums):
            if nums[last_zero] != 0 and nums[i] == 0:
                last_zero = i
                continue

            if nums[i] != 0 and nums[last_zero] == 0:
                nums[last_zero] = nums[i]
                nums[i] = 0
                last_zero += 1
            i += 1

