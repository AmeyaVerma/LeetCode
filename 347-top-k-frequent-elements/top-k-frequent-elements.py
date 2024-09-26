class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        # Sort by frequency and get the top k elements
        return [item for item, freq in count.most_common(k)]