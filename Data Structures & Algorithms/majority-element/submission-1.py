class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans, maxi = 0, 0
        for n in nums:
            if ans == n:
                maxi += 1
            else:
                if maxi == 0:
                    ans = n
                    maxi += 1
                else:
                    maxi -= 1
        
        return ans