class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainder={}
        for i in range(len(nums)):
            tot= target-nums[i]
            if tot in remainder:
                return [i,remainder[tot]]
            else:
                remainder[nums[i]]=i