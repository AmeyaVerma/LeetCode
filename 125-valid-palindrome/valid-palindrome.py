class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        k=""
        for i in s:
            if i.isalnum():
                k+=i
        return k== k[::-1]