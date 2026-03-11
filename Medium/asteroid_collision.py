"""
We are given an array asteroids of integers representing asteroids in a row. The indices of the asteroid in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.

Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

Example 4:

Input: asteroids = [3,5,-6,2,-1,4]​​​​​​​
Output: [-6,2,4]
Explanation: The asteroid -6 makes the asteroid 3 and 5 explode, and then continues going left. On the other side, the asteroid 2 makes the asteroid -1 explode and then continues going right, without reaching asteroid 4.

Constraints:

    2 <= asteroids.length <= 104
    -1000 <= asteroids[i] <= 1000
    asteroids[i] != 0
"""

# Struggled with this one a lot, the idea is to use a stack and continuously pop elements when a collision occurs until it the cascade is resolved. The conditionals and branching logic took many attempts to work out and produced some confusing and slightly repetitive code.
class mySolution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for cur_rock in asteroids:
            if len(stack) == 0:
                stack.append(cur_rock)
                continue
            
            last_rock = stack.pop()
            
            if last_rock > 0 and cur_rock < 0:
                # collision, get absolute value of rocks
                while last_rock > 0 and cur_rock < 0:
                    abs_last, abs_cur = abs(last_rock), abs(cur_rock)
                    if abs_last == abs_cur:
                        # Both rocks destroyed, continue to next
                        break
                    elif abs_last > abs_cur:
                        # Current rock destroyed, add last one back and continue
                        stack.append(last_rock)
                        break
                    else:
                        # Go back through the stack until current destroyed or stack is empty
                        if len(stack) == 0:
                            stack.append(cur_rock)
                            break
                        else:
                            last_rock = stack.pop()
                            # No longer colliding, add both back
                            if last_rock < 0:
                                stack.append(last_rock)
                                stack.append(cur_rock)
            else:
                # No collision, put both rocks in the stack and continue
                stack.append(last_rock)
                stack.append(cur_rock)

        return stack

# The solution is drastically simplified by using reverse indexing to peek at the top element of the stack
class simplifiedSolution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for cur_rock in asteroids:
            flag = True
            # Use negative indexing to peek at elements on the stack
            while len(stack) > 0 and (stack[-1] > 0 and cur_rock < 0):
                abs_last, abs_cur = abs(stack[-1]), abs(cur_rock)
                if abs_last < abs_cur:
                    # Top asteroid is smaller, it explodes and we cascade back
                    stack.pop()
                    continue
                elif abs_last == abs_cur:
                    # Asteroids are the same, break both and move on
                    stack.pop()
                
                # If we are here the current asteroid is destroyed and should not be added to the stack
                flag = 0
                break
            
            if flag:
                stack.append(cur_rock)
        
        return stack