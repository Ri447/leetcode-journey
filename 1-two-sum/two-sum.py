class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pM = {}
        for i, n in enumerate(nums):
            diff = target-n
            if diff in pM:
                return [pM[diff],i]
            pM[n] = i
        return