class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        reverse_x= str(x)
        reverse_x=reverse_x[::-1]
        reverse_x=int(reverse_x)
        if reverse_x== x:
            return True
        else:
            return False