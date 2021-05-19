class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnter = collections.Counter(nums)
        return [x[0] for x in cnter.most_common(k)]