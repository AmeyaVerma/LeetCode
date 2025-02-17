class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hashset=set()
        index=0
        for num in nums:
            if num not in hashset:
                hashset.add(num)
                nums[index]=num
                index +=1
        return index