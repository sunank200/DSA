"""
125. Valid Palindrome
Solved
Easy
Topics
Companies
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        1. take two pointers one from front and another from back
        2. iterate front and back till they are equal. return False if anything doesn't match. Skip non alphabet
        """
        front = 0
        back = len(s) - 1

        while front < back:
            while front < len(s) and not s[front].isalnum():
                front += 1
            while not s[back].isalnum() and back > 0:
                back -= 1
            if front >= back:
                return True
            if s[front].lower() != s[back].lower():
                return False
            front += 1
            back -= 1
        return True

solution = Solution()
s = "A man, a plan, a canal: Panama"
b = ".,"
print(solution.isPalindrome(s=s))
print(solution.isPalindrome(s=b))