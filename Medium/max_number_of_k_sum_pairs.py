"""
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.

Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.

Constraints:

    1 <= nums.length <= 105
    1 <= nums[i] <= 109
    1 <= k <= 109
"""

from collections import defaultdict

# We are counting pairs of compliments, we can traverse the list once by storing the number of times a number has occured in the list without it's compliment occuring, when it's compliment has already occured we increment our count. This is an optimal solution for time with O(n) but also uses O(n) space
class mySolution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        compliments = defaultdict(int)
        count = 0

        for num in nums:
            compliment = k - num
            if compliment in compliments and compliments[compliment] > 0:
                count += 1
                compliments[compliment] -= 1
            else:
                compliments[num] += 1

        return count

# Sorting lists in python uses constant space so time is O(nlogn) but space is O(n). By sorting we know the order, if the nums sum to k move both pointers, if sum is less than k we need a bigger number so move left pointer and vice versa for sums larger than k.
class spaceOptimalSolution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = count = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] + nums[right] == k:
                count += 1
                left += 1
                right -= 1
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                right -= 1
        
        return count