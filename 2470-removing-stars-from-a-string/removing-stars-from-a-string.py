class Solution:
    def removeStars(self, s: str) -> str:
        res=[]
        for n in s:
            if n== "*":
                res and res.pop()
            else:
                res.append(n)
        return "".join(res)
                