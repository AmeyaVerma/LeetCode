class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        l = max(candies)
        return[(val+extraCandies)>=l for val in candies]
        