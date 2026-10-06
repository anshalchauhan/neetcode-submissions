class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        for n in nums:
            hashmap[n] += 1
        
        maj = 0
        ans = 0
        for key in hashmap:
            if hashmap[key] > maj:
                maj = hashmap[key]
                ans = key
        
        return ans