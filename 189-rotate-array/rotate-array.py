class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k = k % n
        
        # Replace the entire array in-place using slicing
        nums[:] = nums[-k:] + nums[:-k]
