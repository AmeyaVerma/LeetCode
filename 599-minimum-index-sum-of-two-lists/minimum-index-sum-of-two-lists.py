class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        mini = float('inf')
        res= []
        for idx2, i2 in enumerate(list1):
            for idx1, i1 in enumerate(list2):
                if i1==i2 and idx1+idx2<= mini:
                    if res is None or idx1+idx2==mini:
                        print("Hitting")
                        res.append(i2)
                    # elif res is not None and idx1+idx2<mini:
                    else:
                        res=[]
                        res.append(i2)
                    
                    mini= idx2+idx1
                    break
        return res
        # for idx_list2,i in enumerate(list2):
        #     if i in list1:
        #         idx_of_element = [index for index, value in enumerate(list1) if value == i]
        #         for idx_list1 in range(len(idx_of_element)):
        #             mini= min(idx_list1-idx_list2)
        # return mini if mini>0 else -mini