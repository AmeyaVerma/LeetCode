class Solution(object):
    def maxOperations(self, nums, k):
        c=Counter(nums)
        seen=set()
        output=0

        for x in c:
            if x not in seen and (k-x) in c:
                if x==(k-x):
                    output+=c[x]//2
                else:
                    output+=min(c[x],c[k-x])
                    seen.add(x)
                    seen.add(k-x)
        return output
