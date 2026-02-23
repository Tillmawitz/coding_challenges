"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

Constraints:

    1 <= flowerbed.length <= 2 * 104
    flowerbed[i] is 0 or 1.
    There are no two adjacent flowers in flowerbed.
    0 <= n <= flowerbed.length
"""

class initialSolution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        max_additional = 0
        flower_len = len(flowerbed)

        # Base cases
        if flower_len == 0 or n > flower_len:
            return False
        elif flower_len == 1:
            return (flowerbed[0] == 0 and n == 1) or n == 0
        elif flower_len == 2:
            valid_spot = flowerbed[0] == 0 and flowerbed[1] == 0
            return (valid_spot and n <= 1) or n == 0

        valid_section = 0
        i = 0
        while i < flower_len:
            beginning = (i == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0)
            end = (i == flower_len - 1 and flowerbed[i] == 0 and flowerbed[i-1] == 0)
            current_valid = False

            if i > 0 and i < flower_len - 1:
                current_valid = (flowerbed[i] == 0 and flowerbed[i + 1] == 0 and flowerbed[i - 1] == 0)

            if beginning or end or current_valid:
                valid_section += 1
            elif valid_section > 0:
                max_additional += (valid_section // 2) + (valid_section % 2)
                valid_section = 0

            i += 1

        if valid_section > 0:
            max_additional += (valid_section // 2) + (valid_section % 2)

        return max_additional >= n

# It looks as though we are to assume that adding a flower does not invalidate further spots? Odd situation.
# Logical statements are simpler than mine
class optimalSolution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            # Check if the current plot is empty.
            if flowerbed[i] == 0:
                # Check if the left and right plots are empty.
                empty_left_plot = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right_lot = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                
                # If both plots are empty, we can plant a flower here.
                if empty_left_plot and empty_right_lot:
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        return True
                    
        return count >= n

        