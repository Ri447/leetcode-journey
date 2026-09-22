class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        n = len(nums)
        r = [nums[0]]
        for i in range(1, n):
            r.append(r[-1] + nums[i])
        return r