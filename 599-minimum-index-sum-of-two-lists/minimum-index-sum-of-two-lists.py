class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        same = [word for word in list1 if word in list2]
        same.sort()
        dic={}
        for word in same:
            idx1=list1.index(word)
            idx2=list2.index(word)
            dic[word]=idx1+idx2
        
        dic = dict(sorted(dic.items(), key=lambda item: item[1]))
        val=list(dic.values())
        val.sort()
        small=val[0]
        res=[]

        for word in dic:
            if dic[word]==small:
                res.append(word)
        return res



        
            

        
        