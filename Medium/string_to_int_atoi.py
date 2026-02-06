"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

    Whitespace: Ignore any leading whitespace (" ").
    Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
    Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
    Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.

Return the integer as the final result.

Example 1:

Input: s = "42"

Output: 42

Explanation:

The underlined characters are what is read in and the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^

Example 2:

Input: s = " -042"

Output: -42

Explanation:

Step 1: "   -042" (leading whitespace is read and ignored)
            ^
Step 2: "   -042" ('-' is read, so the result should be negative)
             ^
Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
               ^

Example 3:

Input: s = "1337c0d3"

Output: 1337

Explanation:

Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
         ^
Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)
             ^

Example 4:

Input: s = "0-1"

Output: 0

Explanation:

Step 1: "0-1" (no characters read because there is no leading whitespace)
         ^
Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit)
          ^

Example 5:

Input: s = "words and 987"

Output: 0

Explanation:

Reading stops at the first non-digit character 'w'.

Constraints:

    0 <= s.length <= 200
    s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.
"""

# Given we are not limited to storing 32-bit integers, I work with the assumption that we can convert the string then check if it exceeds the valid bounds of a 32-bit integer. If this were not the case we would need to instead us the "optimal" solution, however mine runs slightly faster if the assumption is valid
class mySolution:
    def myAtoi(self, s: str) -> int:
        stripped = s.strip()
        sign = 1
        ans = 0
        reading_num = False
        start = end = 0

        if len(stripped) == 0:
            return 0
        elif stripped[0] == "-":
            sign = -1
            stripped = stripped[1:]
        elif stripped[0] == "+":
            stripped = stripped[1:]

        for ind, char in enumerate(stripped):
            if not char.isnumeric():
                break

            if not reading_num and char != "0":
                reading_num = True
                start = ind
            
            if reading_num:
                end = ind
        

        if not reading_num:
            return 0

        num_string = stripped[start : end + 1]
        ans = int(num_string) * sign
        if ans > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif ans < -2 ** 31:
            return -2 ** 31
        else:
            return ans

class optimalSolution:
    def myAtoi(self, input: str) -> int:
        sign = 1
        result = 0
        index = 0
        n = len(input)

        INT_MAX = pow(2, 31) - 1
        INT_MIN = -pow(2, 31)

        # Discard all spaces from the beginning of the input string.
        while index < n and input[index] == " ":
            index += 1

        # sign = +1, if it's positive number, otherwise sign = -1.
        if index < n and input[index] == "+":
            sign = 1
            index += 1
        elif index < n and input[index] == "-":
            sign = -1
            index += 1

        # Traverse next digits of input and stop if it is not a digit.
        # End of string is also non-digit character.
        while index < n and input[index].isdigit():
            digit = int(input[index])

            # Check overflow and underflow conditions.
            if (result > INT_MAX // 10) or (
                result == INT_MAX // 10 and digit > INT_MAX % 10
            ):
                # If integer overflowed return 2^31-1, otherwise if underflowed return -2^31.
                return INT_MAX if sign == 1 else INT_MIN

            # Append current digit to the result.
            result = 10 * result + digit
            index += 1

        # We have formed a valid number without any overflow/underflow.
        # Return it after multiplying it with its sign.
        return sign * result

"""
State Machine

Treating the problem as a DFA is interesting as an exersice, but ultimately not very practical. Mostly a show off solution to demonstrate knowledge of Theory of Computation.
"""

class StateMachine:
    def __init__(self):
        self.State = {"q0": 1, "q1": 2, "q2": 3, "qd": 4}
        self.INT_MAX, self.INT_MIN = pow(2, 31) - 1, -pow(2, 31)

        # Store current state value.
        self.__current_state = self.State["q0"]
        # Store result formed and its sign.
        self.__result = 0
        self.__sign = 1

    def to_state_q1(self, ch: chr) -> None:
        """Transition to state q1."""
        self.__sign = -1 if (ch == "-") else 1
        self.__current_state = self.State["q1"]

    def to_state_q2(self, digit: int) -> None:
        """Transition to state q2."""
        self.__current_state = self.State["q2"]
        self.append_digit(digit)

    def to_state_qd(self) -> None:
        """Transition to dead state qd."""
        self.__current_state = self.State["qd"]

    def append_digit(self, digit: int) -> None:
        """Append digit to result, if out of range return clamped value."""
        if (self.__result > self.INT_MAX // 10) or (
            self.__result == self.INT_MAX // 10 and digit > self.INT_MAX % 10
        ):
            if self.__sign == 1:
                # If sign is 1, clamp result to INT_MAX.
                self.__result = self.INT_MAX
            else:
                # If sign is -1, clamp result to INT_MIN.
                self.__result = self.INT_MIN
                self.__sign = 1

            # When the 32-bit int range is exceeded, a dead state is reached.
            self.to_state_qd()
        else:
            # Append current digit to the result.
            self.__result = (self.__result * 10) + digit

    def transition(self, ch: chr) -> None:
        """Change state based on current input character."""
        if self.__current_state == self.State["q0"]:
            # Beginning state of the string (or some whitespaces are skipped).
            if ch == " ":
                # Current character is a whitespaces.
                # We stay in same state.
                return
            elif ch == "-" or ch == "+":
                # Current character is a sign.
                self.to_state_q1(ch)
            elif ch.isdigit():
                # Current character is a digit.
                self.to_state_q2(int(ch))
            else:
                # Current character is not a space/sign/digit.
                # Reached a dead state.
                self.to_state_qd()

        elif (
            self.__current_state == self.State["q1"]
            or self.__current_state == self.State["q2"]
        ):
            # Previous character was a sign or digit.
            if ch.isdigit():
                # Current character is a digit.
                self.to_state_q2(int(ch))
            else:
                # Current character is not a digit.
                # Reached a dead state.
                self.to_state_qd()

    def get_integer(self) -> int:
        """Return the final result formed with it's sign."""
        return self.__sign * self.__result

    def get_state(self) -> int:
        """Get current state."""
        return self.__current_state


class dfaSolution:
    def myAtoi(self, input: str) -> int:
        q = StateMachine()

        for ch in input:
            q.transition(ch)
            if q.get_state() == q.State["qd"]:
                break

        return q.get_integer()