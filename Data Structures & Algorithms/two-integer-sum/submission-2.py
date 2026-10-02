class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n) time and O(n) space solution
        hashmap = {}
        for i in range(len(nums)):
            if target - nums[i] in hashmap:
                return [hashmap[target - nums[i]], i]
            hashmap[nums[i]] = i
            