# <!-- Count all Digits of a Number
# Easy

# Company
# You are given an integer n. You need to return the number of digits in the number.



# The number will have no leading zeroes, except when the number is 0 itself.


# Example 1

# Input: n = 4

# Output: 1

# Explanation: There is only 1 digit in 4.

# Example 2

# Input: n = 14

# Output: 2

# Explanation: There are 2 digits in 14.

# Now your turn!

# Input: n = 234

# Output:

# Pick your answer -->

class Solution:
    # Function to count all digits in n
    def countDigit(self, n):
        # Edge case
        if n == 0:
            return 1

        # Set counter to 0
        cnt = 0

        # Iterate until n is greater than zero
        while n > 0:
            # Increment count of digits
            cnt = cnt + 1
            n = n // 10

        return cnt

# Input number
n = 6678

# Creating an instance of Solution class
sol = Solution()

# Function call to get count of digits in n
ans = sol.countDigit(n)
print(f"The count of digits in the given number is: {ans}")
