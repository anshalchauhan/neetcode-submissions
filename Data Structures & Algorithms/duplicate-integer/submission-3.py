class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # O(n) solution
        my_dict = {}
        for num in nums:
            if num in my_dict:
                return True
            else:
                my_dict[num] = 1
        return False

        