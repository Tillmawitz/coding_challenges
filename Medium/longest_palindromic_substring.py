class too_slow_Solution:
    def longestPalindrome(self, s: str) -> str:
        hashtable = {}

        def is_palindrome(start, end) -> bool:
            substr = s[start:end]

            if (hashtable.get(substr) is not None) or end <= start:
                return True

            if len(substr) == 1:
                hashtable[substr] = 1
                return True
            elif substr[0] == substr[-1] and is_palindrome(start + 1, end - 1):
                hashtable[substr] = len(substr)
                return True
            else: 
                is_palindrome(start, end - 1)
                is_palindrome(start + 1, end)
                return False
        
        is_palindrome(0, len(s))

        return max(hashtable, key=hashtable.get)

# Time O(n ** 2) space O(n ** 2)
class dp_Solution:
    def longestPalindrome(self, s: str) -> str:
        palin_table = [[False] * len(s) for _ in range(len(s))]
        longest_indices = [0,0]

        for i in range(len(s)):
            palin_table[i][i] = True

        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                palin_table[i][i+1] = True
                longest_indices = [i, i+1]
        
        for dist in range(2, len(s)):
            for i in range(len(s) - dist):
                j = i + dist
                if s[i] == s[j] and palin_table[i+1][j-1]:
                    palin_table[i][j] = True
                    longest_indices = [i, j]

        i, j = longest_indices
        return s[i : j + 1]

# Time O(n ** 2) space O(1)
# while still O(n ** 2) will always have the same or fewer iterations than dp solution as there are O(n ** 2) bounds but O(n) centers and most centers will not produce long palindromes (worst case is all same character)
class expand_centers_Solution:
    def longestPalindrome(self, s: str) -> str: 
        def expand(i: int, j: int) -> int:
            left, right = i, j
            while left >=0 and right < len(s):
                if s[left] != s[right]:
                    break
                
                left -= 1
                right += 1
            
            # Loop breaks when bounds are exceeded or substring is no longer a palindrome, so distance is right - left + 1 - 2
            return right - left - 1
        
        ans = [0, 0]

        for i in range(len(s) - 1):
            odd_len = expand(i, i)
            if odd_len > ans[1] - ans[0] + 1:
                dist = odd_len // 2
                ans = [i - dist, i + dist]
            
            even_len = expand(i, i+1)
            if even_len > ans[1] - ans[0] + 1:
                dist = even_len // 2 - 1
                ans = [i - dist, i + 1 + dist]
            
        return s[ans[0] : ans[1] + 1]