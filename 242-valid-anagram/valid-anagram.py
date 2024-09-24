class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sortes_s= sorted(s)
        sorted_t=sorted(t)
        return sortes_s==sorted_t