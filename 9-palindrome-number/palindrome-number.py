class Solution:
    def isPalindrome(self, x):
        f=str(x)
        return f==f[::-1]