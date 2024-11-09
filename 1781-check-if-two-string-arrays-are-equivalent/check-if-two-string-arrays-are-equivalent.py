class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        var1,var2="",""
        for i in word1:
            var1=var1+i
        for j in word2:
            var2=var2+j
        if var1==var2:
            return True
        else:
            return False