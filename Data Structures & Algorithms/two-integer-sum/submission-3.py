class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n) time and O(n) space solution
        hashmap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[n] = i
        return
            