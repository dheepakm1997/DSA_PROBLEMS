# Count number of odd digits in a number
# Easy

# Company
# You are given an integer n. You need to return the number of odd digits present in the number.



# The number will have no leading zeroes, except when the number is 0 itself.


# Example 1

# Input: n = 5

# Output: 1

# Explanation: 5 is an odd digit.

# Example 2

# Input: n = 25

# Output: 1

# Explanation: The only odd digit in 25 is 5.

# Example 3

# Input: n = 15

# Output:

# 2

class Solution:
    # Function to count number
    # of odd digits in N
    def countOddDigit(self, n):
        # Counter to store the 
        # number of odd digits
        oddDigits = 0

        # Iterate till there are digits left
        while n > 0:
            # Extract last digit
            lastDigit = n % 10
            
            # Check if digit is odd
            if lastDigit % 2 != 0:
                # Increment counter
                oddDigits = oddDigits + 1
            n = n // 10

        return oddDigits

# Input number
n = 6678

# Creating an instance of 
# Solution class
sol = Solution()

# Function call to get count of odd digits in n
ans = sol.countOddDigit(n)
print("The count of odd digits in the given number is:", ans)
