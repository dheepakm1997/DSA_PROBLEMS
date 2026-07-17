# You are given an integer n. Return the integer formed by placing the digits of n in reverse order.


# Example 1

# Input: n = 25

# Output: 52

# Explanation: Reverse of 25 is 52.

# Example 2

# Input: n = 123

# Output: 321

# Explanation: Reverse of 123 is 321.

# Now your turn!

# Input: n = 54

# Output:

# Correct

class Solution:
    def revnum(self,n):
        revNum=0
        while n > 0:
            last_digit = n % 10
            revNum = (revNum * 10) + last_digit
            n= n //10
        return revNum

   
if __name__ =="__main__":

    n = 6678 

    sol = Solution()
    ans= sol.revnum(n)
    print(f" The reversed numbers is {ans}")