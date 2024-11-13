class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maps1={}
        res=[]
        for num in nums:
            if num in maps1:
                maps1[num]+=1
            else:
                maps1[num]=1
        sorted_items = sorted(maps1.items(), key=lambda item: item[1], reverse=True)
        
        for i in range(k):
            res.append(sorted_items[i][0])
        
        return res
