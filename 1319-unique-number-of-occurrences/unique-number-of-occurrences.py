class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        l={
            arr.count(i):i for  i in arr # key is count anvalue is the element to store unique counts
        }
        return len(l)==len(set(arr)) #returns boolean value       