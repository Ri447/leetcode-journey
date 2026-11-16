class Solution:
    def findLHS(self, nums: List[int]) -> int:

        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        max_length = 0

        for num in count:
            if num + 1 in count:
                length = count[num] + count[num + 1]
                max_length = max(max_length, length)

        return max_length