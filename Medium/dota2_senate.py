"""
In the world of Dota2, there are two parties: the Radiant and the Dire.

The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:

    Ban one senator's right: A senator can make another senator lose all his rights in this and all the following rounds.
    Announce the victory: If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and decide on the change in the game.

Given a string senate representing each senator's party belonging. The character 'R' and 'D' represent the Radiant party and the Dire party. Then if there are n senators, the size of the given string will be n.

The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.

Suppose every senator is smart enough and will play the best strategy for his own party. Predict which party will finally announce the victory and change the Dota2 game. The output should be "Radiant" or "Dire".

Example 1:

Input: senate = "RD"
Output: "Radiant"
Explanation: 
The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
And the second senator can't exercise any rights anymore since his right has been banned. 
And in round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.

Example 2:

Input: senate = "RDD"
Output: "Dire"
Explanation: 
The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
And the second senator can't exercise any rights anymore since his right has been banned. 
And the third senator comes from Dire and he can ban the first senator's right in round 1. 
And in round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.

Constraints:

    n == senate.length
    1 <= n <= 104
    senate[i] is either 'R' or 'D'.
"""

from collections import deque
# I was so close with my initial approach, I just needed to add a queue to account for the multiple rounds of voting. By adding members to the end of the queue we can track the "rounds" by continuing to iterate through the entries. The other solutions are things I attempted in order, and kept almost implementing the correct solution
class workingSolution:
    def predictPartyVictory(self, senate: str) -> str:
        r_count = senate.count("R")
        d_count = len(senate) - r_count

        r_bans = 0
        d_bans = 0

        q = deque(senate)
        while r_count and d_count:
            curr = q.popleft()

            if curr == "D":
                if d_bans:
                    d_bans -= 1
                    d_count -= 1
                else:
                    r_bans += 1
                    q.append(curr)
            else:
                if r_bans:
                    r_bans -= 1
                    r_count -= 1
                else:
                    d_bans += 1
                    q.append(curr)
            
        return "Radiant" if r_count else "Dire"

# Doesn't work, there can be multiple rounds of voting like in the case of "DDRRR". We need to keep track of the resulting string in case there are more rounds.
class initialSolution:
    def predictPartyVictory(self, senate: str) -> str:
        r_left, r_powers = 0,0
        d_left, d_powers = 0,0

        for char in senate:
            if char == "R":
                # If there are d members with powers, this member will have been removed
                if d_powers > 0:
                    d_powers -= 1
                    continue

                # Add member to counts
                r_left += 1
                r_powers += 1

                # If there are d members earlier in the line who have already used their powers, they get removed
                if d_left > 0:
                    d_left -= 1
                    r_powers -= 1
            else:
                if r_powers > 0:
                    r_powers -= 1
                    continue
                
                d_left += 1
                d_powers += 1

                if r_left > 0:
                    r_left -= 1
                    d_powers -= 1
        
        if r_left > 0:
            return "Radiant"
        else:
            return "Dire"

# Voting for the earliest opponent is not the optimal strategy, you want to vote for the next opponent then if you have left over power remove opponents from the front
class incorrectSolution:
    def predictPartyVictory(self, senate: str) -> str:
        r_powers = d_powers = 0
        tmp_str = senate
        q = deque()
        
        while len(tmp_str) > 0:
            all_r = True
            all_d = True

            for char in tmp_str:
                if char == "R":
                    all_d = False
                    # If there are d members with powers, this member will be removed
                    if d_powers > 0:
                        d_powers -= 1
                        continue

                    # If there is a D member at the end, they will get removed
                    if len(q) > 0 and q[0] == "D":
                        q.popleft()
                    else:
                        # If not, add R power
                        r_powers += 1
                else:
                    all_r = False

                    if r_powers > 0:
                        r_powers -= 1
                        continue
                    
                    if len(q) > 0 and q[0] == "R":
                        q.popleft()
                    else:
                        d_powers += 1
                    
                q.append(char)
            
            if all_r:
                return "Radiant"
            elif all_d:
                return "Dire"

            tmp_str = "".join(q)
            q.clear()

# Remove the next opposing senator, if you have leftover power remove the opponent from the beginning. This fails because we always want to remove the LATEST opponent, when we have leftover votes we start at the beginning
class anotherWrongSolution:
    def predictPartyVictory(self, senate: str) -> str:
        r_powers = d_powers = 0
        tmp_str = senate
        q = deque()
        
        while len(tmp_str) > 0:
            all_r = True
            all_d = True

            for char in tmp_str:
                if char == "R":
                    all_d = False
                    if d_powers > 0:
                        d_powers -= 1
                        continue
                    
                    r_powers += 1
                else:
                    all_r = False
                    if r_powers > 0:
                        r_powers -= 1
                        continue
                    
                    d_powers += 1
                
                q.append(char)
            
            if all_d:
                return "Dire"
            elif all_r:
                return "Radiant"
            
            tmp_str = ""
            while r_powers > 0:
                if q[0] == "R":
                    return "Radiant"
                else:
                    q.popleft()
                    r_powers -= 1
            
            while d_powers > 0:
                if q[0] == "D":
                    return "Dire"
                else:
                    q.popleft()
                    d_powers -= 1

            tmp_str = tmp_str + "".join(q)
            q.clear()