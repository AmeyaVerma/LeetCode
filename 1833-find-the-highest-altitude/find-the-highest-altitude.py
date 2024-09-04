class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res=0
        a=0
        for i in gain:
            a+=i
            res= max(res,a)
        return res