class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        t= [0]+ flowerbed + [0]
        for i in range (1,len(t)-1):
            if t[i-1]==0 and t[i]==0 and t[i+1]==0:
                t[i]=1
                n-=1
        return n<=0
