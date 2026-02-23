# Too slow for large cases, scales very poorly
class intialSolution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        i = 0
        while i < len(nums) - 1: 
            j = len(nums) - 1
            while j > i:
                if nums[i] < nums[j]:
                    k = i + 1
                    while k < j:
                        if nums[i] < nums[k] and nums[k] < nums[j]:
                            return True
                        k += 1
                j -= 1
            i += 1
        
        return False

# A more efficient solution in terms of time complexity, relying on comparing the value at a given position to the min of the values to the left and max of the values to the right. A dictionary is used to keep track of the number of times a value is present in the right half so that maxRight can be recalculated when the max is removed. Only beat 5% of solutions, still very slow.
from collections import defaultdict

class nextSolution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        numsRight = defaultdict(int)
        i = 2
        while i < len(nums):
            numsRight[nums[i]] += 1
            i += 1
        
        minLeft = nums[0]
        maxRight = max(nums[2:])
        i = 1

        while i < len(nums) - 1:
            num = nums[i] 
            if nums[i] < maxRight and nums[i] > minLeft:
                return True
            
            if nums[i] < minLeft:
                minLeft = nums[i]
            
            numsRight[nums[i+1]] -= 1
            if numsRight[nums[i+1]] <= 0 and nums[i+1] >= maxRight and i < len(nums) - 2:
                maxRight = max(nums[i+2:])
            
            i += 1
        
        return False

# Way overthought the problem. There are 3 possible states for any value, either it is less than the smallest, bigger than the smallest but smaller than the second smallest, or bigger than both. We don't need to worry about the order because of how our update logic is structured. We know there is a value smaller than second_num to the left of it regardless of the current value of first_num, and if a number is bigger than both we have a triplet.
class optimalSolution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_num = float("inf")
        second_num = float("inf")
        for n in nums:
            if n <= first_num:
                first_num = n
            elif n <= second_num:
                second_num = n
            else:
                return True
        return False