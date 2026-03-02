"""
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

    If the group's length is 1, append the character to s.
    Otherwise, append the character followed by the group's length.

The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

Note: The characters in the array beyond the returned length do not matter and should be ignored.

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.

Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".

Constraints:
    1 <= chars.length <= 2000
    chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.
"""

# Fastest category of solutions, uses a bit more memory though
class mySolution:
    def compress(self, chars: List[str]) -> int:
        replace_ind = 0
        sub_str_start = 0

        for ind, char in enumerate(chars):
            if char != chars[sub_str_start]:
                chars[replace_ind] = chars[sub_str_start]
                replace_ind += 1
                sub_len = ind - sub_str_start

                if sub_len > 1:
                    num_string = str(sub_len)
                    for num_char in num_string:
                        chars[replace_ind] = num_char
                        replace_ind += 1
                
                sub_str_start = ind
        
        chars[replace_ind] = chars[sub_str_start]
        replace_ind += 1
        final_sub_len = len(chars) - sub_str_start
        if final_sub_len > 1:
            num_string = str(final_sub_len)
            for num_char in num_string:
                chars[replace_ind] = num_char
                replace_ind += 1

        return replace_ind

# A bit cleaner, don't need to repeat last step outside loop which is much better. Ultimately the same solution, just cleaned up a bit. If I rewrote my solution using a while loop instead of for loop or used an explicit check for the end I can easily remove the duplicate code.
class optimalSolution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        res = 0
        while i < len(chars):
            group_length = 1
            while (i + group_length < len(chars)
                   and chars[i + group_length] == chars[i]):
                group_length += 1
            chars[res] = chars[i]
            res += 1
            if group_length > 1:
                str_repr = str(group_length)
                chars[res:res+len(str_repr)] = list(str_repr)
                res += len(str_repr)
            i += group_length
        return res