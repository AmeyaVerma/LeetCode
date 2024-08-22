class Solution(object):
    def reverseVowels(self, s):
        s=list(s)
        w={"a","e","i","o","u","A","E","I","O","U"}
        l,r=0,len(s)-1
        while l<r:
            if s[l] not in w:
                l+=1
            elif s[r]  not in w:
                r-=1
            else:
                s[l],s[r]=s[r],s[l]
                l+=1
                r-=1
        return "".join(s)