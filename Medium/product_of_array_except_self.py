"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:

    2 <= nums.length <= 105
    -30 <= nums[i] <= 30
    The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""

# Needed guidance, write out steps to solve problem to get a better understanding of how to structure solutions
class mySolution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1 for _ in nums]
        answer = [1 for _ in nums]
        i = 1
        
        while i < len(nums):
            prefix.append(nums[i-1] * prefix[i-1])
            i += 1
        
        i -= 2

        while i >= 0:
            suffix[i] = nums[i+1] * suffix[i+1]
            i -= 1
        
        i = 0

        while i < len(nums):
            answer[i] = prefix[i] * suffix[i]
            i += 1

        return answer

# Came to this from the prompt suggestion. Use ans list to store suffixes, input to store prefixes, then combine into ans
class constantSpaceSolution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1 for _ in nums]

        i = len(nums) - 2
        while i >= 0:
            answer[i] = nums[i+1] * answer[i+1]
            i -= 1

        tmp = nums[0]
        nums[0] = 1
        i = 1
        while i < len(nums):
            new_val = tmp * nums[i-1]
            tmp = nums[i]
            nums[i] = new_val
            i += 1
        
        i = 0
        while i < len(nums):
            answer[i] = nums[i] * answer[i]
            i += 1

        return answer

# A faster implimentation of my constant approach
class optimalSolution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # The length of the input array
        length = len(nums)

        # The answer array to be returned
        answer = [0] * length

        # answer[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the answer[0] would be 1
        answer[0] = 1
        for i in range(1, length):

            # answer[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all
            # elements to the left of index 'i'
            answer[i] = nums[i - 1] * answer[i - 1]

        # R contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R would be 1
        R = 1
        for i in reversed(range(length)):

            # For the index 'i', R would contain the
            # product of all elements to the right. We update R accordingly
            answer[i] = answer[i] * R
            R *= nums[i]

        return answer